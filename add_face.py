import face_recognition
import os
import pickle

# Load existing data
with open("face_encodings.pkl", "rb") as f:
    data = pickle.load(f)

known_encodings = data["encodings"]
known_names = data["names"]

# Ask for the new person's name
person_name = input("Enter the name of the person to add: ")
person_folder = os.path.join("known_face", person_name)

if not os.path.exists(person_folder):
    print(f"[ERROR] Folder '{person_folder}' not found!")
    exit()

print(f"[INFO] Adding new face(s) for {person_name}...")

for filename in os.listdir(person_folder):
    img_path = os.path.join(person_folder, filename)
    if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    image = face_recognition.load_image_file(img_path)
    encodings = face_recognition.face_encodings(image)
    if len(encodings) > 0:
        known_encodings.append(encodings[0])
        known_names.append(person_name)
        print(f"✅ Added {filename}")

# Save the updated data
data = {"encodings": known_encodings, "names": known_names}
with open("face_encodings.pkl", "wb") as f:
    pickle.dump(data, f)

print(f"[INFO] {person_name} added successfully to model!")
