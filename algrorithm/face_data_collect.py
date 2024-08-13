import cv2
import os
import csv

def chooseStudentID(course_id):
    

def getStudentNo(course_id, student_id):
    with open('datasets/data/student_in_course_detail/'+ course_id +'.csv', mode='r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            for item in row:
                if item == student_id:
                    return row[0]

def runFaceDataCollect(course_id):

    print("====== Face Data Collection Started ======")
    video = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    count = 1
    while True:
        ret,frame = video.read()
        print(course_id, count)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.03, 2)
        for (x, y, w, h) in faces:
            count += 1
            faces_folder_path = "datasets/images/"+str(course_id)
            if not os.path.exists(faces_folder_path):
                os.makedirs(faces_folder_path)
            cv2.imwrite(faces_folder_path+"/"+str(student_no)+"."+str(count)+".jpg", gray[y:y+h, x:x+w])
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 5)
            
        cv2.imshow("Face Recognition Test",frame)

        if count > 100:
            break

        key_exit = cv2.waitKey(1)
        if key_exit == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

