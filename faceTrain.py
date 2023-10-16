import os
import cv2 as cv
import numpy as np

DIR = "/Users/luksuz/Desktop/Github Portfolio/Person detector/trainingData"
people = [i for i in os.listdir(DIR) if i != ".DS_Store"]
print(people)
haar_cascade = cv.CascadeClassifier("haar_face.xml")

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        print(path)


        for img in os.listdir(path):
            if not img.endswith(('.png', '.jpg', '.jpeg')):
                continue
            img_path = os.path.join(path, img)
            print(img_path)

            img = cv.imread(img_path)
            if img is None:
                print(f"Error: Failed to load image at {img_path}")
                
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, 1.2, 6)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print("TRAINING done----------------")
features = np.array(features, dtype="object")
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features, labels)

face_recognizer.save("face_trained.yml")
np.save("features.npy", features)
np.save("labels.npy", labels)


print(f"Lenth of the features is {len(features)}")
print(f"Lenth of the labels is {len(labels)}")