import cv2 as cv
import numpy as np

img = cv.imread('images/park.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

lap_float = cv.Laplacian(gray, cv.CV_64F)
lap_abs = np.absolute(lap_float)
lap_uint8 = np.uint8(lap_abs)

cv.imshow('Laplacian Float64', lap_float / lap_float.max())  # Normalize for display
cv.imshow('Laplacian Absolute', lap_abs / lap_abs.max())      # Normalize for display
cv.imshow('Laplacian uint8', lap_uint8)

cv.waitKey(0)
cv.destroyAllWindows()
