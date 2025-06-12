from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.title("Student Management System")

        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 30, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1366, height=60)

        img1 = Image.open("Images/help.png").resize((1366, 650), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=55, width=1366, height=650)

        f_lb = Label(f_lbl,text="Email:akshiths42@gmail.com", font=("times new roman", 30, "bold"), bg="white", fg="blue")
        f_lb.place(x=600, y=400)

        
        
    

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()