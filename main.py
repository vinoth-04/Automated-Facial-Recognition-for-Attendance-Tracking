import streamlit as st
import cv2
import face_recognition
import numpy as np
import os
import pandas as pd
import pickle
from datetime import datetime

st.set_page_config(page_title="Face Attendance", layout="wide")
os.makedirs("known face", exist_ok=True)

csv_file = "attendance.csv"
pickle_file = "face_encodings.pkl"
if not os.path.exists(csv_file):
    pd.DataFrame(columns=["Name", "Status", "Time"]).to_csv(csv_file, index=False)
@st.cache_resource
def load_or_build_encodings():
    if os.path.exists(pickle_file):
        with open(pickle_file, "rb") as f:
            data = pickle.load(f)
        st.success("✅ Loaded known faces from face_encodings.pkl")
        return data["encodings"], data["names"]
    else:
        st.warning("⚠️ No pickle file found — generating...")
        encodings, names = [], []
        for name in os.listdir("known face"):
            person_folder = os.path.join("known face", name)
            if not os.path.isdir(person_folder): continue
            for fn in os.listdir(person_folder):
                if fn.lower().endswith((".png", ".jpg", ".jpeg")):
                    img = face_recognition.load_image_file(os.path.join(person_folder, fn))
                    face_encs = face_recognition.face_encodings(img)
                    if face_encs:
                        encodings.append(face_encs[0])
                        names.append(name)
        with open(pickle_file, "wb") as f:
            pickle.dump({"encodings": encodings, "names": names}, f)
        st.success("💾 Encodings saved.")
        return encodings, names

known_encodings, known_names = load_or_build_encodings()
def can_mark(name, status):
    df = pd.read_csv(csv_file)
    df["Time"] = pd.to_datetime(df["Time"])
    today = datetime.now().date()
    today_entries = df[df["Time"].dt.date == today]
    person_entries = today_entries[today_entries["Name"] == name].sort_values("Time", ascending=False)
    if person_entries.empty:
        return status == "Login"
    last = person_entries.iloc[0]
    return (last["Status"] == "Login" and status == "Logout") or \
           (last["Status"] == "Logout" and status == "Login")

st.title("📸 Smart Face Attendance System")

uploaded = st.camera_input("📸 Capture your face")

if uploaded:
    bytes_data = uploaded.getvalue()
    nparr = np.frombuffer(bytes_data, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locs = face_recognition.face_locations(rgb)
    face_encs = face_recognition.face_encodings(rgb, face_locs)

    recognized = None
    if face_encs:
        for enc in face_encs:
            matches = face_recognition.compare_faces(known_encodings, enc)
            dists = face_recognition.face_distance(known_encodings, enc)
            if len(dists) > 0:
                idx = np.argmin(dists)
                if matches[idx]:
                    recognized = known_names[idx]
                    break

    if recognized:
        st.success(f"✅ Welcome, {recognized}!")
        status = st.radio("Status:", ["Login", "Logout"], key="status")
        if st.button("✅ Submit"):
            if can_mark(recognized, status):
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                new_row = pd.DataFrame([[recognized, status, now]], columns=["Name", "Status", "Time"])
                df = pd.read_csv(csv_file)
                df = pd.concat([df, new_row], ignore_index=True)
                df.to_csv(csv_file, index=False)
                st.balloons()
                st.info(f"✔️ {recognized} marked as **{status}** at {now}")
            else:
                st.error("⚠️ Invalid action — check your last status.")
    else:
        st.warning("❌ No known face detected.")
st.subheader("📋 Attendance Log")
df_log = pd.read_csv(csv_file)
if not df_log.empty:
    df_log["Time"] = pd.to_datetime(df_log["Time"])
    df_log = df_log.sort_values("Time", ascending=False)
st.dataframe(df_log)