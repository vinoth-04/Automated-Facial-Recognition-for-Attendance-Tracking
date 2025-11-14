import face_recognition
import os
import pickle

known_encodings = []
known_names = []

# Loop through each person folder inside "known_face"
for name in os.listdir("known_face"):
    person_folder = os.path.join("known_face", name)
    if not os.path.isdir(person_folder):
        continue

    print(f"[INFO] Processing {name}...")
    for filename in os.listdir(person_folder):
        img_path = os.path.join(person_folder, filename)
        if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        image = face_recognition.load_image_file(img_path)
        encodings = face_recognition.face_encodings(image)
        if len(encodings) > 0:
            known_encodings.append(encodings[0])
            known_names.append(name)

# Save encodings and names into one file
data = {"encodings": known_encodings, "names": known_names}
with open("face_encodings.pkl", "wb") as f:
    pickle.dump(data, f)

print("[INFO] Encoding model saved as 'face_encodings.pkl'")
