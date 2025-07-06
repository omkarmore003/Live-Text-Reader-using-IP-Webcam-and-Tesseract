# 📷 Live-Text-Reader-using-IP-Webcam-and-Tesseract 🔊

This project captures real-time video from an Android IP Webcam, detects visible text using Tesseract OCR, and reads it aloud using a built-in Text-to-Speech (TTS) engine. It's designed as an assistive tool for reading text from signs, documents, or screens using a mobile phone camera.

---

## 🚀 Features

- 📡 Live video feed from Android IP Webcam  
- 🔎 Optical Character Recognition (OCR) using Tesseract  
- 🔊 Real-time audio feedback with pyttsx3 (Text-to-Speech)  
- 🖥️ Simple OpenCV-based GUI with live preview  
- 🕒 Periodic auto text detection (every ~3 seconds)  
- ❌ Press `q` to exit anytime  

---

## 🧰 Requirements

- Python 3.6+
- Tesseract OCR installed on your system
- IP Webcam app (Android) or any IP-based video stream

### 🔧 Python Libraries

Install via `requirements.txt`:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install opencv-python pytesseract pyttsx3
```

---

## 🛠️ Installation

1. **Install Tesseract OCR**

- Download from: [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
- Set the path in your Python code:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

2. **Connect Your Android IP Webcam**

- Install **IP Webcam** app from the Play Store.
- Start server in the app, note the IP (e.g., `http://192.168.1.100:8080`)
- Set this in your code:

```python
IP_CAMERA_URL = "http://<your_ip_address>:8080/video"
```

3. **Run the Project**

```
python text.py
```

---

## 📂 File Structure

```
IP-Webcam-OCR-TTS/
├── text.py               # Main application script
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── LICENSE               # Optional: MIT license
```

---

## 🎯 How It Works

1. Connect to a live video stream from your mobile phone using IP Webcam.
2. Capture frames from the feed using OpenCV.
3. Convert the frame to grayscale and binarize it.
4. Extract text using Tesseract OCR.
5. If text is detected, speak it using pyttsx3 TTS.

---

## 🧪 Sample Output

```
[INFO] Starting IP Webcam OCR...
[INFO] Detected Text:
Hello, World!
[INFO] Reading text aloud...
```

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Omkar More**  
GitHub: [@omkarmore003](https://github.com/omkarmore003)

---

## 💡 Future Improvements

- Add language translation before TTS
- Implement button or voice trigger instead of time-based OCR
- Improve OCR accuracy with preprocessing filters

---


## 🗨️ Feedback & Contributions

Pull requests, issues, and suggestions are welcome! Let's build better accessibility tools together. ✨
