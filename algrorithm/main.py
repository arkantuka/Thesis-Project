import face_data_collect as fdatcol
import face_train as ftrain
import face_recognition as frec
import csv_write as csvw

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
else:
    print("Mode Not Found")