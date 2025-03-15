import os 
import cv2 as cv
import numpy as np

p=[]
for i  in os.listdir(r"C:/xampp/htdocs/programming/opencv\SECTION_3_Faces/train"):
    p.append(i)
    
print(p)