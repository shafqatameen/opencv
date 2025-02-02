import cv2
import numpy as np

img=cv2.imread('img/fruits.jpg')
#img=np.zeros((500,500,3))

def draw(event,x,y,flags,params):
    if event==1:
        cv2.circle(img,center=(x,y),radius=10,color=(255,0,0),thickness=-1)
'''    print(event)
    if event==0:
        print('mouse moved')
    if event==1:
        print('left button clicked')
    if event==2:
        print('right button clicked')
    if event==3:
        print('middle button clicked')
    if event==4:
        print('left button clicked released')
    if event==5:
        print('right button clicked released')
    if event==6:
        print('middle button clicked released')
    '''


cv2.namedWindow(winname="window")
cv2.setMouseCallback('window',draw)

while True:
    cv2.imshow('window',img)
    if (cv2.waitKey(1) & 0xFF)==ord('x'):
        break

cv2.destroyAllWindows()




