import cv2 as cv
import numpy as np

#load img
image=cv.imread("images/cats.jpg")
cv.imshow("cat",image)
img=cv.resize(image,(300,300))
cv.imshow("resized cat",img)
#average blur
img_blur=cv.blur(img,(3,3))
cv.imshow("blur",img_blur)

#Gaussian blur
img_gauss_blur=cv.GaussianBlur(img,(3,3),0)
cv.imshow("Gaussian blur",img_gauss_blur)

#median blur
img_median=cv.medianBlur(img,3)
cv.imshow("median blur",img_median)

#bilateral blur
img_bilateral=cv.bilateralFilter(img,3,75,75)
cv.imshow("bilateral blur",img_bilateral)

#hstack
stacked=np.hstack((img,img_blur,img_gauss_blur,img_median,img_bilateral))
cv.imshow("stacked (img,img_blur,img_gauss_blur,img_median,img_bilateral)",stacked)

cv.waitKey(0)