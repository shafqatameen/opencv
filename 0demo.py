import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv.imread("images/cat.jpg")  # Replace with your image path

# Convert to different color spaces
hsv= cv.cvtColor(img, cv.COLOR_BGR2HSV)
lab= cv.cvtColor(img, cv.COLOR_BGR2LAB)
hls= cv.cvtColor(img, cv.COLOR_BGR2HLS)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # Single channel

'''# Convert images to RGB for Matplotlib
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
hsv_rgb = cv.cvtColor(hsv_img, cv.COLOR_HSV2RGB)
lab_rgb = cv.cvtColor(lab_img, cv.COLOR_LAB2RGB)
hls_rgb = cv.cvtColor(hls_img, cv.COLOR_HLS2RGB)'''

# Convert grayscale to 3-channel for display consistency
gray_img_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2RGB)

# Display each image in a separate Matplotlib window
plt.figure("Original Image")
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")

plt.figure("Grayscale Image")
plt.imshow(gray)
plt.title("Grayscale Image")
plt.axis("off")

plt.figure("HSV Image")
plt.imshow(hsv)
plt.title("HSV Image")
plt.axis("off")

plt.figure("LAB Image")
plt.imshow(lab)
plt.title("LAB Image")
plt.axis("off")

plt.figure("HLS Image")
plt.imshow(hls)
plt.title("HLS Image")
plt.axis("off")

plt.show()
