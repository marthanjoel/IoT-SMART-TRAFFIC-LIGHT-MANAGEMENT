import cv2
import sys

# --- Load the Haar Cascade XML file ---
cascade_path = '/home/user/IOT-BASED-SMART-TRAFFIC-LIGHT-MANAGEMENT-SYSTEM.-/cars3.xml'
car_cascade = cv2.CascadeClassifier(cascade_path)

if car_cascade.empty():
    print(f"Error: Cannot load cascade file at {cascade_path}")
    sys.exit()

# --- Open video capture (0 for webcam, or replace with video file path) ---
cap = cv2.VideoCapture(0)  # Change 0 to 'video.mp4' if using a file

if not cap.isOpened():
    print("Error: Cannot open video source")
    sys.exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Cannot read frame from video")
        break

    # Optional: crop the frame safely
    frame = frame[120:, :-20] if frame.shape[0] > 120 and frame.shape[1] > 20 else frame

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow('Vehicle Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
