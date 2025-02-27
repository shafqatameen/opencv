import cv2 as cv
import matplotlib.pyplot as plt
from pathlib import Path as path
image=sorted(path("images").glob('*'))
print(image)
img=cv.imread(image[3])
cv.imshow("img", img)
cv.waitKey(0)