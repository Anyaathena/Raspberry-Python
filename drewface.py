import cv2

cap = cv2.VideoCapture(0)
filename = 'drew.jpeg'
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
frame = cv2.imread(filename)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 3)
for (x, y, w, h) in faces:
    frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()