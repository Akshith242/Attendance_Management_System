from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql
from register import Register
from main import Face_Recognition_System

def main():
    win=Tk()
    app=Login(win)
    win.mainloop()

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1366x768+0+0") 

        # Open and resize the image
        img = Image.open(r"C:\Users\Akshi\FirstProject\FacialRecognitionSystem\Images\login.png")
        img = img.resize((1366, 768), Image.ANTIALIAS)  # Resize to window size
        self.bg = ImageTk.PhotoImage(img)

        # Set the background
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relheight=1, relwidth=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=500,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\Akshi\FirstProject\FacialRecognitionSystem\Images\login2.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        img_lbl=Label(image=self.photoimage1,bg="black",borderwidth=0)
        img_lbl.place(x=620,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=100,y=100)

        # Label
        username_label = Label(frame, text="USERNAME:", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username_label.place(x=50, y=155)

        self.textuser = ttk.Entry(frame, font=("times new roman", 15))
        self.textuser.place(x=40, y=180, width=270)
        password_label = Label(frame, text="PASSWORD:", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password_label.place(x=50, y=225)

        self.textpass = ttk.Entry(frame, font=("times new roman", 15), show="*")
        self.textpass.place(x=40, y=250, width=270)

        # Icon Images
        img2=Image.open(r"C:\Users\Akshi\FirstProject\FacialRecognitionSystem\Images\login4.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        img_lb2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        img_lb2.place(x=530,y=330,width=20,height=20)

        img3 = Image.open(r"C:\Users\Akshi\FirstProject\FacialRecognitionSystem\Images\login3.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        img_lb3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        img_lb3.place(x=530, y=400, width=20, height=20)

        # Login Button
        login_btn = Button(frame, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="#1a75ff", activeforeground="white", activebackground="#0052cc", cursor="hand2",command=self.login_win)
        login_btn.place(x=110, y=300, width=120, height=40)
        register_btn = Button(frame, text="Register", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="#28a745", activeforeground="white", activebackground="#218838", cursor="hand2",command=self.register_window)
        register_btn.place(x=110, y=360, width=120, height=40)
        forget_btn = Button(frame, text="Forgot Password?", font=("times new roman", 12, "underline"), bd=0, fg="#ff9933", bg="black", activeforeground="#ff9933", activebackground="black", cursor="hand2",command=self.forget_password)
        forget_btn.place(x=100, y=410, width=140, height=30)


    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    

    def login_win(self):
        if self.textuser.get()=="" or self.textpass.get()=="":
            messagebox.showerror("Error","Please enter both username and password")
        elif self.textuser.get()=="akshith" and self.textpass.get()=="akki":
            
            messagebox.showinfo("Sucess","Welcome to Student Management System")
        else:
            # messagebox.showerror("Invalid","Invalid username or password")
            conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Akshith@242",
                    database="face_recognizer"
                )
            cur = conn.cursor()
            cur.execute("SELECT * FROM register WHERE email=%s and password=%s", (self.textuser.get(), self.textpass.get()))

            row=cur.fetchone()
            if row == None:
                messagebox.showerror("Error","Invalid Username and password")
            else:
                open=messagebox.askyesno("YesNo","Only Admins has access")
                if open:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open:
                        return
            conn.commit()
            conn.close()


    def reset_password(self):
            if self.security_q_combo.get() == "Select":
                messagebox.showerror("Error", "Select the security question", parent=self.root2)
                return
            if self.security_a_entry.get() == "":
                messagebox.showerror("Error", "Please enter the answer", parent=self.root2)
                return
            if self.security_new_pass.get() == "":
                messagebox.showerror("Error", "Please enter the new password", parent=self.root2)
                return

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Akshith@242",
                database="face_recognizer"
            )
            cur = conn.cursor()
            query = "SELECT * FROM register WHERE email=%s AND securityQ=%s AND securityA=%s"
            value = (self.textuser.get(), self.security_q_combo.get(), self.security_a_entry.get())
            cur.execute(query, value)
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Incorrect security answer", parent=self.root2)
            else:
                update_query = "UPDATE register SET password=%s WHERE email=%s"
                cur.execute(update_query, (self.security_new_pass.get(), self.textuser.get()))
                conn.commit()
                messagebox.showinfo("Success", "Password reset successful. Please login with new password.", parent=self.root2)
                self.root2.destroy()
            conn.close()


    def forget_password(self):
        if self.textuser.get()=="":
            messagebox.showerror("Error","Please enter your email address to reset passowrd")
        else:
            conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Akshith@242",
                    database="face_recognizer"
                )
            cur = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.textuser.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
            # print(row)
            if row==None:
                messagebox.showerror("Error","Please enter  the valid user name(email)")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget password")
                self.root2.geometry("340x450+610+170")

                lbl = Label(self.root2, text="Forgot Password", font=("times new roman", 20, "bold"), fg="navy", bg="white")
                lbl.place(x=0, y=10, relwidth=1)

                 # Security Question
                security_q_label = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
                security_q_label.place(x=50, y=80)
                self.security_q_combo = ttk.Combobox(self.root2, font=("times new roman", 13), state="readonly")
                self.security_q_combo["values"] = ("Select", "Your Birth Place", "Your Pet Name","your faviourite destination","Favourite color")
                self.security_q_combo.current(0)
                self.security_q_combo.place(x=50, y=110, width=250)

                # Security Answer
                security_a_label = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
                security_a_label.place(x=50, y=150)
                self.security_a_entry = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
                self.security_a_entry.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New Passoword", font=("times new roman", 15, "bold"), bg="white")
                new_password.place(x=50, y=220)
                self.security_new_pass = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
                self.security_new_pass.place(x=50, y=250, width=250)

                # Reset Password Button
                reset_btn = Button(
                    self.root2,
                    text="RESET",
                    font=("times new roman", 15, "bold"),
                    bg="#1a75ff",
                    fg="white",
                    bd=3,
                    relief=RIDGE,
                    activebackground="#0052cc",
                    activeforeground="white",
                    cursor="hand2",
                    command=self.reset_password
                )
                reset_btn.place(x=100, y=300)

                # Add reset_password method to handle the reset logic
                




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

        login_btn = Button(frame, image=self.login_photo, bd=0, cursor="hand2", bg="white", activebackground="white",command=self.return_login)
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

    def return_login(self):
        self.root.destroy()
            
           


if __name__ == "__main__":
    # root=Tk()
    # obj=Login(root)
    # root.mainloop()
    main()
   
    
