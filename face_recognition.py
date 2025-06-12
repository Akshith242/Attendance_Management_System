
import os
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
import mysql.connector
from time import strftime
from datetime import datetime



class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1366x768')
        self.root.title("Face Recofnition System")

    # Title Label
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 30, "bold"), bg="darkgrey", fg="blue")
        title_lbl.place(x=0, y=0, width=1366, height=60)

        img_top = Image.open(r"C:\Users\Akshi\FirstProject\FacialRecognitionSystem\Images\face_detector.png")
        img_top = img_top.resize((650, 705), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_label = Label(self.root, image=self.photoimg_top)
        f_label.place(x=0, y=55, width=650, height=705)

        img_bottom = Image.open(r"C:\Users\Akshi\FirstProject\FacialRecognitionSystem\Images\face_rec.png")
        img_bottom = img_bottom.resize((950, 705), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_label1 = Label(self.root, image=self.photoimg_bottom)
        f_label1.place(x=600, y=55, width=950, height=705)

        # button
        btn = Button(f_label1, text="Face Recognition", cursor="hand2", font=("times new roman", 20, "bold"),
                           bg="green", fg="white",command=self.face_recog)
        btn.place(x=450, y=500, width=250, height=60)

# ===========attendance===================================================
    def mark_attendance(self,i,r,df,d):
        with open("akshith.csv","r+",newline="\n") as f:
            myData=f.readlines()
            name_list=[]
            for line in myData:
                entry=line.split(",")
                name_list.append(entry[0])
            if((i not in name_list) and ( r not in name_list) and (df not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{df},{d},{dtstring},{d1},Present")


    # ======FAce Recognition==============================
    def face_recog(self):
        def drwa_boundary(img, classifier, scalefactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scalefactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)

                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))

                connection = mysql.connector.connect(
                    host="localhost", username="root", password="Akshith@242", database="face_recognizer")
                my_cursor = connection.cursor()

                def fetch_value(query):
                    my_cursor.execute(query)
                    result = my_cursor.fetchone()
                    return result[0] if result else "Unknown"

                name = fetch_value(f"SELECT name FROM students WHERE student_id = {id}")
                roll = fetch_value(f"SELECT rollno FROM students WHERE student_id = {id}")
                dep = fetch_value(f"SELECT dep FROM students WHERE student_id = {id}")
                stu_id = fetch_value(f"SELECT student_id FROM students WHERE student_id = {id}")

                if confidence > 77:  # you had >100, which is impossible since confidence is max 100
                    cv2.putText(img, f"Student_ID:{stu_id}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll:{roll}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{dep}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                    self.mark_attendance(stu_id, roll, name, dep)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img,clf,faceCascade):
            coord=drwa_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face recognition",img)
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        






if __name__=="__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()