import face_data_collect as fdatcol
import face_train as ftrain
import face_recognition as frec
import csv_write as csvw
import csv

course_id = input("Enter Course Code: ")
mode = input("Enter Mode (1: csv write,2: face collect,3: face train,4: face recognition): ")
if mode == '1':
    csvw.runCSVWrite(course_id)
elif mode == '2':
    fdatcol.runFaceDataCollect(course_id)
elif mode == '3':
    ftrain.runFaceTrain(course_id)
elif mode == '4':
    frec.runFaceRecognition(course_id)
elif mode == '5':
    #for clean up attendence file
    with open('datasets/data/attendance/'+ course_id +'_attendence.csv', mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Student ID', 'Name', 'Attendence Time'])
else:
    print("Mode Not Found")