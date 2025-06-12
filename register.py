from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1350x750+0+0")

        img = Image.open(r"C:\Users\Akshi\FirstProject\FacialRecognitionSystem\Images\login5.png")
        img = img.resize((1350, 750), Image.ANTIALIAS)  # Resize to window size
        self.bg = ImageTk.PhotoImage(img)

        # vraibles==============
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_security_q = StringVar()
        self.var_security_a = StringVar()
        self.var_password = StringVar()
        self.var_confirm_password = StringVar()

        # Set the background
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relheight=1, relwidth=1)

        # =============left image===================================
        left_img = Image.open(r"C:\Users\Akshi\FirstProject\FacialRecognitionSystem\Images\register.png")
        left_img = left_img.resize((400, 600), Image.ANTIALIAS)
        self.left_photo = ImageTk.PhotoImage(left_img)

        left_lbl = Label(self.root, image=self.left_photo, bg="black")
        left_lbl.place(x=100, y=100, width=400, height=500)
        # =========Frame=====================
        frame = Frame(self.root, bg="white")
        frame.place(x=500, y=100, width=700, height=500)
        # Register label
        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="black", bg="white")
        register_lbl.place(x=20, y=20)

        # First Name
        fname_label = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname_label.place(x=50, y=80)
        self.fname_entry = Entry(frame, font=("times new roman", 15), bg="lightgray", textvariable=self.var_fname)
        self.fname_entry.place(x=50, y=110, width=250)

        # Last Name
        lname_label = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        lname_label.place(x=370, y=80)
        self.lname_entry = Entry(frame, font=("times new roman", 15), bg="lightgray", textvariable=self.var_lname)
        self.lname_entry.place(x=370, y=110, width=250)

        # Contact No
        contact_label = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white")
        contact_label.place(x=50, y=160)
        self.contact_entry = Entry(frame, font=("times new roman", 15), bg="lightgray", textvariable=self.var_contact)
        self.contact_entry.place(x=50, y=190, width=250)

        # Email
        email_label = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        email_label.place(x=370, y=160)
        self.email_entry = Entry(frame, font=("times new roman", 15), bg="lightgray", textvariable=self.var_email)
        self.email_entry.place(x=370, y=190, width=250)

        # Security Question
        security_q_label = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
        security_q_label.place(x=50, y=240)
        self.security_q_combo = ttk.Combobox(frame, font=("times new roman", 13), state="readonly", textvariable=self.var_security_q)
        self.security_q_combo["values"] = ("Select", "Your Birth Place", "Your Pet Name","your faviourite destination","Favourite color")
        self.security_q_combo.current(0)
        self.security_q_combo.place(x=50, y=270, width=250)

        # Security Answer
        security_a_label = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        security_a_label.place(x=370, y=240)
        self.security_a_entry = Entry(frame, font=("times new roman", 15), bg="lightgray", textvariable=self.var_security_a)
        self.security_a_entry.place(x=370, y=270, width=250)

        # Password
        password_label = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        password_label.place(x=50, y=320)
        self.password_entry = Entry(frame, font=("times new roman", 15), bg="lightgray", show="*", textvariable=self.var_password)
        self.password_entry.place(x=50, y=350, width=250)

        # Confirm Password
        confirm_password_label = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white")
        confirm_password_label.place(x=370, y=320)
        self.confirm_password_entry = Entry(frame, font=("times new roman", 15), bg="lightgray", show="*", textvariable=self.var_confirm_password)
        self.confirm_password_entry.place(x=370, y=350, width=250)


        # Terms and Conditions Checkbutton
        self.var_chk = IntVar()
        self.chk_btn = Checkbutton(frame, text="I Agree to the Terms & Conditions", variable=self.var_chk, font=("times new roman", 12), bg="white", onvalue=1, offvalue=0)
        self.chk_btn.place(x=50, y=400)

        # Register Now Button as Image
        register_img = Image.open(r"C:\Users\Akshi\FirstProject\FacialRecognitionSystem\Images\register_now.png")
        register_img = register_img.resize((200, 50), Image.ANTIALIAS)
        self.register_photo = ImageTk.PhotoImage(register_img)

        register_btn = Button(frame, image=self.register_photo, bd=0, cursor="hand2", bg="white", activebackground="white", command=self.register_data)
        register_btn.place(x=250, y=440, width=200, height=50)
        # Login Button as Image
        login_img = Image.open(r"C:\Users\Akshi\FirstProject\FacialRecognitionSystem\Images\login_now.png")
        login_img = login_img.resize((200, 50), Image.ANTIALIAS)
        self.login_photo = ImageTk.PhotoImage(login_img)

        login_btn = Button(frame, image=self.login_photo, bd=0, cursor="hand2", bg="white", activebackground="white")
        login_btn.place(x=480, y=440, width=200, height=50)

        # =========Fubctionality declaration===============
    def register_data(self):
        if (self.fname_entry.get() == "" or
            self.lname_entry.get() == "" or
            self.contact_entry.get() == "" or
            self.email_entry.get() == "" or
            self.security_q_combo.get() == "Select" or
            self.security_a_entry.get() == "" or
            self.password_entry.get() == "" or
            self.confirm_password_entry.get() == ""):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        elif self.password_entry.get() != self.confirm_password_entry.get():
            messagebox.showerror("Error", "Password and Confirm Password must be same", parent=self.root)
            return

        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms and conditions", parent=self.root)
            return

        # Here you can add code to save the data to a database or file
        else:
            import mysql.connector
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Akshith@242",
                    database="face_recognizer"
                )
                cur = conn.cursor()
                cur.execute("SELECT * FROM register WHERE email=%s", (self.var_email.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "User already exists, please try another email", parent=self.root)
                    conn.close()
                    return
                cur.execute(
                    "INSERT INTO register (first_name, last_name, contact, email, securityQ, securityA, password) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_security_q.get(),
                        self.var_security_a.get(),
                        self.var_password.get()
                    )
                )
                conn.commit()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Database error: {str(e)}", parent=self.root)
                return
            messagebox.showinfo("Success", "Registered Successfully!", parent=self.root)




if __name__=="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()
