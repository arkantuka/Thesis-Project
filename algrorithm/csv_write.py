import csv
import os

def getCourseIDs(path):
    course_paths = [os.path.join(path,f) for f in os.listdir(path)]
    course_ids = []
    for course_path in course_paths:
        course_id = os.path.split(course_path)[1].split('.')[0]
        course_ids.append(course_id)
    return course_ids

def checkStudentID(course_id, student_id):
    with open('datasets/data/student_in_course_detail/'+ course_id +'.csv', mode='r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row[1] == student_id:
                return True
    return False

def writeData(courseIDs, course_id):
    if course_id not in courseIDs:
        print("====== Course Not Found : Create New Course ======")
        with open('datasets/data/student_in_course_detail/'+ course_id +'.csv', mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            writer.writerow(['No','Student ID', 'Name'])
            writer.writerow([1, student_id, name])
            print("====== Write Complete ======")
        with open('datasets/data/attendance/'+ course_id +'_attendence.csv', mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Student ID', 'Name', 'Attendence Time'])
    else :
        print("====== Course Found ======")
        with open('datasets/data/student_in_course_detail/'+ course_id +'.csv', mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            numline = sum(1 for line in open('datasets/data/student_in_course_detail/'+ course_id +'.csv'))
            if checkStudentID(course_id, student_id) == False:
                writer.writerow([numline+1, student_id, name])
                print("====== Write Complete ======")
            else:
                print("====== Error : Student ID Already Exists ======")

def runCSVWrite(course_id):
    path = 'datasets/data/student_in_course_detail/'
    course_ids = getCourseIDs(path)
    writeData(course_ids, course_id)
    add_more = input("Do you want to add more data? (y/n): ")
    if add_more == 'y':
        runCSVWrite(course_id)
    else:
        print("====== CSV Write Complete ======")
