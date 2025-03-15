import cv2 as cv
#load and read the image
img=cv.imread("images/group2.jpg")
cv.imshow("group2",img)
#conver into gray
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray_img)
#haar cascade
haar_cascade=cv.CascadeClassifier("SECTION_3_Faces/haar_face.xml")

#faces_rect=haar_cascade.detectMultiScale(gray_img,scaleFactor=1.1,minNeighbors=4)
faces_rect=haar_cascade.detectMultiScale(gray_img,1.1,4)
#dectect the face
for x,y,w,h in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
cv.imshow("face",img)
print(f'number of faces found={len(faces_rect)}')
cv.waitKey(0)