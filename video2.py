import cv2

# Open webcam (0 for default camera)
cap = cv2.VideoCapture(0)

# Get video properties
frame_width = int(cap.get(3))  # Width
frame_height = int(cap.get(4))  # Height
fps = 30  # Frame rate (adjust as needed)

# Define codec and create VideoWriter object
output_path = "captured_video.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 format
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# Check if webcam is opened
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press 'q' to stop recording...")

while True:
    ret, frame = cap.read()  # Read a frame from the webcam
    if not ret:
        break  # Exit loop if no frame is captured

    # Display the video feed
    cv2.imshow("Webcam Live Feed", frame)

    # Save the frame to the output file
    out.write(frame)

    # Press 'q' to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
out.release()
cv2.destroyAllWindows()
print("Video saved as 'captured_video.mp4'")
