# pylint:disable=no-member
import cv2 as cv
import numpy as np
from pathlib import Path

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR = Path("C:/xampp/htdocs/programming/opencv/SECTION_3_Faces/train")
haar_cascade = cv.CascadeClassifier(str(Path("SECTION_3_Faces/haar_face.xml")))

features = []
labels = []

def create_train():
    for person in people:
        path = DIR / person
        label = people.index(person)

        for img_path in path.iterdir():
            img_array = cv.imread(str(img_path))
            
            if img_array is None:
                continue  # Skip unreadable images

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                face_roi = gray[y:y+h, x:x+w]
                print(f"face_roi: {face_roi.shape}")
                features.append(face_roi)
                print(f"features: {len(features)}")
                labels.append(label)
                print(f'Label: {label}, {img_path}')
                

create_train()

print(f"Training complete ✅\nTotal faces: {len(features)}\nTotal labels: {len(labels)}")

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)
face_recognizer.save("SECTION_3_Faces/face_trained.yml")
np.save("SECTION_3_Faces/features.npy", features)
np.save("SECTION_3_Faces/labels.npy", labels)




'''import os 
import cv2 as cv
import numpy as np

people=['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIC=r"C:/xampp/htdocs/programming/opencv\SECTION_3_Faces/train"
p=[]
for i  in os.listdir(r"C:/xampp/htdocs/programming/opencv\SECTION_3_Faces/train"):
    p.append(i)

print(p)


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

'''