import cv2
import numpy as np

names = ['Anya']
model = cv2.face.LBPHFaceRecognizer_create()
model.read('faces.data')
print('load training data done')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cv2.namedWindow('video', cv2.WINDOW_NORMAL)
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 3)
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        face_img = cv2.resize(gray[y: y + h, x: x + w], (400, 400))
        try:
            params = model.predict(face_img)
            print('label: {}, confidence: {}'.format(params[0], params[1]))
            if params[1] < 50:
                cv2.putText(frame, names[params[0]], (x, y - 10),font, 1, (255,255,0), 3, cv2.LINE_AA)
        except:
            continue
    cv2.imshow('video', frame)
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        break
