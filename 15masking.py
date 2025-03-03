import cv2 as cv
import numpy as np

#load and read the image
img=cv.imread("images/park.jpg")
cv.imshow('Park',img)

#BLANK
blank=np.zeros(img.shape[:2],dtype="uint8")
cv.imshow("Blank",blank)
mask=cv.rectangle(blank.copy(),(0,0),(img.shape[1]//2,img.shape[0]//2),255,-1)
cv.imshow("mask",mask)

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow("masked",masked)
cv.waitKey(0)