import cv2 as cv
import matplotlib.pyplot as plt
from pathlib import Path as path
#arranging the file using pathlib
image=sorted(path("images").glob('*'))
print(image)
#default bgr img
img=cv.imread(image[3])
cv.imshow("img->bgr", img)
#converted into rgb img
img_rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("img->rbg", img_rgb)

#Default img rgb using bgr
plt.imshow(img)
plt.title("img->bgr")
plt.show()
#using defailt img rgb
plt.imshow(img_rgb)
plt.title("img->rbg")
plt.show()

cv.waitKey(0)
if cv.waitKey(0)& 0xFF ==ord('q'):
    cv.destroyAllWindows()