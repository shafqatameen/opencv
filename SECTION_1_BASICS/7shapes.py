import cv2 as cv
import numpy as np

# Create the image using numpy
blank=np.zeros((500,500,3),dtype="uint8")
cv.imshow('Blank Image',blank)

# 1. Paint the image a certain color
blank[0:500,0:250]=100,25,10
cv.imshow("green",blank)

#draw the rectangle
cv.rectangle(blank,pt1=(0,0),pt2=(250,250),color=(0,0,200),thickness=-1)
cv.imshow("Rectangle",blank)

#draw the circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),100,(200,0,220),thickness=-1)
cv.imshow("Circle",blank)

#draw the text
cv.putText(blank,"hello bhai",(0,int(0.75*blank.shape[0])),cv.FONT_HERSHEY_TRIPLEX,2,(20,255,0),1)
cv.imshow("Text",blank)

#draw the line
cv.line(blank,(0,0),(500,500),(255,255,255),3)
cv.imshow("Line",blank)
cv.waitKey(0)