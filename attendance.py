from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import csv
from tkinter import filedialog
my_data=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.title(" Attendance System")
        # ==========vairiables==============
        self.var_attend_id = StringVar()
        self.var_name = StringVar()
        self.var_date = StringVar()
        self.var_department = StringVar()
        self.var_time = StringVar()
        self.var_roll = StringVar()
        self.var_attendance_status = StringVar()

        img1 = Image.open("Images/attend.jpg").resize((750, 201), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=750, height=201)

        img2 = Image.open("Images/attend2.png").resize((600, 201), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=751, y=0, width=600, height=201)

        bg_img = Image.open("Images/attend3.png").resize((1366, 638), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(bg_img)
        bg_label = Label(self.root, image=self.bg)
        bg_label.place(x=0, y=220, width=1366, height=500)
        
        # Title
        title_lbl = Label(bg_label, text="ATTENDNACE MANAGEMENT SYSTEM", font=("times new roman", 30, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1366, height=50)
        
        # Main Frame
        main_frame = Frame(bg_label, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1340, height=500)
         # Left Label Frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=660, height=500)
         # Image inside left frame
        img_left = Image.open("Images/student.png").resize((650, 100), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=650, height=100)

        left_main_frame = Frame(left_frame,relief=RIDGE, bd=2, bg="white")
        left_main_frame.place(x=20, y=135, width=660, height=300)

        # Label entries
        attendance_id=Label(left_main_frame,text="AttendanceId:",font=("times new roman", 12,"bold"))
        attendance_id.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        attendance_id_entry = ttk.Entry(left_main_frame, width=20, font=("times new roman", 12, "bold"), textvariable=self.var_attend_id)
        attendance_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        name_label = Label(left_main_frame, text="Name:", font=("times new roman", 12, "bold"))
        name_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        name_entry = ttk.Entry(left_main_frame, width=20, font=("times new roman", 12, "bold"),textvariable=self.var_name)
        name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        date_label = Label(left_main_frame, text="Date:", font=("times new roman", 12, "bold"))
        date_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        date_entry = ttk.Entry(left_main_frame, width=20, font=("times new roman", 12, "bold"),textvariable=self.var_date)
        date_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        department_label = Label(left_main_frame, text="Department:", font=("times new roman", 12, "bold"))
        department_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        department_entry = ttk.Entry(left_main_frame, width=20, font=("times new roman", 12, "bold"),textvariable=self.var_department)
        department_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        time_label = Label(left_main_frame, text="Time:", font=("times new roman", 12, "bold"))
        time_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)
        time_entry = ttk.Entry(left_main_frame, width=20, font=("times new roman", 12, "bold"),textvariable=self.var_time)
        time_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        roll_label = Label(left_main_frame, text="Roll:", font=("times new roman", 12, "bold"))
        roll_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)
        roll_entry = ttk.Entry(left_main_frame, width=20, font=("times new roman", 12, "bold"),textvariable=self.var_roll)
        roll_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        self.status_label = Label(left_main_frame, text="Attendance Status:", font=("times new roman", 12, "bold"))
        self.status_label.grid(row=2, column=2, padx=10, pady=10, sticky=W)
        self.status_combo = ttk.Combobox(left_main_frame, font=("times new roman", 12, "bold"), width=18, state="readonly",textvariable=self.var_attendance_status)
        self.status_combo["values"] = ("Status","Present", "Absent")
        self.status_combo.current(0)
        self.status_combo.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        #bbuttons frame
        button_frame = Frame(left_main_frame, bd=2, bg="white")
        button_frame.place(x=0, y=200, width=640, height=40)

        #savw buton
        save_btn = Button(button_frame, text="Import csv", font=("times new roman", 12, "bold"), bg="blue", fg="white",command=self.import_csv)
        save_btn.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        update_btn = Button(button_frame, text="Export csv", font=("times new roman", 12, "bold"), bg="blue", fg="white",command=self.export_csv)
        update_btn.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        delete_btn = Button(button_frame, text="Update",  font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        reset_btn = Button(button_frame, text="Reset", font=("times new roman", 12, "bold"), bg="blue", fg="white",command=self.reset_data)
        reset_btn.grid(row=0, column=3, padx=10, pady=5, sticky=W)
        
        # right frmae 
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=680, y=10, width=650, height=500)

        tabel_frame = Frame(right_frame, bd=2, bg="white",relief=RIDGE)
        tabel_frame.place(x=5, y=5, width=630, height=450)

        # ==========scroll bar table
        scroll_x=ttk.Scrollbar(tabel_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tabel_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(tabel_frame,column=("id","roll","name","department","time","date","attendance status"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
        scroll_x.pack(side=TOP,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        self.AttendanceReportTable.heading("id",text="AttendanceID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="time")
        self.AttendanceReportTable.heading("date",text="date ")
        self.AttendanceReportTable.heading("attendance status",text="attendance status")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=80)
        self.AttendanceReportTable.column("roll",width=70)
        self.AttendanceReportTable.column("name",width=70)
        self.AttendanceReportTable.column("department",width=70)
        self.AttendanceReportTable.column("time",width=70)
        self.AttendanceReportTable.column("date",width=70)
        self.AttendanceReportTable.column("attendance status",width=80)
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # ===================faetch data================================
    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    
    # import csv
    def import_csv(self):
        global my_data
        my_data.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        with open(fln) as f:
            csv_read=csv.reader(f,delimiter=',')
            for i in csv_read:
                my_data.append(i)
            self.fetch_data(my_data)

    # Export csv
    def export_csv(self):
        try:
            if len(my_data)<1:
                messagebox.showerror("No Data","No Data Found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfile(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode='w',newline="") as f1:
                exp_write=csv.writer(f1,delimiter=',')
                for i in my_data:
                    exp_write.writerow(i)
                messagebox.showinfo("Succesfully","Your data exported succesfully ")
        except Exception as e:
            messagebox.showerror("Error",f"Due to:{str(e)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_roll.set(rows[1])
        self.var_name.set(rows[2])
        self.var_department.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_attendance_status.set(rows[6])
    def reset_data(self):
        self.var_attend_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_department.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance_status.set("")
        
        






      




if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()