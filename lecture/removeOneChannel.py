import cv2
#load iimage
img=cv2.imread('img/fruits.jpg')
print(img.shape)

'''#show image
cv2.imshow('COLOR IMAGE',img)
cv2.waitKey(0)'''

#remove the channel
img[:,:,0]=0                 #remove blue channel
cv2.imshow('IMAGE WITHOUT BLUE CHANNEL',img)
cv2.waitKey(0)

img[:,:,1]=0
cv2.imshow('IMAGE WITHOUT GREEN CHANNEL',img)
cv2.waitKey(0)

img[:,:,2]=0
cv2.imshow('IMAGE WITHOUT RED CHANNEL',img)
cv2.waitKey(0)

