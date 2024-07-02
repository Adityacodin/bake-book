import customtkinter as ctk
from db.database import Database
from tkinter import messagebox
from PIL import Image
import math

class EmployeeWindow(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        def display_info(self,attributes):
            self.row = -1
            counter = 0
            if attributes[len(attributes)-1] == 'cake_weight':
                self.row = 0
                cake_info = self.product_frame[self.row]
                self.cake_buttons = []
                for frame in cake_info:
                    try:
                        logo_image = Image.open(str(self.info[self.row][counter][5]))
                        logo = ctk.CTkImage(light_image=logo_image, size=(100, 100))
                        ctk.CTkLabel(frame, text='', image=logo).pack(side='top',padx = 10,pady =10)
                        ctk.CTkLabel(frame,text = str(self.info[self.row][counter][2]+" - "+str(self.info[self.row][counter][3])+" Rs"),font = ("Garamond Bold",15),text_color='white').pack(side = 'top',padx = 10)
                        ctk.CTkLabel(frame,text = "Quantity - " + str(self.info[self.row][counter][6]),font = ("Garamond Bold",15),text_color='white').pack(side = 'top',padx = 10)
                        button = ctk.CTkButton(frame,text = 'Add To Cart',text_color = 'white', fg_color='#A569BD', hover_color='#D2B4DE',font = ("Garamond Bold",15))
                        button.pack(pady = 10,side='top')
                        self.cake_buttons.append(button)
                        counter+=1
                    except FileNotFoundError:
                        print("Image not found. Please check the path.")
            elif attributes[len(attributes)-1] == 'bread_units':
                self.row = 2
                bread_info = self.product_frame[self.row]
                self.bread_buttons = []
                for frame in bread_info:
                    try:
                        logo_image = Image.open(str(self.info[self.row][counter][5]))
                        logo = ctk.CTkImage(light_image=logo_image, size=(100, 100))
                        ctk.CTkLabel(frame, text='', image=logo).pack(side='top',padx = 10,pady =10)
                        ctk.CTkLabel(frame,text = str(self.info[self.row][counter][2]+" - "+str(self.info[self.row][counter][3])+" Rs"),font = ("Garamond Bold",15),text_color='white').pack(side = 'top',padx = 10)
                        ctk.CTkLabel(frame,text = "Quantity - " + str(self.info[self.row][counter][6]),font = ("Garamond Bold",15),text_color='white').pack(side = 'top',padx = 10)
                        button = ctk.CTkButton(frame,text = 'Add To Cart',text_color = 'white', fg_color='#A569BD', hover_color='#D2B4DE',font = ("Garamond Bold",15))
                        button.pack(pady = 10,side='top')                        
                        self.bread_buttons.append(button)
                        counter+=1
                    except FileNotFoundError:
                        print("Image not found. Please check the path.")
            else : 
                self.row = 1
                pastry_info = self.product_frame[self.row]  
                self.pastry_buttons = []
                for frame in pastry_info:
                    try:
                        logo_image = Image.open(str(self.info[self.row][counter][5]))
                        logo = ctk.CTkImage(light_image=logo_image, size=(100, 100))
                        ctk.CTkLabel(frame, text='', image=logo).pack(side='top',padx = 10,pady =10)
                        ctk.CTkLabel(frame,text = str(self.info[self.row][counter][2])+" - "+str(self.info[self.row][counter][3])+" Rs",font = ("Garamond Bold",15),text_color='white').pack(side = 'top',padx = 10)
                        ctk.CTkLabel(frame,text = "Quantity - 1 Unit",font = ("Garamond Bold",15),text_color='white').pack(side = 'top',padx = 10)
                        button = ctk.CTkButton(frame,text = 'Add To Cart',text_color = 'white', fg_color='#A569BD', hover_color='#D2B4DE',font = ("Garamond Bold",15))
                        button.pack(pady = 10,side='top')
                        self.pastry_buttons.append(button)
                        counter+=1
                    except FileNotFoundError:
                        print("Image not found. Please check the path.")
          

            
            

        def fill_frame(self,product,product_frame):
            self.attributes = None
            self.row = -1            
            if product == 'c':
                self.attributes = ['cake_id','bakery_name','cake_name','cake_price','cake_quantity','cake_img','cake_weight']
                self.row = 0
                counter = 0
                # print(self.row)
                frames = []
                for i in range(0,self.cake_row):
                    for j in range(0,3):
                        frame = ctk.CTkFrame(self.cake_frame[i],fg_color = '#8E44AD')
                        frame.pack(side='left',fill = 'both',expand = True,padx = 10,pady = 10)
                        frames.append(frame)
                        counter+=1
                        if len(self.info[self.row]) == counter:
                            break
                product_frame.append(frames)
                display_info(self,self.attributes)

            elif product == 'p':
                self.attributes = ['pastry_id','bakery_name','pastry_name','pastry_price','pastry_quantity','pastry_img']
                self.row = 1
                counter = 0
                # print(self.row)
                frames = []
                for i in range(0,self.pastry_row):
                    for j in range(0,3):
                        frame = ctk.CTkFrame(self.pastry_frame[i],fg_color = '#8E44AD')
                        frame.pack(side='left',fill = 'both',expand = True,padx = 10,pady = 10)
                        frames.append(frame)
                        counter+=1
                        if len(self.info[self.row]) == counter:
                            break
                product_frame.append(frames)
                display_info(self,self.attributes)

            elif product == 'b':
                self.attributes = ['bread_id','bakery_name','bread_name','bread_price','bread_quantity','bread_img','bread_units']
                self.row =2
                counter = 0
                frames = []
                for i in range(0,self.bread_row):
                    for j in range(0,3):
                        frame = ctk.CTkFrame(self.bread_frame[i],fg_color = '#8E44AD')
                        frame.pack(side='left',fill = 'both',expand = True,padx = 10,pady = 10)
                        frames.append(frame)
                        counter+=1
                        if len(self.info[self.row]) == counter:
                            break
                product_frame.append(frames)
                display_info(self,self.attributes)

        def display_contents(self):

            cake_scrollFrame = ctk.CTkScrollableFrame(self)

            self.cake_scroll = ctk.CTkScrollableFrame(self.cake_tab,fg_color = '#A569BD')
            self.cake_scroll.pack(fill = 'both',expand = True)
            self.pastry_scroll = ctk.CTkScrollableFrame(self.pastry_tab,fg_color = '#A569BD')
            self.pastry_scroll.pack(fill = 'both',expand = True)
            self.bread_scroll = ctk.CTkScrollableFrame(self.bread_tab,fg_color = '#A569BD')
            self.bread_scroll.pack(fill = 'both',expand = True)
            columns = 3
            self.cake_row = math.ceil(len(self.info[0])/columns)
            self.pastry_row = math.ceil(len(self.info[1])/columns)
            self.bread_row = math.ceil(len(self.info[2])/columns)
            print("bread_row_count = ",self.bread_row)
            self.product_frame = []
            self.cake_frame = []
            for i in range(0,self.cake_row):
                frame=ctk.CTkFrame(self.cake_scroll,fg_color='#A569BD')
                self.cake_frame.append(frame)
                self.cake_frame[i].pack(fill='both', expand=True)
            fill_frame(self,'c',self.product_frame)
            


            self.pastry_frame = []
            for i in range(0,self.pastry_row):
                frame=ctk.CTkFrame(self.pastry_scroll,fg_color='#A569BD')
                self.pastry_frame.append(frame)
                self.pastry_frame[i].pack(fill='both', expand=True)
            fill_frame(self,'p',self.product_frame)
                
            self.bread_frame = []
            for i in range(0,self.bread_row):
                frame=ctk.CTkFrame(self.bread_scroll,fg_color='#A569BD')
                self.bread_frame.append(frame)
                self.bread_frame[i].pack(fill='both', expand=True)
            fill_frame(self,'b',self.product_frame)

            

            


            
                





        
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

            display_contents(self)
            



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
                self.cake_info = self.db.fetch_results("SELECT * FROM cakes;")
                self.pastry_info = self.db.fetch_results("SELECT * FROM pastries;")
                self.bread_info = self.db.fetch_results("SELECT * FROM breads;")
                self.info = (self.cake_info,self.pastry_info,self.bread_info)
                display_employee_interface(self)
                


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
        self.employee_password = ctk.CTkEntry(self.frame_one,placeholder_text = "Password",show = '*')
        self.employee_password.place(relx = 0.5, rely = 0.45, anchor = ctk.CENTER)

        self.login_button = ctk.CTkButton(self.frame_one,text = 'Login',fg_color='#A569BD',hover_color='#8E44AD',command = lambda : login(self.employee_username.get(),self.employee_password.get()))
        self.login_button.place(relx = 0.5, rely = 0.6, anchor = ctk.CENTER)