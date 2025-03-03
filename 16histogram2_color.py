import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('images/cats.jpg')

#masked image
blank=np.zeros(img.shape[:2],dtype="uint8")
mask=cv.rectangle(blank.copy(),(0,0),(img.shape[1]//2,img.shape[0]//2),255,-1)
masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow("masked",masked)

#color histogram for color image
colors=('b','g','r')
for i,col in enumerate(colors):
    hist_color=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist_color,color=col)
    plt.xlim([0,256])    
plt.show()

#color histogram for masked image
colors=('b','g','r')
for i,col in enumerate(colors):
    hist_color=cv.calcHist([masked],[i],None,[256],[0,256])
    plt.plot(hist_color,color=col)
    plt.xlim([0,256])   
plt.show()
