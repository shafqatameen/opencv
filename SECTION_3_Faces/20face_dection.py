import os 
import cv2 as cv
import numpy as np

people=['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIC=r"C:/xampp/htdocs/programming/opencv\SECTION_3_Faces/train"
'''p=[]
for i  in os.listdir(r"C:/xampp/htdocs/programming/opencv\SECTION_3_Faces/train"):
    p.append(i)

print(p)'''


features=[]
labels=[]
haar_cascade=cv.CascadeClassifier("SECTION_3_Faces/haar_face.xml")

def create_train():
    for person in people:
        path=os.path.join(DIC,person)
        label=people.index(person)  
        for img in os.listdir(path):
            img_path=os.path.join(path,img)
            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            faces_rect=haar_cascade.detectMultiScale(gray,1.1,1)
            for (x,y,w,h) in faces_rect:
                faces_roi=gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()

print(f'length of features={len(features)}')
print(f'length of labels={len(labels)}')

features=np.array(features,dtype="object")
labels=np.array(labels)

face_recognizer=cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features,labels)

face_recognizer.write('train.yml')

print("training done")
#save labels and features
np.save('features.npy',features)
np.save('labels.npy',labels)

