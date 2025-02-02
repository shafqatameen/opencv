import cv2
import numpy as np

# Load the image
img = cv2.imread('img/fruits.jpg')

# Check if the image is loaded correctly
if img is None:
    print("Error: Image not found or path is incorrect.")
    exit()

# Resize the image to a manageable size (e.g., 600x400)
scale_percent = 50  # Reduce size by 50%
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

# Remove blue channel
img_without_blue = img.copy()
img_without_blue[:, :, 0] = 0

# Remove green channel
img_without_green = img.copy()
img_without_green[:, :, 1] = 0

# Remove red channel
img_without_red = img.copy()
img_without_red[:, :, 2] = 0

# Stack images horizontally
new_img = np.hstack((img_without_blue, img_without_green, img_without_red))

# Show the final stacked image
cv2.imshow("Single Channel Removed", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()





'''import cv2
import numpy as np


# Load the image
img = cv2.imread('img/fruits.jpg')

# Remove blue channel
img_without_blue = img.copy()
img_without_blue[:, :, 0] = 0
cv2.imshow('IMAGE WITHOUT BLUE CHANNEL', img_without_blue)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Remove green channel
img_without_green = img.copy()
img_without_green[:, :, 1] = 0
cv2.imshow('IMAGE WITHOUT GREEN CHANNEL', img_without_green)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Remove red channel
img_without_red = img.copy()
img_without_red[:, :, 2] = 0
cv2.imshow('IMAGE WITHOUT RED CHANNEL', img_without_red)
cv2.waitKey(0)
cv2.destroyAllWindows()

new_img=np.hstack((img_without_blue,img_without_green,img_without_red))
cv2.imshow("single channel removed",new_img)
cv2.waitKey(0)'''