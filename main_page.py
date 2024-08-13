import tkinter as tk
from algrorithm import add_csv_data as add_dt

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
        
        MainPage.createLabel(window,"Face Data Collect")
        MainPage.createButton(window,"Face Data Collect",lambda: MainPage.createLabel(window,"Face Data Collect"))
        MainPage.createLabel(window,"Face Train")
        MainPage.createButton(window,"Face Train",lambda: MainPage.createLabel(window,"Face Train"))
        MainPage.createLabel(window,"Face Recognition")
        MainPage.createButton(window,"Face Recognition",lambda: MainPage.createLabel(window,"Face Recognition"))
        
        window.mainloop()