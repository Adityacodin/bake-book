import customtkinter as ctk
from db.database import Database
from tkinter import messagebox

class EmployeeWindow(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

    
        def display_employee_interface(self):
            self.frame_one.destroy()
            self.frame_two = ctk.CTkFrame(self,fg_color = '#D2B4DE')
            self.frame_two.pack(fill = 'both',expand = True)

            self.Tab = ctk.CTkTabview(self.frame_two,fg_color='#8E44AD',
            segmented_button_fg_color='#8E44AD',
            segmented_button_selected_color='#D2B4DE',
            segmented_button_unselected_color='#8E44AD',
            segmented_button_selected_hover_color='#D2B4DE',
            segmented_button_unselected_hover_color='#8E44AD')
            self.Tab.pack(padx = 10, pady = 10,fill = 'both',expand = True)
            self.cake_tab = self.Tab.add('Cake')
            self.pastry_tab = self.Tab.add('Pastry')
            self.bread_tab = self.Tab.add('Breads')
            self.inventory_tab = self.Tab.add('Inventory')


        def is_valid(self,username,password):
            self.db = Database('localhost',3306,'root','716807','bakery')
            credentials = self.db.fetch_results("SELECT username,password FROM users WHERE username = %s AND password = %s AND role = %s;",(username,password,'employee'))
            # print(credentials)
            if username == credentials[0][0] and password == credentials[0][1]:
                print("Valid")
                print(credentials)
                return True
            else:
                print("Invalid")
                print(credentials)
                return False

        def login(username,password):
            if username == '' and password == '':
                messagebox.showerror('','Username and Password field cannot be empty.')
            elif username == '' or password == '':
                if username == '':
                    messagebox.showerror('','Username field cannot be empty.')
                else:
                    messagebox.showerror('','Password field cannot be empty.')

            if is_valid(self,username,password):
                display_employee_interface(self)
                self.cake_info = self.db.fetch_results("SELECT * FROM cakes;")
                self.pastry_info = self.db.fetch_results("SELECT * FROM pastries;")
                self.bread_info = self.db.fetch_results("SELECT * FROM breads;")

                print(self.cake_info)

            else:
                messagebox.showerror("Login Failed","Invalid Credentials!")

        # self.configure(fg_color='#D2B4DE')
        self.pack(fill = "both", expand = True)
        self.frame_one = ctk.CTkFrame(self,fg_color='#D2B4DE')
        self.frame_one.pack(fill = 'both', expand = True)
        ctk.CTkLabel(self.frame_one,text="Bakebook", font = ("Garamond Bold",50)).pack(side = 'top',pady = 20)
        ctk.CTkLabel(self.frame_one,text="Employee Login", font = ("Garamond Bold",20)).pack(side = 'top',pady = 10)
        self.employee_username = ctk.CTkEntry(self.frame_one,placeholder_text = "Username")
        self.employee_username.place(relx = 0.5, rely = 0.4, anchor = ctk.CENTER)
        self.employee_password = ctk.CTkEntry(self.frame_one,placeholder_text = "Password")
        self.employee_password.place(relx = 0.5, rely = 0.45, anchor = ctk.CENTER)

        self.login_button = ctk.CTkButton(self.frame_one,text = 'Login',fg_color='#A569BD',hover_color='#8E44AD',command = lambda : login(self.employee_username.get(),self.employee_password.get()))
        self.login_button.place(relx = 0.5, rely = 0.6, anchor = ctk.CENTER)