import cv2 as cv
import numpy as np
# Reading the image
img= cv.imread('images/cat.jpg')
cv.imshow('Cat', img)
# Converting to grayscale
grayimg= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray cat', grayimg)
#converting to hsv
hsvimg= cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hue saturation value', hsvimg)
#converting to lab
labimg=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',labimg)
#converting to rgb
rgbimg=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgbimg)
#converting to hls
hlsimg=cv.cvtColor(img,cv.COLOR_BGR2HLS)
cv.imshow('hUE lightness saturation',hlsimg)
#converting to xyz
xyzimg=cv.cvtColor(img,cv.COLOR_BGR2XYZ)
cv.imshow('x y z',xyzimg)
#displaying the single channels
cv.imshow('blue ',img[:,:,0])
cv.imshow('Green ',img[:,:,1])
cv.imshow('Red ',img[:,:,2])

cv.waitKey(0)