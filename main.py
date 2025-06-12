import os
from time import strftime
from tkinter import*
from tkinter import ttk
import tkinter
from tkinter import messagebox

from PIL import Image,ImageTk
from student import StudentManagementSystem
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from developer import Developer
from help import Help


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        # First row images
        img=Image.open(r"C:\Users\Akshi\FirstProject\FacialRecognitionSystem\Images\clgImage.jpg").resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        Label(self.root,image=self.photoimg).place(x=0,y=0,width=500,height=130)

        img1=Image.open(r"C:\Users\Akshi\FirstProject\FacialRecognitionSystem\Images\face_rec.png").resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        Label(self.root,image=self.photoimg1).place(x=500,y=0,width=400,height=130)

        img2=Image.open(r"C:\Users\Akshi\FirstProject\FacialRecognitionSystem\Images\indu.png").resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        Label(self.root,image=self.photoimg2).place(x=900,y=0,width=500,height=130)

        # Background
        img3=Image.open(r"C:\Users\Akshi\FirstProject\FacialRecognitionSystem\Images\bgImage.png").resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=50)

        

        def time():
            string=strftime('%H:%M:%S:%p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_lbl,font=("times new roman",10,"bold"),bg="white",fg="blue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()
            

        # Button configurations
        buttons = [
    ("student.png", "Student Details", 200, 100, self.student_details),
    ("face_detector.png", "Face Detector", 500, 100, self.face_detector),
    ("attendance.png", "Attendance", 800, 100, self.attendance),
    ("help.png", "Help", 1100, 100, self.help),
    ("train.png", "Train Data", 200, 380, self.train_data),
    ("photos.png", "Photos", 500, 380, self.open_photos),
    ("developer.png", "Developer", 800, 380, self.developer),
    ("exit.png", "Exit", 1100, 380, self.exit_app),
]

        self.button_images = []

        for img_file, text, x, y, cmd in buttons:
            image = Image.open(f"C:/Users/Akshi/FirstProject/FacialRecognitionSystem/Images/{img_file}").resize((220,220), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            self.button_images.append(photo)

            btn = Button(bg_img, image=photo, cursor="hand2", command=cmd)
            btn.place(x=x, y=y, width=200, height=200)

            btn_lbl = Button(bg_img, text=text, cursor="hand2", command=cmd,
                        font=("times new roman",15,"bold"), bg="darkblue", fg="white")
            btn_lbl.place(x=x, y=y+200, width=200, height=40)
    
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = StudentManagementSystem(self.new_window)

    def face_detector(self):
        print("Face Detector clicked")
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)

    def attendance(self):
        print("Attendance clicked")
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)


    def help(self):
        print("Help clicked")
        self.new_window = Help(self.root)
        self.app = Developer(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
        print("Train Data clicked")

    def open_photos(self):
        os.startfile("data")  # or another folder if different

    def developer(self):
        print("Developer clicked")
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def exit_app(self):
        self.exit=messagebox.askyesno("Face recognition","DO you want to exit the sysyem")
        if self.exit:
            self.root.destroy()
        else:
            return
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
