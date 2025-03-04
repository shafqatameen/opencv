import cv2 as cv
import matplotlib.pyplot as plt
from pathlib import Path as path
import numpy as np

#arranging the file using pathlib
image=sorted(path("images").glob('*'))
print(image)
#default bgr img
img=cv.imread(image[3])
#cv.imshow("img->bgr", img)
#converted into rgb img
img_rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
#cv.imshow("img->rbg", img_rgb)

cmbined_img=np.hstack((img_rgb,img))
cv.imshow("stack of img: img_rgb,img", cmbined_img)

#ushing stack display hsv, gray,lab,hls
hsv_img=cv.cvtColor(img,cv.COLOR_BGR2HSV)
lab_img=cv.cvtColor(img,cv.COLOR_BGR2LAB)
hls_img=cv.cvtColor(img,cv.COLOR_BGR2HLS)

stack_img=np.hstack((hsv_img,lab_img,hls_img))

cv.imshow("stack of imgs(cv)", stack_img)

# Display each image in a separate Matplotlib window
#using hstack in matplotlib for img_rgb and img_bgr
plt.figure("stack of img : img_rgb,img")
plt.imshow(cmbined_img)
plt.title("stack of img : img_rgb,img")


#using hstack in matplotlib for hsv,gray,lab,hls
plt.figure("stack of imgs(plt)")
plt.imshow(stack_img)               #need image in rgb only(plt )
plt.title("stack of imgs(plt)")
plt.show()

cv.waitKey(0)
if cv.waitKey(0)& 0xFF ==ord('q'):
    cv.destroyAllWindows()

