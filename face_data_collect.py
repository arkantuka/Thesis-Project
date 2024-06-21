import cv2

video = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
id = input("Enter Your ID: ")
count = 0

while True:
    ret,frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.05, 5)
    for (x, y, w, h) in faces:
        count += 1
        cv2.imwrite("datasets/User."+str(id)+"."+str(count)+".jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 5)
        
    cv2.imshow("Face Recognition Test",frame)

    if count > 100:
        break

    key_exit = cv2.waitKey(1)
    if key_exit == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
print("====== Collecting Samples Complete ======")