import face_data_collect as fdatcol
import face_train as ftrain
import face_recognition as frec
import csv_write as csvw

course_id = input("Enter Course Code: ")
mode = input("Enter Mode (1: face collect,2: face train,3: face recognition,4: csv write): ")
if mode == '1':
    fdatcol.runFaceDataCollect(course_id)
elif mode == '2':
    ftrain.runFaceTrain(course_id)
elif mode == '3':
    frec.runFaceRecognition(course_id)
elif mode == '4':
    csvw.runCSVWrite(course_id)
else:
    print("Mode Not Found")