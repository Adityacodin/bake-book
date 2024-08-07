import customtkinter as ctk
from db.database import Database
# from cryptography.fernet import 
from gui.spinbox import FloatSpinbox 
from tkinter import ttk
from tkinter import messagebox

class AdminWindow(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        def display_table(self):
            if not self.flag:
                self.flag = True
                self.tab_win = ctk.CTk()
                self.tab_win.title('Inventory Table')
                self.tab_win.geometry('800x650')
                self.main_fm = ctk.CTkScrollableFrame(self.tab_win,fg_color = '#8E44AD')
                self.main_fm.pack(fill = 'both',expand = True)
                self.cake_table = ttk.Treeview(self.main_fm,columns = ('cid','c_prod','c_quant','c_price'),show = 'headings')
                self.cake_table.heading('cid',text='ID')
                self.cake_table.heading('c_prod',text='Cake Name')
                self.cake_table.heading('c_quant',text='Quantity')
                self.cake_table.heading('c_price',text = 'Price')
                self.cake_table.pack(pady = 10)

                self.pastry_table = ttk.Treeview(self.main_fm,columns = ('cid','c_prod','c_quant','c_price'),show = 'headings')
                self.pastry_table.heading('cid',text='PaID')
                self.pastry_table.heading('c_prod',text='Pastry Name')
                self.pastry_table.heading('c_quant',text='Quantity')
                self.cake_table.heading('c_price',text = 'Price')
                self.pastry_table.pack(pady =10)

                self.bread_table = ttk.Treeview(self.main_fm,columns = ('cid','c_prod','c_quant','c_price'),show = 'headings')
                self.bread_table.heading('cid',text='BID')
                self.bread_table.heading('c_prod',text='Bread Name')
                self.bread_table.heading('c_quant',text='Quantity')
                self.cake_table.heading('c_price',text = 'Price')
                self.bread_table.pack(pady = 10)

                for i in range(0,3):
                    List = self.inv_info[i]
                    c=0
                    for j in range(0,len(List)):
                        data = List[len(List)-1-c]
                        c+=1
                        if i==0:
                            self.cake_table.insert(parent='',index = 0, values = data)
                        elif i == 1:
                            self.pastry_table.insert(parent='',index = 0, values = data)
                        elif i==2:
                            self.bread_table.insert(parent='',index = 0, values = data)


                self.tab_win.mainloop()         
                self.flag = False
                print(self.flag)  

        def add(self,p_upd,category):
            if str(self.spin.get()).isnumeric():
                if category == 'Cake':
                    self.db_cursor.execute_query("UPDATE cakes set cake_quantity = cake_quantity + %s WHERE cake_id = %s",(str(self.spin.get()),str(p_upd[0])))
                elif category == 'Pastry':
                    self.db_cursor.execute_query("UPDATE pastries set pastry_quantity = pastry_quantity + %s WHERE pastry_id = %s",(str(self.spin.get()),str(p_upd[0])))
                elif category == 'Bread':
                    self.db_cursor.execute_query("UPDATE breads set bread_quantity = bread_quantity + %s WHERE bread_id = %s",(str(self.spin.get()),str(p_upd[0])))
                messagebox.showinfo("Success","Inventory Update Successfully")
            else :
                messagebox.showerror("Invalid data","Please enter Numerical Values")


        def update_quantity(self,p_upd,category):
            self.spin_win = ctk.CTk()
            self.spin_win.title(f'Update {p_upd[1]}')
            self.spin_win.geometry('300x200')
            self.frame = ctk.CTkFrame(self.spin_win,fg_color = '#8E44AD')
            self.frame.pack(fill = 'both',expand = True)
            self.spin = FloatSpinbox(self.frame,step_size= 1,to_value = 100)
            self.spin.place(relx = 0.5,rely  =0.4,anchor = ctk.CENTER)
            self.add_btn = ctk.CTkButton(self.frame,text = 'Add',command =lambda : add(self,p_upd,category))
            self.add_btn.place(relx = 0.5,rely = 0.6,anchor = ctk.CENTER)
            self.spin_win.mainloop()

        def valid(self,data):
            if data.isnumeric() :
                if str(type(self.prod_frame)) == "<class 'customtkinter.windows.widgets.ctk_frame.CTkFrame'>":
                    self.prod_frame.destroy()
                id = int(self.product_id.get())
                self.product_to_updated = None
                self.prod_frame = ctk.CTkFrame(self.inv_tab,fg_color = '#8E44AD')
                self.prod_frame.pack(fill = 'both',expand = True)
                if id>=100 and id<=self.inv_info[0][len(self.inv_info[0])-1][0] :
                    for entry in self.inv_info[0]:
                        if entry[0] == id:
                            self.product_to_be_updated = self.db_cursor.fetch_results("SELECT cake_id,cake_name,cake_quantity,cake_price FROM cakes WHERE cake_id = %s",str(id))
                            print(self.product_to_be_updated)
                elif id>=200 and id<=self.inv_info[1][len(self.inv_info[1])-1][0] :
                    for entry in self.inv_info[1]:
                        if entry[0] == id:
                            self.product_to_be_updated = self.db_cursor.fetch_results("SELECT pastry_id,pastry_name,pastry_quantity,pastry_price FROM pastries WHERE pastry_id = %s",str(id))
                elif id>=300 and id<=self.inv_info[2][len(self.inv_info[2])-1][0] :
                    for entry in self.inv_info[2]:
                        if entry[0] == id:
                            self.product_to_be_updated = self.db_cursor.fetch_results("SELECT bread_id,bread_name,bread_quantity,bread_price FROM breads WHERE bread_id = %s",str(id))
                else :
                    messagebox.showerror("Invalid data","enter valid product id".title())
                    return
                
                category = None
                if entry[0] < 200:
                    category = 'cake'.title()
                elif entry[0] < 300:
                    category = 'pastry'.title()
                else :
                    category = 'bread'.title()
                ctk.CTkLabel(self.prod_frame,text = f'Product Name : {self.product_to_be_updated[0][1]}',font = ("Garamond Bold",15),text_color = 'white').place(relx = 0.2,rely = 0.1,anchor =ctk.CENTER)
                ctk.CTkLabel(self.prod_frame,text = f'Product Quantity : {self.product_to_be_updated[0][2]}',font = ("Garamond Bold",15),text_color = 'white').place(relx = 0.2,rely = 0.3,anchor =ctk.CENTER)
                self.change_quant_btn = ctk.CTkButton(self.prod_frame,text = 'Update Inventory',command = lambda : update_quantity(self,self.product_to_be_updated[0],category))
                self.change_quant_btn.place(relx = 0.5,rely = 0.3,anchor = ctk.CENTER)
                ctk.CTkLabel(self.prod_frame,text = f'Product Price : {self.product_to_be_updated[0][3]}',font = ("Garamond Bold",15),text_color = 'white').place(relx = 0.2,rely = 0.5,anchor =ctk.CENTER)
                ctk.CTkLabel(self.prod_frame,text = f'Category : {category}',font = ("Garamond Bold",15),text_color = 'white').place(relx = 0.2,rely = 0.7,anchor =ctk.CENTER)
            else :
                messagebox.showerror("Invalid data","enter valid product id".title())

        def display_inventory(self):
            self.display_tables_in_sep_window = ctk.CTkButton(self.inv_tab,text = 'Products table',command = lambda : display_table(self))
            self.display_tables_in_sep_window.pack(padx = 20,pady = 20)
            self.in_frame = ctk.CTkFrame(self.inv_tab,fg_color = '#8E44AD')
            self.in_frame.pack(fill = 'both')
            self.prod_frame = None
            ctk.CTkLabel(self.in_frame,text = 'Enter Product Id').place(relx = 0.3,rely = 0.4,anchor = ctk.CENTER)
            self.product_id = ctk.CTkEntry(self.in_frame,placeholder_text = 'Product Id')
            self.product_id.place(relx = 0.5, rely = 0.4, anchor = ctk.CENTER)
            self.load_btn = ctk.CTkButton(self.in_frame,text = 'Ok',command = lambda : valid(self,self.product_id.get()))
            self.load_btn.place(relx = 0.7,rely = 0.4,anchor = ctk.CENTER)
            
        def display_orders(self):
            self.flag = False

        def display_emp(self):
                self.emp_tab = ctk.CTk()
                self.emp_tab.title('Inventory Table')
                self.emp_tab.geometry('800x650')
                self.main_fme = ctk.CTkFrame(self.tab_win,fg_color = '#8E44AD')
                self.main_fme.pack(fill = 'both',expand = True)
                self.emp_table = ttk.Treeview(self.main.fme,columns = ('cid','c_prod','c_quant','c_price'),show = 'headings')
                self.emp_table.heading('cid',text='Employee ID')
                self.emp_table.heading('c_prod',text='Employee Name')
                self.emp_table.heading('c_quant',text='username')
                self.emp_table.heading('c_price',text = 'password')
                self.emp_table.pack(pady = 10)
                emp_info = self.db_cursor.fetch_results("")
                self.emp_tab.mainloop()
    
        def show_p(self):
                if self.n%2 == 0:
                    self.pass_ent.configure(show = '')
                    self.cpass_ent.configure(show = '')
                    self.n+=1
                else:
                    self.pass_ent.configure(show = '*')
                    self.cpass_ent.configure(show = '*')
                    self.n+=1

        def val(self):
                if self.pass_ent.get() == self.cpass_ent.get():
                    u_n = len(self.db_cursor.fetch_results("SELECT * FROM users WHERE username = %s;",(self.user_ent.get())))
                    if u_n == 0 :
                        self.db_cursor.execute_query("INSERT INTO users(username,password,role,u_name,age) VALUES (%s,%s,'employee',%s,%s);",(self.user_ent.get(),self.pass_ent.get(),self.emp_name_ent.get(),self.spin_emp.get()))
                        messagebox.showerror('Success',"Employee registration successful".title())             
                    else:
                        print(len(self.db_cursor.fetch_results("SELECT * FROM users WHERE username = %s;",self.user_ent.get())))
                        messagebox.showerror("Oops!!","Username already exists")
                else:
                    messagebox.showerror("Oops!!","Try Again")

        def display_staff(self):
            # self.emp_table = ttk.Treeview(self.staff_tab,columns = ('cid','c_prod','c_quant','c_price'),show = 'headings')
            # self.emp_table.heading('cid',text='Employee ID')
            # self.emp_table.heading('c_prod',text='Employee Name')
            # self.emp_table.heading('c_quant',text='username')
            # self.emp_table.heading('c_price',text = 'password')
            # self.emp_table.pack(pady = 10)
            self.win = None
            self.emp_list = ctk.CTkButton(self.staff_tab,text = 'Employee Info')
            self.emp_list.pack(padx = 20,pady = 20)
            self.main_f = ctk.CTkFrame(self.staff_tab,fg_color='#D2B4DE')
            self.main_f.pack(fill='both',expand = True)
            self.emp_name_lb = ctk.CTkLabel(self.main_f,text = 'Enter Employee Name : ')
            self.emp_name_lb.place(relx = 0.2,rely = 0.2, anchor=ctk.CENTER)
            self.emp_name_ent = ctk.CTkEntry(self.main_f,placeholder_text  = "Full Name")
            self.emp_name_ent.place(relx = 0.6,rely = 0.2,anchor =ctk.CENTER)
            self.emp_age_lb = ctk.CTkLabel(self.main_f,text = 'Age : ')
            self.emp_age_lb.place(relx = 0.2,rely = 0.3, anchor=ctk.CENTER)
            self.spin_emp = FloatSpinbox(self.main_f,step_size= 1,to_value = 50)
            self.spin_emp.place(relx = 0.4,rely  =0.3,anchor = ctk.CENTER)
            self.user_lb = ctk.CTkLabel(self.main_f,text = 'Username: ')
            self.user_lb.place(relx = 0.2,rely = 0.4, anchor=ctk.CENTER)
            self.user_ent = ctk.CTkEntry(self.main_f)
            self.user_ent.place(relx = 0.6,rely = 0.4,anchor =ctk.CENTER)
            self.pass_lb = ctk.CTkLabel(self.main_f,text = 'Set Password : ')
            self.pass_lb.place(relx = 0.2,rely = 0.5, anchor=ctk.CENTER)
            self.pass_ent = ctk.CTkEntry(self.main_f,show = '*')
            self.pass_ent.place(relx = 0.6,rely = 0.5,anchor =ctk.CENTER)
            self.c_pass_lb = ctk.CTkLabel(self.main_f,text = 'Confirm Password')
            self.c_pass_lb.place(relx = 0.2,rely = 0.6, anchor=ctk.CENTER)
            self.cpass_ent = ctk.CTkEntry(self.main_f,show = '*')
            self.cpass_ent.place(relx = 0.6,rely = 0.6,anchor =ctk.CENTER)
            self.n = 0
            self.show_pass = ctk.CTkButton(self.main_f,text = 'Show',command = lambda : show_p(self))
            self.show_pass.place(relx = 0.9,rely = 0.6,anchor =ctk.CENTER)
            self.reg_button = ctk.CTkButton(self.main_f,text = 'Register',command = lambda : val(self))
            self.reg_button.place(relx= 0.5,rely  = 0.7,ancho = ctk.CENTER)

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
            
            cake_info = self.db_cursor.fetch_results("Select cake_id,cake_name,cake_quantity,cake_price FROM cakes;")
            pastry_info = self.db_cursor.fetch_results("Select pastry_id,pastry_name,pastry_quantity,pastry_price FROM pastries;")
            bread_info = self.db_cursor.fetch_results("Select bread_id,bread_name,bread_quantity,bread_price FROM breads;")

            for i in range(0,len(cake_info)):
                data = cake_info[len(cake_info)-1-i]
                self.cake_table.insert(parent='',index = 0, values = data)
            for i in range(0,len(pastry_info)):
                data = pastry_info[len(pastry_info)-1-i]
                self.pastry_table.insert(parent='',index = 0, values = data)
            for i in range(0,len(bread_info)):
                data = bread_info[len(bread_info)-1-i]
                self.bread_table.insert(parent='',index = 0, values = data)
            
        def display_products(self):
            self.flag = False
            self.refresh_btn = ctk.CTkButton(self.product_tab,text = 'Refresh',command = lambda : insert_values(self)) 
            self.refresh_btn.pack(padx = 10,pady = 10)
            self.main_fm = ctk.CTkScrollableFrame(self.product_tab,fg_color = '#8E44AD')
            self.main_fm.pack(fill = 'both',expand = True)
            self.cake_table = ttk.Treeview(self.main_fm,columns = ('cid','c_prod','c_quant','c_price'),show = 'headings')
            self.cake_table.heading('cid',text='ID')
            self.cake_table.heading('c_prod',text='Cake Name')
            self.cake_table.heading('c_quant',text='Quantity')
            self.cake_table.heading('c_price',text = 'Price')
            self.cake_table.pack(pady = 10)

            self.pastry_table = ttk.Treeview(self.main_fm,columns = ('cid','c_prod','c_quant','c_price'),show = 'headings')
            self.pastry_table.heading('cid',text='PaID')
            self.pastry_table.heading('c_prod',text='Pastry Name')
            self.pastry_table.heading('c_quant',text='Quantity')
            self.pastry_table.heading('c_price',text = 'Price')
            self.pastry_table.pack(pady =10)

            self.bread_table = ttk.Treeview(self.main_fm,columns = ('cid','c_prod','c_quant','c_price'),show = 'headings')
            self.bread_table.heading('cid',text='BID')
            self.bread_table.heading('c_prod',text='Bread Name')
            self.bread_table.heading('c_quant',text='Quantity')
            self.pastry_table.heading('c_price',text = 'Price')
            self.bread_table.pack(pady = 10)

            for i in range(0,3):
                List = self.inv_info[i]
                c=0
                for j in range(0,len(List)):
                    data = List[len(List)-1-c]
                    c+=1
                    if i==0:
                        self.cake_table.insert(parent='',index = 0, values = data)
                    elif i == 1:
                        self.pastry_table.insert(parent='',index = 0, values = data)
                    elif i==2:
                        self.bread_table.insert(parent='',index = 0, values = data)


        def display_admin_interface(self):
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
            self.inv_tab = self.Tab.add('Inventory')
            self.order_tab = self.Tab.add('Orders')
            self.staff_tab = self.Tab.add('Staff')
            self.product_tab = self.Tab.add('Products')
            self.flag = False
            self.db_cursor = Database('localhost',3306,'root','716807','bakery')
            # fetch relevant data here
            # inv 
            self.inv_info = []
            self.inv_info.append(self.db_cursor.fetch_results("SELECT cake_id,cake_name,cake_quantity,cake_price FROM cakes;"))
            self.inv_info.append(self.db_cursor.fetch_results("SELECT pastry_id,pastry_name,pastry_quantity,pastry_price FROM pastries;"))
            self.inv_info.append(self.db_cursor.fetch_results("SELECT bread_id,bread_name,bread_quantity,bread_price FROM breads;"))
            display_inventory(self)
            display_orders(self)
            display_staff(self)
            display_products(self)

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


    


