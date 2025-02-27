import cv2 as cv
import numpy as np

#load and read the image
img=cv.imread("images/park.jpg")
cv.imshow('Park',img)

# transformation functions
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dim=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dim)

'''x: Moves the image horizontally.
+x → Shifts right.
-x → Shifts left.
   y: Moves the image vertically.
+y → Shifts down.
-y → Shifts up.           '''

translated=translate(img,-100,-100)
cv.imshow("window",translated)

# Rotation
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint is None:
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dim=(width,height)
    return cv.warpAffine(img,rotMat,dim)

rotated=rotate(img,180)
cv.imshow('rotated image',rotated)

# Resizing
resized=cv.resize(img,(1000,1000),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#flip
'''flipCode: Defines the flipping direction:
0  → Flip vertically (upside down).
1  → Flip horizontally (mirror image).
-1 → Flip both vertically & horizontally (180° rotation).'''
fliped=cv.flip(img,-1)
cv.imshow('Fliped',fliped)

#cropping
cropped=img[0:img.shape[0]//2,0:img.shape[1]//2]
cv.imshow('Cropped',cropped)


cv.waitKey(0)
