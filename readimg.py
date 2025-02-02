import cv2

img=cv2.imread('img/fruits.jpg')
print(img.shape)
cv2.imshow('original image called color image',img)
##cv2.waitKey(4)

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img_gray.shape)
cv2.imshow('gray image called grayscale image',img_gray)
#cv2.waitKey(10)

cv2.imshow('image without blue color',img[:,:,0])
#cv2.waitKey(100000)

cv2.imshow('image without green color',img[:,:,1])
#cv2.waitKey(100000)

cv2.imshow('image without red color',img[:,:,2])
#cv2.waitKey(100000)


