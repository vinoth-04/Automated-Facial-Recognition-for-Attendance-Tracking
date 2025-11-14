# 📸 Smart Face Recognition-Based Attendance System

An AI-powered biometric solution using facial recognition to automate attendance tracking. Real-time face detection via webcam, secure login/logout status recording, timestamp-based logging, and web interface built with Streamlit for easy accessibility and data management.

## ✨ Features

- **Real-time Face Recognition** - Identifies individuals using advanced facial recognition algorithms
- **Automated Attendance Tracking** - Automatic login/logout recording with timestamps
- **Web-Based Interface** - User-friendly Streamlit application for easy access
- **Duplicate Prevention** - Prevents invalid status transitions (e.g., logout without login)
- **CSV-Based Logging** - Attendance records stored in CSV format for easy analysis
- **Face Encoding Storage** - Efficient face encoding using pickle for fast recognition
- **Dynamic Face Addition** - Add new users without retraining the entire model

## 🛠️ Tech Stack

- **Python 3.x** - Core programming language
- **Streamlit** - Web framework for interactive UI
- **OpenCV (cv2)** - Computer vision and image processing
- **face_recognition** - Facial recognition library
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **Pickle** - Serialization for face encodings

## 📁 Project Structure

```
face-recognition-attendance/
├── main.py                    # Main Streamlit web application
├── train_encoding.py          # Generate and save face encodings
├── add_face.py               # Add new faces to the system
├── test.py                   # Standalone face recognition with webcam
├── attendance.csv            # Attendance records
├── face_encodings.pkl        # Stored face encodings
├── known_face/               # Directory with training images
│   ├── rohit/               # Individual's face images
│   ├── virat/               # Individual's face images
│   └── [person_name]/       # Add more people here
├── requirement.txt           # Python dependencies
└── README.md                # Project documentation
```

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- Webcam/Camera for face capture
- Windows/Mac/Linux OS

### Setup Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/face-recognition-attendance.git
   cd face-recognition-attendance
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirement.txt
   ```

4. **Organize known faces:**
   - Create folders inside `known_face/` for each person
   - Add 3-5 clear face images per person (jpg, jpeg, png)
   ```
   known_face/
   ├── rohit/
   │   ├── image1.jpg
   │   ├── image2.jpg
   └── virat/
       ├── image1.jpg
       ├── image2.jpg
   ```

## 📖 Usage

### Option 1: Train Face Encodings (First Time Only)
```bash
python train_encoding.py
```
This generates `face_encodings.pkl` with all known face data.

### Option 2: Add New Person
```bash
python add_face.py
```
Follow prompts to add a new person's faces to the system.

### Option 3: Run Web Application
```bash
streamlit run main.py
```
- Open browser at `http://localhost:8501`
- Capture your face using the camera
- Select "Login" or "Logout"
- Click "Submit" to record attendance

### Option 4: Test with Webcam
```bash
python test.py
```
Real-time face recognition without attendance logging. Press 'q' to exit.

## 📊 Attendance Record

Records are saved in `attendance.csv` with columns:
- **Name** - Person's name
- **Status** - Login or Logout
- **Time** - Timestamp of the record

Example:
```
Name,Status,Time
rohit,Login,2025-11-14 09:30:45
rohit,Logout,2025-11-14 17:45:30
virat,Login,2025-11-14 09:15:00
```

## 🎯 How It Works

1. **Face Encoding** - Face images are converted to 128-dimensional encodings
2. **Storage** - Encodings are saved in `face_encodings.pkl`
3. **Recognition** - Captured face is compared against known encodings
4. **Logging** - Matching face triggers attendance record creation
5. **Validation** - System ensures valid status transitions

## ⚠️ Requirements

Create `requirement.txt`:
```
streamlit
opencv-python
face-recognition
numpy
pandas
pillow
```

Or install directly:
```bash
pip install streamlit opencv-python face-recognition numpy pandas pillow
```

## 🔒 Security Considerations

- Encodings are stored locally in `face_encodings.pkl`
- No images are stored after encoding
- CSV file contains only attendance records (names, status, time)
- For production use, consider database encryption

## 🐛 Troubleshooting

**Issue: "No faces found" in images**
- Ensure images are clear and face is visible
- Use well-lit environments
- Add more training images per person

**Issue: False positives (wrong person recognized)**
- Add more diverse training images
- Increase face distance threshold in code
- Use higher quality images

**Issue: Streamlit app not opening**
- Check if port 8501 is available
- Try: `streamlit run main.py --server.port 8502`

## 📝 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

Created by: VINOTH KUMAR A
GitHub: https://github.com/vinoth-04

## 🤝 Contributing

Feel free to fork, modify, and contribute improvements!

## 📞 Support

For issues or questions, please create an issue in the repository.

---

**Happy coding! 🚀**
