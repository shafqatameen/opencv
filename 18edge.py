import cv2 as cv
import numpy as np

img=cv.imread('images/park.jpg')
cv.imshow('Park',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#laplacian edge detection
lap=cv.Laplacian(gray,cv.CV_64F)
abs_lap=np.absolute(lap)
lap_uint8=np.uint8(abs_lap)
#all_lap=np.hstack((lap_uint8,lap,abs_lap))#needs all in same data type
cv.imshow('Laplacian',lap_uint8)


#sobel edge detection
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel=cv.bitwise_and(sobelx,sobely)
combined=np.hstack((combined_sobel,sobelx,sobely))
cv.imshow('Sobel',combined)

#canny edge detection
canny = cv.Canny(gray,125,175)
cv.imshow('Canny',canny)

cv.waitKey(0)