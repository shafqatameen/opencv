import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

#load and read the img
img=cv.imread("images/park.jpg")
cv.imshow('Park',img)

#conver the img into gray
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)



blank=np.zeros(img.shape[:2],dtype="uint8")
mask=cv.rectangle(blank.copy(),(0,0),(img.shape[1]//2,img.shape[0]//2),255,-1)
masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow("masked",masked)

#grayscale histogram
gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])
#histogram of masked image
masked_gray_hist=cv.calcHist([gray],[0],mask,[256],[0,256])


#plot the histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(gray_hist)
plt.xlim([0,256])

#plot the histogram for the masked image
plt.figure()
plt.title("Masked Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(masked_gray_hist)
plt.xlim([0,256])
plt.show()



cv.waitKey(0)