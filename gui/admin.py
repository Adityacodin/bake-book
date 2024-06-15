import customtkinter as ctk
from db.database import Database
# from cryptography.fernet import Fernet
from tkinter import messagebox

class AdminWindow(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        def display_admin_interface(self):
            self.frame_one.destroy()
            self.frame_two = ctk.CTkFrame(self,fg_color = '#D2B4DE')
            self.frame_two.pack(fill = 'both',expand = True)

        def is_valid(username,password):
            db = Database('localhost',3306,'root','716807','bakery')
            credentials = db.fetch_results("Select username,password FROM users WHERE username = %s AND password = %s AND role = %s;",(username,password,'admin'))
            if username == credentials[0][0] and password == credentials[0][1]:
                print("Valid")
                print(credentials)
                return True
            else:
                print("Invalid")
                print(credentials)
                return False


        def login(username,password):
            if is_valid(username,password):
                display_admin_interface(self)
            else:
                messagebox.showerror("Login Failed","Invalid Credentials!")

        def check(suser,passw,c_passw,bakery_name):
            if passw  == c_passw:
                db = Database('localhost',3306, 'root', '716807', 'bakery')
            # key = Fernet.generate_key()
            # dec_key = key.decode()
            # db.execute_query("INSERT INTO settings (setting_key,setting_value) VALUES (%s,%s),(%s,%s);",('fernet_key',dec_key,'bakery_name',bakery_name))
            # passkey = passw.encode()
            # f_obj = Fernet(key)
            # encrypted_pass = f_obj.encrypt(passkey)
            db.execute_query("INSERT INTO settings (setting_key,setting_value) VALUES (%s,%s);",('bakery_name',bakery_name))
            db.execute_query("INSERT INTO users (username, password, role) VALUES (%s, %s, %s);", (user, passw, 'admin'))
            # print(encrypted_pass)
            messagebox.showinfo("Success","Registration successful")

        # db.execute_query("")


        def display_reg_window(self):
            self.frame_one.destroy()
            self.frame_two = ctk.CTkFrame(self,fg_color = '#D2B4DE')
            self.frame_two.pack(fill = 'both', expand = True)
            ctk.CTkLabel(self.frame_two,text = "Bakery name : ",font = ("Garamond Bold",15)).place(relx = 0.2, rely= 0.2 ,anchor = ctk.CENTER)
            self.bakery_name = ctk.CTkEntry(self.frame_two,placeholder_text = "Bakery Name")
            self.bakery_name.place(relx = 0.4, rely = 0.2, anchor=ctk.CENTER)
            ctk.CTkLabel(self.frame_two,text = "Admin username : ",font = ("Garamond Bold",15)).place(relx = 0.2, rely= 0.3 ,anchor = ctk.CENTER)
            self.admin_username = ctk.CTkEntry(self.frame_two,placeholder_text = "admin_username")
            self.admin_username.place(relx = 0.4, rely = 0.3, anchor=ctk.CENTER)
            ctk.CTkLabel(self.frame_two,text = "Set admin password : ",font = ("Garamond Bold",15)).place(relx = 0.2, rely= 0.4 ,anchor = ctk.CENTER)
            self.admin_password = ctk.CTkEntry(self.frame_two,placeholder_text = "admin_password")
            self.admin_password.place(relx = 0.4, rely = 0.4, anchor=ctk.CENTER)
            ctk.CTkLabel(self.frame_two,text = "Confirm password : ",font = ("Garamond Bold",15)).place(relx = 0.2, rely= 0.5 ,anchor = ctk.CENTER)
            self.c_password = ctk.CTkEntry(self.frame_two,placeholder_text = "admin_password")
            self.c_password.place(relx = 0.4, rely = 0.5, anchor=ctk.CENTER)

            ctk.CTkButton(self.frame_two,text = "Register",fg_color='#A569BD',hover_color='#8E44AD',command = lambda: check(self.admin_username.get(),self.admin_password.get(),self.c_password.get(),self.bakery_name.get())).place(relx = 0.5,rely = 0.6,anchor = ctk.CENTER)

        # self.configure(fg_color='#D2B4DE')
        self.pack(fill = "both", expand = True)
        self.frame_one = ctk.CTkFrame(self,fg_color='#D2B4DE')
        self.frame_one.pack(fill = 'both', expand = True)
        # self.back_button = ctk.CTkButton(self.frame_one, text = "<--",fg_color='#A569BD',hover_color='#8E44AD')
        # self.back_button.place(relx = 0.1, rely = 0.1, anchor = ctk.TOP)
        ctk.CTkLabel(self.frame_one,text="Bakebook", font = ("Garamond Bold",50)).pack(side = 'top',pady = 20)
        ctk.CTkLabel(self.frame_one,text="Admin Login", font = ("Garamond Bold",20)).pack(side = 'top',pady = 10)
        self.admin_username = ctk.CTkEntry(self.frame_one,placeholder_text = "Username")
        self.admin_username.place(relx = 0.5, rely = 0.4, anchor = ctk.CENTER)
        self.admin_password = ctk.CTkEntry(self.frame_one,placeholder_text = "Password")
        self.admin_password.place(relx = 0.5, rely = 0.45, anchor = ctk.CENTER)

        self.login_button = ctk.CTkButton(self.frame_one,text = 'Login',fg_color='#A569BD',hover_color='#8E44AD',command = lambda : login(self.admin_username.get(),self.admin_password.get()))
        self.login_button.place(relx = 0.5, rely = 0.6, anchor = ctk.CENTER)
        self.register_button = ctk.CTkButton(self.frame_one,text = 'Register',fg_color = '#A569BD',hover_color='#8E44AD',command = lambda: display_reg_window(self))
        self.register_button.place(relx = 0.5, rely = 0.65, anchor = ctk.CENTER)


    


