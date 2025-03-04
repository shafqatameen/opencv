import cv2 as cv

img = cv.imread('images/park.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Simple threshold
threshold , thresh = cv.threshold(gray, 150,255,cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

# Inverse threshold
threshold,thresh= cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Inverse Threshold', thresh)


# Adaptive threshold
adp_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,1)
cv.imshow('Adaptive Threshold', adp_thresh)

cv.waitKey(0)
