import csv
import os

course_id = input("Enter Course Code: ")
path = 'datasets/data/student_in_course_detail/'

class writeData:

    def getCourseIDs(path):
        course_paths = [os.path.join(path,f) for f in os.listdir(path)]
        course_ids = []
        for course_path in course_paths:
            course_id = os.path.split(course_path)[1].split('.')[0]
            course_ids.append(course_id)
        return course_ids

    def writeData(courseIDs):
        
        if course_id not in courseIDs:
            with open('datasets/data/student_in_course_detail/'+ course_id +'.csv', mode='w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['No','Student ID', 'Name'])
        else :
            with open('datasets/data/student_in_course_detail/'+ course_id +'.csv', mode='a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                student_id = input("Enter Student ID: ")
                name = input("Enter Name: ")
                numline = sum(1 for line in open('datasets/data/student_in_course_detail/'+ course_id +'.csv'))
                writer.writerow([numline, student_id, name])

    course_ids = getCourseIDs(path)
    writeData(course_ids)