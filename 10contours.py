import cv2 as cv
import numpy as np

# Read the image
img=cv.imread('images/cats.jpg')
cv.imshow('cats',img)
#create blank image
blank=np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank',blank)

# Convert to gray scale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# Blur the image
blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

# Canny edge detection
canny =cv.Canny(blur,125,175)
cv.imshow('canny',canny)

# Thresholding
ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)

#contouurs
contours, hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours) } contours found')

# Draw the contours
cv.drawContours(blank,contours,-1,(90,90,90),1)
cv.imshow('contours drawn',blank)

cv.waitKey(0)