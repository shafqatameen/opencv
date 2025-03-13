import cv2 as cv

# Open the default camera (0), or use 1, 2 for external cameras
capture = cv.VideoCapture(0)

# Check if the camera opened successfully
if not capture.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    isTrue, frame = capture.read()

    if not isTrue:  # Break if frame is not read (camera error)
        print("Error reading frame.")
        break

    cv.imshow('Webcam', frame)

    # Press 'd' to exit
    if cv.waitKey(1) & 0xFF == ord('d'):
        break

# Release resources
capture.release()
cv.destroyAllWindows()
