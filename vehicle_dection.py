import cv2

# Load the Haar Cascade for car detection
# Ensure haarcascade_car.xml is in the same directory as this script.
# You can get this file using the get_cascades.py script from the previous step.
car_cascade = cv2.CascadeClassifier('haarcascade_car.xml')

# Check if the cascade file loaded correctly
if car_cascade.empty():
    raise Exception("Error loading haarcascade_car.xml. Make sure the file is in the correct path.")

# Create a VideoCapture object to read from the webcam (usually index 0)
cap = cv2.VideoCapture(0)

# Check if the webcam was opened successfully
if not cap.isOpened():
    print("Error: Could not open video stream from webcam.")
    exit()

while True:
    # Read a single frame from the video stream
    ret, frame = cap.read()

    # Break the loop if the frame could not be read
    if not ret:
        break

    # Convert the frame to grayscale for faster processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect cars in the frame
    # The detectMultiScale function detects objects of different sizes in the input image.
    # It returns a list of rectangles, each representing a detected car.
    cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    # Draw rectangles around the detected cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the result in a window
    cv2.imshow('Vehicle Detection', frame)

    # Press 'q' to exit the video stream
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
