import cv2
import csv
import os

course_id = input("Enter Course Code: ")
course_id_path = 'datasets/data/student_in_course_detail/'

def getCourseIDs(path):
    course_paths = [os.path.join(path,f) for f in os.listdir(path)]
    course_ids = []
    for course_path in course_paths:
        course_id = os.path.split(course_path)[1].split('.')[0]
        course_ids.append(course_id)
    return course_ids

course_ids = getCourseIDs(course_id_path)

if course_id not in course_ids:
    print("====== Error : Course Not Found ======")
else:
    def face_data_collect():
        student_found = False
        input_id = input("Enter Your Student ID: ")
        with open('datasets/data/student_in_course_detail/'+ course_id +'.csv', mode='r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                for item in row:
                    if item == input_id:
                        student_no = int(row[0])
                        student_found = True
                        break
        if student_found == False:
            print("====== Error : Student Not Found ======")
            return
            # เผื่อใช้
            # numline = sum(1 for line in open('datasets/data/student_in_course_detail/'+ course_id +'.csv'))
            # student_no = numline+1

        video = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        count = 0
        while True:
            ret,frame = video.read()
            print(course_id, student_no, count)

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.03, 5)
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
        print("====== Collecting Samples Complete ======")

    face_data_collect()