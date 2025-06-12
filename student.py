from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.title("Student Management System")

        # vairiables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_StudentId = StringVar()
        self.var_name = StringVar()
        self.var_division = StringVar()
        self.var_roll_no = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_radio=StringVar()

       

        # Top header images
        img1 = Image.open("Images/student1.png").resize((455, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=455, height=130)

        img2 = Image.open("Images/face_rec.png").resize((455, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=455, y=0, width=455, height=130)

        img3 = Image.open("Images/student2.png").resize((455, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=910, y=0, width=455, height=130)

        # Background
        bg_img = Image.open("Images/bgImage.png").resize((1366, 638), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(bg_img)
        bg_label = Label(self.root, image=self.bg)
        bg_label.place(x=0, y=130, width=1366, height=638)

        # Title
        title_lbl = Label(bg_label, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 30, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1366, height=50)

        # Main Frame
        main_frame = Frame(bg_label, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1340, height=570)

        # Left Label Frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=660, height=550)

        # Image inside left frame
        img_left = Image.open("Images/student.png").resize((650, 100), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=650, height=100)

        # Current Course Frame
        course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Current course information", font=("times new roman", 12, "bold"))
        course_frame.place(x=5, y=105, width=650, height=100)

        # Department
        Label(course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=0, padx=10)
        self.dep_combo = ttk.Combobox(course_frame, font=("times new roman", 12), state="readonly", width=18,textvariable=self.var_dep)
        self.dep_combo["values"] = ("Select Department", "CSE", "ECE", "IT", "ME", "CE")
        self.dep_combo.current(0)
        self.dep_combo.grid(row=0, column=1, padx=2, pady=5, sticky=W)

        # Course
        Label(course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=2, padx=10)
        self.course_combo = ttk.Combobox(course_frame, font=("times new roman", 12), state="readonly", width=18, textvariable=self.var_course)
        self.course_combo["values"] = ("Select Course", "B.Tech", "M.Tech", "MBA")
        self.course_combo.current(0)
        self.course_combo.grid(row=0, column=3, padx=2, pady=5, sticky=W)

        # Year
        Label(course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=0, padx=10)
        self.year_combo = ttk.Combobox(course_frame, font=("times new roman", 12), state="readonly", width=18, textvariable=self.var_year)
        self.year_combo["values"] = ("Select Year", "1st", "2nd", "3rd", "4th")
        self.year_combo.current(0)
        self.year_combo.grid(row=1, column=1, padx=2, pady=5, sticky=W)

        # Semester
        Label(course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=2, padx=10)
        self.semester_combo = ttk.Combobox(course_frame, font=("times new roman", 12), state="readonly", width=18, textvariable=self.var_semester)
        self.semester_combo["values"] = ("Select Semester", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
        self.semester_combo.current(0)
        self.semester_combo.grid(row=1, column=3, padx=2, pady=5, sticky=W)

        # Student Info Frame
        student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        student_frame.place(x=5, y=210, width=650, height=250)

        # Labels and Entries
        fields = [
            ("StudentID:", self.var_StudentId),
            ("Student Name:", self.var_name),
            ("Class Division:", self.var_division),
            ("Roll No:", self.var_roll_no),
            ("Gender:", self.var_gender),
            ("DOB:", self.var_dob),
            ("Email:", self.var_email),
            ("Phone No:", self.var_phone),
            ("Address:", self.var_address),
            ("Teacher Name:", self.var_teacher)
        ]

        positions = [(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2), (3, 0), (3, 2), (4, 0), (4, 2)]

        for (label_text, var), (r, c) in zip(fields, positions):
            Label(student_frame, text=label_text, font=("times new roman", 12), bg="white").grid(row=r, column=c, padx=10, pady=5, sticky=W)
            entry = ttk.Entry(student_frame, width=20, font=("times new roman", 12), textvariable=var)
            entry.grid(row=r, column=c + 1, padx=10, pady=5, sticky=W)
        #radio buttons
        self.var_radio = StringVar()
         # Default value for radio buttons
        radiobtn1 = Radiobutton(student_frame, text="Take Photo Sample", value="Yes", font=("times new roman", 12, "bold"), bg="white",variable=self.var_radio)
        radiobtn1.grid(row=5, column=0, padx=10, pady=5, sticky=W)
    
        radiobtn2 = Radiobutton(student_frame, text="No Photo Sample", value="No", font=("times new roman", 12, "bold"), bg="white", variable=self.var_radio)
        radiobtn2.grid(row=5, column=1, padx=10, pady=5, sticky=W)
        #bbuttons frame
        button_frame = Frame(student_frame, bd=2, bg="white")
        button_frame.place(x=0, y=200, width=640, height=40)

        #savw buton
        save_btn = Button(button_frame, text="Save", font=("times new roman", 12, "bold"), bg="blue", fg="white",command=self.add_data)
        save_btn.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        update_btn = Button(button_frame, text="Update", command=lambda: self.update_data(), font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        delete_btn = Button(button_frame, text="Delete", command=lambda: self.delete_data(), font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        reset_btn = Button(button_frame, text="Reset", command=lambda: self.reset_data(), font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        #take photo sample button
        take_photo_btn = Button(button_frame, text="Take Photo Sample", command=lambda: self.generate_dataset(), font=("times new roman", 12, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=4, padx=10, pady=5, sticky=W)


        # Right Label Frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=680, y=10, width=650, height=550)

        #search system frame
        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=10, width=640, height=70)
        #search by
        search_by_label = Label(search_frame, text="Search By:", font=("times new roman", 12, "bold"), bg="purple")
        search_by_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        self.search_by_combo = ttk.Combobox(search_frame, font=("times new roman", 12), state="readonly", width=15)
        self.search_by_combo["values"] = ("Select", "StudentID", "Roll No", "Phone No")
        self.search_by_combo.current(0)
        self.search_by_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        self.search_entry = ttk.Entry(search_frame, width=20, font=("times new roman", 12))
        self.search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        #search button
        search_btn = Button(search_frame, text="Search", command=lambda: self.search_data(), font=("times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        #show all button
        show_all_btn = Button(search_frame, text="Show All", command=lambda: self.show_all_data(), font=("times new roman", 12, "bold"), bg="blue", fg="white")
        show_all_btn.grid(row=0, column=3, padx=10, pady=5, sticky=W)
        #table frame
        table_frame = Frame(right_frame, bd=2, bg="white")
        table_frame.place(x=5, y=90, width=640, height=450)
        #scroll bars
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, columns=("Department","Course","Year","Semester","StudentID", "Name", "Division", "Roll No", "Gender", "DOB", "Email", "Phone", "Address", "Teacher"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.pack(fill=BOTH, expand=1)


        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("StudentID", text="StudentID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Division", text="Division")
        self.student_table.heading("Roll No", text="Roll No")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Phone", text="Phone")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Teacher", text="Teacher")

        
        self.student_table["show"] = "headings"
        self.student_table.column("Department", width=50)
        self.student_table.column("Course", width=50)
        self.student_table.column("Year", width=50)
        self.student_table.column("Semester", width=50)

        self.student_table.column("StudentID", width=50)
        self.student_table.column("Name", width=50)
        self.student_table.column("Division", width=50)
        self.student_table.column("Roll No", width=50)
        self.student_table.column("Gender", width=50)
        self.student_table.column("DOB", width=50)
        self.student_table.column("Email", width=50)
        self.student_table.column("Phone", width=50)
        self.student_table.column("Address", width=50)
        self.student_table.column("Teacher", width=50)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.student_table.pack(fill=BOTH, expand=1)
        self.show_all_data()
      
        # Dummy methods for buttons (implement as needed)

  


    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "" or self.var_year.get() == "" or self.var_semester.get() == "":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                connection= mysql.connector.connect(host="localhost",username="root",password="Akshith@242",database="face_recognizer")
                my_cursor = connection.cursor()
                my_cursor.execute("""
                INSERT INTO students (
                    dep, course, year, semester, student_id, name, division,
                    rollno, gender, dob, email, phone, address, teacher, radio
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_StudentId.get(),
                self.var_name.get(),
                self.var_division.get(),
                self.var_roll_no.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_radio.get()
            ))
                connection.commit()
                self.show_all_data()
                connection.close()
                messagebox.showinfo("Success", "Student details added successfully", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.root)    
  
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "" or self.var_year.get() == "" or self.var_semester.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
                if update:
                    connection = mysql.connector.connect(host="localhost", username="root", password="Akshith@242", database="face_recognizer")
                    my_cursor = connection.cursor()
                    my_cursor.execute("""
                        UPDATE students SET
                            dep=%s, course=%s, year=%s, semester=%s, name=%s,
                            division=%s, rollno=%s,gender=%s, dob=%s,
                            email=%s, phone=%s, address=%s, teacher=%s, radio=%s where student_id=%s""",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_name.get(),
                        self.var_division.get(),
                        self.var_roll_no.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio.get()
                        ,self.var_StudentId.get()

                            ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "Student details updated successfully", parent=self.root)
                connection.commit()
                self.show_all_data()
                connection.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.root)

        

    def delete_data(self):
        if self.var_StudentId.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this student details?", parent=self.root)
                if delete:
                    connection = mysql.connector.connect(host="localhost", username="root", password="Akshith@242", database="face_recognizer")
                    my_cursor = connection.cursor()
                    my_cursor.execute("DELETE FROM students WHERE student_id=%s", (self.var_StudentId.get(),))
                    connection.commit()
                    self.show_all_data()
                    connection.close()
                    messagebox.showinfo("Success", "Student details deleted successfully", parent=self.root)
                else:
                    if not delete:
                        return
                
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.root)
        

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_StudentId.set("")
        self.var_name.set("")
        self.var_division.set("")
        self.var_roll_no.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio.set("")

     # Generetae data set Take photo sample
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "" or self.var_year.get() == "" or self.var_semester.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        try:
            student_id = self.var_StudentId.get()
            if not student_id.isdigit():
                messagebox.showerror("Error", "Student ID must be numeric", parent=self.root)
                return

            conn = mysql.connector.connect(
                host="localhost", username="root", password="Akshith@242", database="face_recognizer")
            cursor = conn.cursor()

            # Update student details
            cursor.execute("""
                UPDATE students SET
                    dep=%s, course=%s, year=%s, semester=%s, name=%s,
                    division=%s, rollno=%s, gender=%s, dob=%s,
                    email=%s, phone=%s, address=%s, teacher=%s, radio=%s
                WHERE student_id=%s
            """, (
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_name.get(),
                self.var_division.get(),
                self.var_roll_no.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_radio.get(),
                student_id
            ))

            conn.commit()
            self.show_all_data()
            self.reset_data()
            conn.close()

            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            if face_classifier.empty():
                messagebox.showerror("Error", "Failed to load Haar cascade.")
                return

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    return gray[y:y+h, x:x+w]
                return None

            cap = cv2.VideoCapture(0)
            img_id = 0

            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                face = face_cropped(frame)
                if face is not None:
                    img_id += 1
                    face_resized = cv2.resize(face, (450, 450))
                    file_path = f"data/user.{student_id}.{img_id}.jpg"
                    cv2.imwrite(file_path, face_resized)

                    cv2.putText(face_resized, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    cv2.imshow("Cropped Face", face_resized)

                if cv2.waitKey(1) == ord('q') or img_id == 100:
                    break

            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Generating dataset completed successfully", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", f"Due to: {str(e)}", parent=self.root)



                

      



    def take_photo_sample(self):
        pass

    def search_data(self):
        pass
# This function will fetch all the data from the database and display it in the table
    def show_all_data(self):
        conn= mysql.connector.connect(host="localhost", username="root", password="Akshith@242", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM students")
        data= my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in data:
                self.student_table.insert("", END, values=row)
            conn.commit()
        conn.close()
        pass
    #as the user clicks on the table, the data will be fetched and displayed in the entry fields
    def get_cursor(self,event=""):
        cursor_focus= self.student_table.focus()
        content= self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_StudentId.set(data[4])
        self.var_name.set(data[5])
        self.var_division.set(data[6])
        self.var_roll_no.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio.set(data[14])
if __name__ == "__main__":
    root = Tk()
    obj = StudentManagementSystem(root)
    root.mainloop()



