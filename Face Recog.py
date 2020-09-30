import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'Known Images'
images = []
classnames = []
myList = os.listdir(path)
for cl in myList:
    currImg = cv2.imread(f'{path}/{cl}')
    images.append(currImg)
    classnames.append(os.path.splitext(cl)[0])
print('Starting Encoding')


def findEncodings(images):
    encodings = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoding = face_recognition.face_encodings(img)[0]
        encodings.append(encoding)
    return encodings


def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            t = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{t}')


EncodingsList = findEncodings(images)
print('Finished Encoding')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    faceLocCurrFace = face_recognition.face_locations(imgS)
    encodeCurrFace = face_recognition.face_encodings(imgS)

    for encodeFace, faceLoc in zip(encodeCurrFace, faceLocCurrFace):
        matches = face_recognition.compare_faces(EncodingsList, encodeFace)
        faceDis = face_recognition.face_distance(EncodingsList, encodeFace)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classnames[matchIndex]
            y1, x2, y2, x1 = faceLoc
            cv2.rectangle(img, (4*x1, 4*y1), (4*x2, 4*y2), (0, 0, 255), 2)
            cv2.putText(img, name, (4*x1, 4*y1), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            markAttendance(name)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
