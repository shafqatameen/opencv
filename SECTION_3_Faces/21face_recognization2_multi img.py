from pathlib import Path
import numpy as np
import cv2 as cv

# Load Haar cascade
haar_cascade = cv.CascadeClassifier(str(Path('SECTION_3_Faces/haar_face.xml')))

# People names based on your training labels (same order!)
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

# Load trained face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read(str(Path('SECTION_3_Faces/face_trained.yml')))

# Set the path to validation images
val_dir = Path('SECTION_3_Faces/val')

# Traverse all JPG images in all subfolders of val_dir
for img_path in val_dir.glob('*/*.jpg'):
    img = cv.imread(str(img_path))
    if img is None:
        print(f"[!] Could not load image: {img_path}")
        continue

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

    print(f"\n📷 Image: {img_path.name}")
    for (x, y, w, h) in faces_rect:
        faces_roi = gray[y:y + h, x:x + w]

        label, confidence = face_recognizer.predict(faces_roi)
        print(f'    → Predicted: {people[label]} | Confidence: {round(confidence, 2)}')

        cv.putText(img, people[label], (x, y - 10), cv.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv.imshow('Detected Face', img)
    cv.waitKey(500)  # Show each image for 500ms
    cv.destroyAllWindows()