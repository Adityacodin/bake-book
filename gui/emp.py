import customtkinter as ctk
from db.database import Database
from tkinter import messagebox
from PIL import Image
import math
from gui.spinbox import FloatSpinbox
from tkinter import ttk



class EmployeeWindow(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        # def on_closing():
        #     del open_windows[product_id]
        #     quantity_window.destroy()

        def add(self,product_info,quantity,quantity_win):
            if str(quantity).isnumeric() :
                 self.order_list.append((product_info,int(quantity)))
                 self.open_windows.remove(int(product_info[0]))
                 quantity_win.destroy()

        def calculate(list):
            sum = 0
            for entry in list:
                sum += int(entry[len(entry)-1])
            return sum

        def clicked_confirmed(self,closing_window):
            self.flag = True
            closing_window.destroy()
            
            for entry in self.order_list:
                if entry[0][len(entry[0])-1] == 'One Kilo' or entry[0][len(entry[0])-1] == 'Half Kilo':
                    print(1)
                    self.db.execute_query("UPDATE cakes SET cake_quantity = cake_quantity-%s WHERE cake_id = %s",(str(entry[1]),str(entry[0][0])))
                elif len(entry[0]) == 7:
                    print(3)
                    self.db.execute_query("UPDATE breads SET bread_quantity = bread_quantity-%s WHERE bread_id = %s",(str(entry[1]),str(entry[0][0])))
                elif len(entry[0]) == 6:
                    print(2)
                    self.db.execute_query("UPDATE pastries SET pastry_quantity = pastry_quantity-%s WHERE pastry_id = %s",(str(entry[1]),str(entry[0][0])))

            total = calculate(self.info1)
            
            messagebox.showinfo('Success',f'Order Processed Successfully\nOrder Total is {total} Rs')


 
        def confirm_order(self):
            confirm_window = ctk.CTk()
            confirm_window.geometry('900x500')
            confirm_window.title('Confirm Order')
            frame = ctk.CTkFrame(confirm_window,fg_color = '#8E44AD')
            frame.pack(fill = 'both',expand = True)
            self.info1 = []
            i=0
            for entry in self.order_list:
                self.info1.append([str(entry[0][0]),entry[0][2],str(entry[1]),str(entry[1]*entry[0][3])])

            table = ttk.Treeview(frame,columns=('prod_id','prod_name','quantity','price'),show='headings')
            table.heading('prod_id',text = 'Product ID')
            table.heading('prod_name',text = 'Product')
            table.heading('quantity',text = 'Quantity')
            table.heading('price',text = 'Price')
            for i in range(len(self.info1)):
                data = self.info1[i]
                table.insert(parent='',index = 0, values = data)
            table.pack(fill = 'both',expand = True,padx = 20,pady = 20)
            confirm_btn = ctk.CTkButton(frame,text = 'Confirm',command = lambda : clicked_confirmed(self,confirm_window))
            confirm_btn.pack(padx = 10,pady = 10)
            confirm_window.mainloop()
        
        def checkout(self):
            self.flag = False
            if str(type(self.order_list)) == "<class 'NoneType'>" :
                messagebox.showerror('Invalid action','Cart is empty N')
            elif str(type(self.order_list)) == "<class 'list'>" and len(self.order_list) == 0:
                messagebox.showerror('Invalid action','Cart is empty F')
            else :
                confirm_order(self)
                

        def clicked_proceed(self,win):
            win.destroy()
            self.order_list.clear()

        def clicked_cancel(win):
            win.destroy()

        def new_order(self):
            if str(type(self.order_list)) != "<class 'NoneType'>":
                msg_app = ctk.CTk()
                frame = ctk.CTkFrame(msg_app)
                frame.pack(fill = 'both',expand = True)
                ctk.CTkLabel(frame,text = "There happens to be some items in the cart from previous order, if you proceed then the record of items from previous order which was not completed will be deleted.").pack(padx = 10, pady = 20)
                proceed_btn = ctk.CTkButton(frame,text = 'Proceed',command = lambda : clicked_proceed(self,msg_app))
                proceed_btn.place(relx = 0.3,rely = 0.6)
                cancel_btn = ctk.CTkButton(frame,text = 'Cancel',command = lambda : clicked_cancel(msg_app))
                cancel_btn.place(relx = 0.6,rely = 0.6)
                msg_app.geometry('950x150')
                msg_app.mainloop()
            else :
                self.order_list = []
                self.open_windows = []
                messagebox.showinfo('','New cart has been initialised, you may proceed to add items') 

        def check(self,product_id) : 
            if product_id in self.open_windows:
                return False
            else :
                return True

                
        def add_to_cart(self,product_info,product_type):
            if str(type(self.order_list)) == "<class 'NoneType'>":
                messagebox.showerror("Warning","Kindly initialise a new cart in order to add items in to the cart")
            else : 
                if check(self,int(product_info[0])) :
                    self.open_windows.append(int(product_info[0]))
                    quantity_win = ctk.CTk()
                    quantity_win.geometry('400x100')
                    quantity_win.title('Quantity for '+ str(product_info[2]))
                    frame = ctk.CTkFrame(quantity_win,fg_color = '#8E44AD')
                    frame.pack(fill = 'both',expand = True)
                    quantity = FloatSpinbox(frame,step_size = 1,to_value = product_info[4])
                    quantity.place(relx = 0.5,rely = 0.4 ,anchor = ctk.CENTER)
                    proceed_btn = ctk.CTkButton(frame,text = 'Proceed',command = lambda : add(self,product_info,quantity.get(),quantity_win))
                    proceed_btn.pack(side = 'bottom',padx = 10,pady = 10)
                    quantity_win.mainloop()
                    self.order_list.append(product_info)
            

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
                        product_name = self.info[self.row][counter]
                        ctk.CTkLabel(frame,text = str(self.info[self.row][counter][2]+" - "+str(self.info[self.row][counter][3])+" Rs"),font = ("Garamond Bold",15),text_color='white').pack(side = 'top',padx = 10)
                        ctk.CTkLabel(frame,text = "Quantity - " + str(self.info[self.row][counter][6]),font = ("Garamond Bold",15),text_color='white').pack(side = 'top',padx = 10)
                        button = ctk.CTkButton(frame,text = 'Add To Cart',text_color = 'white', fg_color='#A569BD', hover_color='#D2B4DE',font = ("Garamond Bold",15),command = lambda product_info = product_name : add_to_cart(self,product_info,'cake'))
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
                        product_name = self.info[self.row][counter]
                        ctk.CTkLabel(frame,text = str(self.info[self.row][counter][2]+" - "+str(self.info[self.row][counter][3])+" Rs"),font = ("Garamond Bold",15),text_color='white').pack(side = 'top',padx = 10)
                        ctk.CTkLabel(frame,text = "Quantity - " + str(self.info[self.row][counter][6]),font = ("Garamond Bold",15),text_color='white').pack(side = 'top',padx = 10)
                        button = ctk.CTkButton(frame,text = 'Add To Cart',text_color = 'white', fg_color='#A569BD', hover_color='#D2B4DE',font = ("Garamond Bold",15),command = lambda product_info = product_name : add_to_cart(self,product_info,'bread'))
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
                        product_name = self.info[self.row][counter]
                        ctk.CTkLabel(frame,text = str(self.info[self.row][counter][2])+" - "+str(self.info[self.row][counter][3])+" Rs",font = ("Garamond Bold",15),text_color='white').pack(side = 'top',padx = 10)
                        ctk.CTkLabel(frame,text = "Quantity - 1 Unit",font = ("Garamond Bold",15),text_color='white').pack(side = 'top',padx = 10)
                        button = ctk.CTkButton(frame,text = 'Add To Cart',text_color = 'white', fg_color='#A569BD', hover_color='#D2B4DE',font = ("Garamond Bold",15),command = lambda product_info = product_name : add_to_cart(self,product_info,'pastry'))
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
        
        def insert_values(self):
            cake_selected = self.cake_table.get_children()
            pastry_selected = self.pastry_table.get_children()
            bread_selected = self.bread_table.get_children()
            if (len(cake_selected) + len(pastry_selected)+len(bread_selected)) != 0:
                for item in cake_selected:
                    self.cake_table.delete(item)
                for item in pastry_selected:
                    self.pastry_table.delete(item)
                for item in bread_selected:
                    self.bread_table.delete(item)
            
            cake_info = self.db.fetch_results("Select cake_id,cake_name,cake_quantity FROM cakes;")
            pastry_info = self.db.fetch_results("Select pastry_id,pastry_name,pastry_quantity FROM pastries;")
            bread_info = self.db.fetch_results("Select bread_id,bread_name,bread_quantity FROM breads;")

            for i in range(0,len(cake_info)):
                data = cake_info[len(cake_info)-1-i]
                self.cake_table.insert(parent='',index = 0, values = data)
            for i in range(0,len(pastry_info)):
                data = pastry_info[len(pastry_info)-1-i]
                self.pastry_table.insert(parent='',index = 0, values = data)
            for i in range(0,len(bread_info)):
                data = bread_info[len(bread_info)-1-i]
                self.bread_table.insert(parent='',index = 0, values = data)
            

            

        def display_contents(self):
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
            self.order_list = None
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

            # display_inventory
            self.inv_frame = ctk.CTkScrollableFrame(self.inventory_tab,fg_color='#8E44AD')
            self.inv_frame.pack(fill = 'both',expand =True)
            self.refresh_btn = ctk.CTkButton(self.inv_frame,text = 'Refresh',command = lambda : insert_values(self)) 
            self.refresh_btn.pack(padx = 10,pady = 10)
            self.cake_table = ttk.Treeview(self.inv_frame,columns = ('cid','c_prod','c_quant'),show = 'headings')
            self.cake_table.heading('cid',text='Cake ID')
            self.cake_table.heading('c_prod',text='Cake Name')
            self.cake_table.heading('c_quant',text='Quantity')
            self.cake_table.pack(pady = 10)

            self.pastry_table = ttk.Treeview(self.inv_frame,columns = ('cid','c_prod','c_quant'),show = 'headings')
            self.pastry_table.heading('cid',text='Pastry ID')
            self.pastry_table.heading('c_prod',text='Pastry Name')
            self.pastry_table.heading('c_quant',text='Quantity')
            self.pastry_table.pack(pady =10)

            self.bread_table = ttk.Treeview(self.inv_frame,columns = ('cid','c_prod','c_quant'),show = 'headings')
            self.bread_table.heading('cid',text='Bread ID')
            self.bread_table.heading('c_prod',text='Bread Name')
            self.bread_table.heading('c_quant',text='Quantity')
            self.bread_table.pack(pady = 10)
            insert_values(self)            
    
        def display_employee_interface(self):
            self.frame_one.destroy()
            self.frame_two = ctk.CTkFrame(self,fg_color = '#D2B4DE')
            self.frame_two.pack(fill = 'both',expand = True)

            self.new_cart_btn = ctk.CTkButton(self.frame_two,text = "New Order",command = lambda: new_order(self),text_color = 'white',fg_color='#A569BD',hover_color='#8E44AD',font = ("Garamond Bold",15))
            self.new_cart_btn.pack(side = 'top',padx = 10,pady = 10)

            self.checkout_btn = ctk.CTkButton(self.frame_two,text = "Checkout",command = lambda: checkout(self),text_color = 'white',fg_color='#A569BD',hover_color='#8E44AD',font = ("Garamond Bold",15))
            self.checkout_btn.pack(side = 'bottom',padx = 10,pady = 10)

            self.Tab = ctk.CTkTabview(self.frame_two,fg_color='#8E44AD',
            segmented_button_fg_color='#8E44AD',
            segmented_button_selected_color='#D2B4DE',
            segmented_button_unselected_color='#8E44AD',
            segmented_button_selected_hover_color='#D2B4DE',
            segmented_button_unselected_hover_color='#8E44AD')
            self.Tab.pack(padx = 10, pady = 10,fill = 'both',expand = True)
            self.cake_tab = self.Tab.add('Cake')
            self.pastry_tab = self.Tab.add('Pastry')
            self.bread_tab = self.Tab.add('Bread')
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