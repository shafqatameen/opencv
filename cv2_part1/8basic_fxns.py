import cv2 as cv

img=cv.imread('images/park.jpg')
cv.imshow('Park',img)

# 1. Convert to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# 2. Blur the image
blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# 3. Edge Cascade
canny=cv.Canny(blur,125,175)
cv.imshow('Canny Edges',canny)

# 4. Dilating the image
dilated=cv.dilate(canny,(3,3),iterations=1)
cv.imshow('Dilated',dilated)

# 5. Eroding
eroded=cv.erode(dilated,(3,3),iterations=1)
cv.imshow('Eroded',eroded)
cv.waitKey(0)
