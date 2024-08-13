import tkinter as tk
from algrorithm import first_add_csv_data as add_dt
from algrorithm import second_face_data_collect as face_coll
# from algrorithm import fourth_face_recognition as face_rec
import input_course_page as icp

class MainPage():
    
    def createLabel(window,label_name):
        label = tk.Label(window,
                         text=label_name,
                         font=("Leelawadee", 20),
                         padx=100)
        label.pack()
        
    def createButton(window,label_name,command):
        button = tk.Button(window,foreground="blue",background='gray',
                           text=label_name,height=2,width=10,
                           padx=100,
                           font=("Leelawadee", 10),
                           command=command)
        button.pack(pady=5)
        
    def button_click(window,course_id,command):
        window.destroy()
        if(command == 1):
            add_dt.runCSVWrite(course_id)
        elif(command == 2):
            face_coll.chooseStudentIDpopUp(course_id)
        elif(command == 3):
            print("Face Train")
        elif(command == 4):
            print("Face Recognition")
        elif(command == 5):
            icp.FaceRecognitionApp().runMain()
        else:
            print("Error")
        
    def __init__(self, course_id):
        self.course_id = course_id
        
        window = tk.Tk()
        window.resizable(False, False)
        window.title('Test Application GUI Window Face Recognition')
        window.eval('tk::PlaceWindow . center')
        
        choose_active_label = tk.Label(window, 
                              text="Choose Your Active", 
                              font=("Leelawadee", 30) ,
                              padx=100, pady=10)
        choose_active_label.pack()
        
        #Buttons for each page
        #Buttons for add student data page
        MainPage.createLabel(window,"Student Data Collect")
        MainPage.createButton(window,
                              "Student Data Collect",
                              command=lambda: MainPage.button_click(window,self.course_id,1))
        
        MainPage.createLabel(window,"StudentFace Collect")
        MainPage.createButton(window,
                              "Student Face Collect",
                              command=lambda: MainPage.button_click(window,self.course_id,2))
        MainPage.createLabel(window,"Face Train")
        MainPage.createButton(window,
                              "Face Train",
                              command=lambda: MainPage.button_click(window,self.course_id,3))
        #Buttons for face recognition page
        MainPage.createLabel(window,"Face Recognition")
        MainPage.createButton(window,
                              "Face Recognition",
                              command=lambda: MainPage.button_click(window,self.course_id,4))
        
        MainPage.createButton(window,
                              "Back To Input Course ID",
                              command=lambda: MainPage.button_click(window,self.course_id,5))
        
        window.mainloop()