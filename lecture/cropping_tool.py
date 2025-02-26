import cv2
import numpy as np

# Global variables
cropping = False  # Flag to indicate cropping state
start_x, start_y, end_x, end_y = -1, -1, -1, -1
image = cv2.imread("img/fruits.jpg")  # Load your image here
clone = image.copy()  # Keep a copy of the original image

# Mouse callback function
def crop_rectangle(event, x, y, flags, param):
    global start_x, start_y, end_x, end_y, cropping, image
    
    if event == cv2.EVENT_LBUTTONDOWN:  # Mouse button pressed
        start_x, start_y = x, y
        cropping = True

    elif event == cv2.EVENT_MOUSEMOVE:  # Mouse movement
        if cropping:
            temp_image = clone.copy()  # Use a copy to avoid overwriting
            cv2.rectangle(temp_image, (start_x, start_y), (x, y), (0, 255, 0), 2)
            cv2.imshow("Image", temp_image)

    elif event == cv2.EVENT_LBUTTONUP:  # Mouse button released
        end_x, end_y = x, y
        cropping = False
        cv2.rectangle(image, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)
        cv2.imshow("Image", image)

        # Ensure coordinates are correct
        if start_x != end_x and start_y != end_y:
            cropped_image = clone[start_y:end_y, start_x:end_x]  # Extract ROI
            cv2.imshow("Cropped Image", cropped_image)
            cv2.imwrite("cropped_output.jpg", cropped_image)  # Save cropped image

# Set up the OpenCV window
cv2.imshow("Image", image)
cv2.setMouseCallback("Image", crop_rectangle)

# Keep the window open until 'q' is pressed
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
