import cv2 as cv

img= cv.imread("images/cat.jpg")

cv.imshow('window ka naam cat image',img)
cv.waitKey(0)
cv.destroyAllWindows()

#reading an img greater than the screen size
large_img=cv.imread("images/cat_large.jpg")
cv.imshow('it a large image',large_img)
cv.waitKey(0)

