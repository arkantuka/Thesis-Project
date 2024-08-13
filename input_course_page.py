import tkinter as tk
import main_page as mp

#Go to main page when submit button is clicked
def button_click(course_id):
    window.destroy()
    mp.MainPage(course_id)

window = tk.Tk()
window.resizable(False, False)
window.title('Test Application GUI Window Face Recognition')
window.eval('tk::PlaceWindow . center')

#Enter course label
enter_course_label = tk.Label(window, 
                              text="Enter Your Course ID", 
                              font=("Leelawadee", 50) ,
                              padx=100, pady=10)
enter_course_label.pack()

#Course ID entry
courseID_entry = tk.Entry(window, font=("Leelawadee", 30))
courseID_entry.pack()

#Submit Button 
id_submit_button = tk.Button(window, background='black', foreground='green',
                             text="Submit",
                             font=("Leelawadee", 30, "bold"), 
                             command=lambda: button_click(courseID_entry.get()))
id_submit_button.pack(padx=20, pady=20)

window.mainloop()