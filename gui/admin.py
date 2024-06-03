import customtkinter as ctk 

class AdminWindow(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.configure(fg_color='#D2B4DE')
        self.pack(fill = "both", expand = True)
        ctk.CTkLabel(self,text="Bakebook", font = ("Garamond Bold",30)).pack(side = 'top',pady = 20)
        ctk.CTkLabel(self,text="Admin Login", font = ("Garamond Bold",20)).pack(side = 'top',pady = 20)
        self.admin_username = ctk.CTkEntry(self,placeholder_text = "Username")
        self.admin_username.place(relx = 0.5, rely = 0.4, anchor = ctk.CENTER)
        self.admin_password = ctk.CTkEntry(self,placeholder_text = "Password")
        self.admin_password.place(relx = 0.5, rely = 0.45, anchor = ctk.CENTER)

        self.login_button = ctk.CTkButton(self,text = 'Login',fg_color='#A569BD',hover_color='#8E44AD')
        self.login_button.place(relx = 0.5, rely = 0.6, anchor = ctk.CENTER)