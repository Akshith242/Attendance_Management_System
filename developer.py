from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.title("Developer")

        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 30, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1366, height=60)

        img1 = Image.open("Images/developer.png").resize((1366, 650), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=55, width=1366, height=650)

        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=900, y=50, width=1340, height=500)

        f_lbl1 = Label(main_frame, image=self.photoimg1)
        f_lbl1.place(x=300, y=0, width=1, height=650)



if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()