import cv2 as  cv
import numpy as np
from pathlib import Path

#path of images
image=sorted(Path("images").glob('*'))[2]

#load img
img=cv.imread(str(image))
#show img
cv.imshow("bgr img",img)

b , g , r=cv.split(img)
stack_rgb=np.hstack((b,g,r))
cv.imshow("stack of img",stack_rgb,)

#shape of img and  b g r imgs
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#merge 
merged=cv.merge([b,g,r])
cv.imshow("merged img", merged)

blank=np.zeros(img.shape[:2],dtype="uint8")
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

stack_colors=np.hstack((blue,green,red))
cv.imshow("stack of colors",stack_colors)

cv.waitKey(0)
if cv.waitkey(0) &0xFF==ord('q'):
    cv.destroyAllWindows