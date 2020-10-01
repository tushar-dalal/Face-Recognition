import cv2
import face_recognition
import os

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


EncodingsList = findEncodings(images)

fileClassNames = open("ClassNames.txt", "w")
for i in classnames:
    fileClassNames.writelines(f'{i}\n')

fileEncodings = open("Encodings.txt", "w")
for i in EncodingsList:
    for j in i:
        fileEncodings.writelines(f'{str(j)}\n')
    fileEncodings.writelines("--\n")

print('Finished Encoding')