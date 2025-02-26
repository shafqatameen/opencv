import cv2 as cv
import numpy as np

# Create the image using numpy
black_img = np.zeros((500,500),dtype=np.uint8)
white_img = np.ones((500,500),dtype=np.uint8)*255

#show the image on window
cv.imshow('Black Image',black_img)
cv.imshow('White Image',white_img)
cv.waitKey(0)