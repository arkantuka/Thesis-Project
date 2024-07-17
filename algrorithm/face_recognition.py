import cv2
import csv

course_id = input("Enter Course Code: ")

def getStudentName():
    name_list = []
    with open('datasets/data/student_in_course_detail/'+ course_id +'.csv', mode='r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            name_list.append(row[2])
    return name_list

all_name = getStudentName()
print(all_name)

video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read("TrainingData.yml")

while True:
    ret,frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.03, 2)
    for (x, y, w, h) in faces:
        serial, conf = face_recognizer.predict(gray[y:y+h, x:x+w])
        if(conf > 50 & serial):
            print(serial)
            cv2.putText(frame, all_name[serial]+" "+str(conf), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)
        else:
            cv2.putText(frame, "Unknown", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 5)
        
    cv2.imshow("Face Recognition Test",frame)

    key_exit = cv2.waitKey(1)
    if key_exit == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
print("====== Face Recognition Samples Complete ======")