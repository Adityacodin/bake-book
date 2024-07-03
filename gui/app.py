import customtkinter as ctk 
import tkinter as tk 
from PIL import Image
from gui.admin import AdminWindow
from gui.emp import EmployeeWindow

class App(ctk.CTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        def display_admin_win(self):
            self.to_login_frame.destroy()
            self.admin_login = AdminWindow(self.main_frame)

        def display_employee_win(self):
            self.to_login_frame.destroy()
            self.emp_login = EmployeeWindow(self.main_frame)

        def display_login(self):
            self.to_login_frame = ctk.CTkFrame(master=self.main_frame, fg_color='#ffffff')
            self.to_login_frame.pack(fill='both', expand=True)
            try:
                logo_image = Image.open('C:/Users/33333333333333333333/gitdemo/bake-book/images/cake_cj7_icon.ico')
                logo = ctk.CTkImage(light_image=logo_image, size=(200, 200))
                ctk.CTkLabel(self.to_login_frame, text='', image=logo).pack(side='top')
            except FileNotFoundError:
                print("Image not found. Please check the path.")
            ctk.CTkLabel(self.to_login_frame, text='Bake-Book', font=('Garamond bold', 24)).pack(side='top', pady=20)
            ctk.CTkLabel(self.to_login_frame, text='Manage your bakery like a piece of cake :)', font=('Garamond bold', 14)).pack(side='top')
            ctk.CTkButton(self.to_login_frame, text='Admin', fg_color='#A569BD', hover_color='#8E44AD', command=lambda: display_admin_win(self)).place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
            ctk.CTkButton(self.to_login_frame, text='Employee', fg_color='#A569BD', hover_color='#8E44AD', command= lambda: display_employee_win(self)).place(relx=0.5, rely=0.57, anchor=ctk.CENTER)

        self.title("Bakebook")
        self.geometry('800x650')
        self.main_frame = ctk.CTkFrame(self,fg_color = 'light gray')
        self.main_frame.pack(fill="both",expand = True)
        display_login(self)
