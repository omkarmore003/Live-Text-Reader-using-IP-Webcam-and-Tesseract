import cv2
import pytesseract
import pyttsx3

# Set path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Use video stream instead of snapshot
IP_CAMERA_URL = "http://172.27.121.132:8080/video"

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak_text(text):
    if text.strip():
        print("[INFO] Reading text aloud...")
        engine.say(text)
        engine.runAndWait()
    else:
        print("[INFO] No text detected to read.")

def extract_text_from_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    text = pytesseract.image_to_string(gray)
    print("[INFO] Detected Text:\n", text.strip())
    return text.strip()

def main():
    print("[INFO] Starting IP Webcam OCR...")
    cap = cv2.VideoCapture(IP_CAMERA_URL)

    if not cap.isOpened():
        print("[ERROR] Unable to open video stream from IP Webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[WARNING] Failed to grab frame.")
            continue

        cv2.imshow("IP Webcam Feed - Press 'q' to quit", frame)

        # Extract and read text every 3 seconds
        key = cv2.waitKey(1) & 0xFF
        if cv2.getTickCount() % 90 == 0:  # Roughly every ~3 sec (30 FPS assumed)
            text = extract_text_from_frame(frame)
            speak_text(text)

        if key == ord('q'):
            print("[INFO] Exiting...")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
