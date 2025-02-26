import cv2

# Open the video file (change 'video.mp4' to 0 for webcam)
video_path = "output_video.mp4"  # Change this to your video file or use 0 for a webcam
cap = cv2.VideoCapture(video_path)

# Check if the video file opened correctly
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get video properties
frame_width = int(cap.get(3))  # Width of frames
frame_height = int(cap.get(4))  # Height of frames
fps = int(cap.get(cv2.CAP_PROP_FPS))  # Frames per second

# Define the codec and create VideoWriter object
output_path = "output_video.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 format
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height), isColor=False)

while True:
    ret, frame = cap.read()  # Read a frame
    if not ret:
        break  # Exit loop if no frame is returned

    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Show the frame
    cv2.imshow("Grayscale Video", gray_frame)

    # Write the processed frame to output file
    out.write(gray_frame)

    # Handle playback controls
    key = cv2.waitKey(250) & 0xFF
    if key == ord('q'):  # Press 'q' to quit
        break
    elif key == ord('p'):  # Press 'p' to pause
        cv2.waitKey(-1)  # Wait until any key is pressed to resume

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()
