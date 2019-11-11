from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from PIL import ImageTk, Image


try:
    con = mysql.connector.connect(host='localhost', user='root', password='Rudrapun96@', database=' softwarica ')
    cur = con.cursor()
except mysql.connector.Error as e:
    print(e)

''' Default username => admin and default password => admin is set to open the login system '''

class Student:

    """ Login System Interface """
    def __init__(self, root):
        self.root = root
        root.protocol('WM_DELETE_WINDOW', self.CloseWindow)

        self.image = Image.open("z..jpg")
        self.photo = ImageTk.PhotoImage(self.image)
        self.ImageLabel = Label(self.root, image=self.photo)
        self.ImageLabel.place(x=170, y=70)

        self.LoginLabel = Label(self.root, text='Login System', font=('Times New Roman', 20, 'bold'), bg='azure2',
                                fg='OrangeRed2')
        self.LoginLabel.place(x=150, y=20)

        self.UserEntry = Entry(self.root, fg='grey')
        self.UserEntry.place(x=130, y=230, width=200, height=25)
        self.UserEntry.insert(0, 'Enter your name ...')
        self.UserEntry.bind('<FocusIn>', self.on_entry_click)
        self.UserEntry.bind('<FocusOut>', self.on_focusout)

        self.PasswordEntry = Entry(self.root, fg='grey')
        self.PasswordEntry.place(x=130, y=270, width=200, height=25)
        self.PasswordEntry.insert(0, 'Enter your password ...')
        self.PasswordEntry.bind('<FocusIn>', self.on_entry_click1)
        self.PasswordEntry.bind('<FocusOut>', self.on_focusout1)

        self.label = Label(self.root, text='Forgot Password?', bg='azure2')
        self.label.place(x=190, y=300)

        self.LoginBtn = Button(self.root, text='LOGIN', command=self.login, width=10, height=2, bg='orangered')
        self.LoginBtn.place(x=190, y=350)


    def login(self):
        username = self.UserEntry.get()
        password = self.PasswordEntry.get()
        if username == str('admin') and password == str('admin'):
            self.main_window()
        else:
            messagebox.showerror('Login Systems', 'Too Bad, invalid login detail')
            self.UserEntry.delete(0, END)
            self.PasswordEntry.delete(0, END)



    def on_entry_click(self, event):
        if self.UserEntry.get() == 'Enter your name ...':
            self.UserEntry.delete(0, 'end')
            self.UserEntry.insert(0, '')
            self.UserEntry.config(fg='black')

    def on_focusout(self, event):
        if self.UserEntry.get() == '':
            self.UserEntry.insert(0, 'Enter your name ...')
            self.UserEntry.config(fg='grey')

    def on_entry_click1(self, event):
        if self.PasswordEntry.get() == 'Enter your password ...':
            self.PasswordEntry.delete(0, 'end')
            self.PasswordEntry.insert(0, '')
            self.PasswordEntry.config(fg='black')
            self.PasswordEntry.config(show='*')

    def on_focusout1(self, event):
        if self.PasswordEntry.get() == '':
            self.PasswordEntry.insert(0, 'Enter your password ...')
            self.PasswordEntry.config(fg='grey')




    def main_window(self):
        student.back_function()
        self.scree = Toplevel(root)
        self.scree.protocol('WM_DELETE_WINDOW', self.CloseWindow)
        self.scree.title('Student Information')
        self.scree.configure(bg='azure2')
        self.scree.geometry('500x500+600+50')

        self.image1 = Image.open("h.jpg")
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.ImageLabel1 = Label(self.scree,image=self.photo1)
        self.ImageLabel1.place(x=120, y=70)

        self.Window_Frame = Frame(self.scree, bg='azure2')
        self.Window_Frame.pack()

        self.WindowLabel = Label(self.Window_Frame, text='Welcome to Student database system', bg='azure2',
                                 font=('Times New Roman', 20, 'bold'), fg='OrangeRed2')
        self.WindowLabel.grid(row=0, column=1, pady=20)

        self.btn_frame = Frame(self.scree, bd=4, bg='azure2', relief=RIDGE)
        self.btn_frame.place(x=70, y=290, width=350, height=170)

        self.SaveBtn = Button(self.btn_frame, text='Save Students Detail', bg='tan2',
                              command=self.save_student, width=20, height=2)
        self.SaveBtn.place(x=10, y=20)

        self.SearchBtn = Button(self.btn_frame, text='Search Students Detail', bg='tan2',
                                command=self.search_details, width=20, height=2)
        self.SearchBtn.place(x=180, y=20)

        self.SortStudent = Button(self.btn_frame, text='Sort Students Detail', command=self.sort_details, bg='tan2',
                                  width=20, height=2)
        self.SortStudent.place(x=10, y=90)

        self.CloseBtn = Button(self.btn_frame, text='Close Window', bg='tan2',
                               command=self.CloseWindow, width=20, height=2)
        self.CloseBtn.place(x=180, y=90)

    def CloseWindow(self):
        msg_box = messagebox.askquestion('Exit application', 'Are you sure you want to exit')
        if msg_box == 'yes':
            self.root.destroy()


    def update(self):

        """ Update query """

        first_name = self.firsten.get()
        last_name = self.lasten.get()
        student_id = self.iden.get()
        degree = self.Degreeen.get()

        gender = self.GenderCombo.get()
        address = self.AddressEntry.get()
        contact = self.contactentry.get()

        if first_name == '' or last_name == '' or student_id == '' or degree == ' ' or gender == ''\
                or address == '' or contact == '':
            messagebox.showerror('Error', 'Please fill all inputs')
        else:
            query = 'update student_table1 set First_Name=%s, Last_Name=%s, Degree=%s,' \
                    'Gender=%s, Address=%s, Contact_no=%s where Student_id=%s'
            values = (first_name, last_name, degree, gender, address, contact, int(student_id))
            cur.execute(query, values)
            con.commit()
            self.show()
            self.clear()



    def delete(self):

        """ delete query """
        selected_item = self.student_table.selection()
        self.student_table.delete(selected_item)

        roll = self.iden.get()
        query = 'delete from student_table1 where Student_id=%s'
        values = (roll,)

        cur.execute(query, values)
        con.commit()
        self.clear()

    def search_details(self):
        search.raise_me()
        self.back_main()

    def back_main(self):
        self.scree.withdraw()

    def raise_main(self):
        self.scree.deiconify()

    def sort_details(self):
        sort.raise_me()

    def back_function(self):
        self.root.withdraw()

    def raise_me(self):
        self.root.tkraise()

    def clear(self):
        self.firsten.delete(0, END)
        self.lasten.delete(0, END)
        self.iden.delete(0, END)
        self.Degreeen.delete(0, END)
        self.GenderCombo.delete(0, END)
        self.AddressEntry.delete(0, END)
        self.contactentry.delete(0, END)

    def add_info(self):

        """ add query """
        first_name = self.firsten.get()
        last_name = self.lasten.get()
        student_id = self.iden.get()
        degree = self.Degreeen.get()

        gender = self.GenderCombo.get()
        address = self.AddressEntry.get()
        contact = self.contactentry.get()

        if first_name == '' or last_name == ''or student_id == '' or degree == '' or gender == ''\
                or address == '' or contact == '':
            messagebox.showerror('Error', 'Please fill all entries ')

        elif len(contact) < 10:
            messagebox.showerror('Error', 'The Length of contact number is less than 10 digits')
        elif len(contact) > 10:
            messagebox.showerror('Error', 'The Length of contact number is more than 10 digits')

        else:

            query = 'insert into student_table1 values(%s,%s,%s,%s,%s,%s,%s)'
            values = (first_name, last_name, student_id, degree, gender, address, contact)
            cur.execute(query, values)
            con.commit()
            self.show()
            self.clear()
            messagebox.showinfo('sucess', 'Added sucessfully')


    def show(self):

        """ to get all data from mysql """

        query = 'select * from student_table1'
        cur.execute(query)
        rows = cur.fetchall()

        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())

        for row in rows:
            self.student_table.insert('', END, values=row)

    def pointer(self, event):
        point = self.student_table.focus()
        content = self.student_table.item(point)
        row = content['values']
        self.clear()
        self.firsten.insert(1, row[0])
        self.lasten.insert(0, row[1])
        self.iden.insert(0, row[2])
        self.Degreeen.insert(0, row[3])
        self.GenderCombo.insert(0, row[4])
        self.AddressEntry.insert(0, row[5])
        self.contactentry.insert(0, row[6])


    def save_student(self):
        self.screen = Toplevel(root)
        self.screen.protocol('WM_DELETE_WINDOW', self.CloseWindow)
        self.screen.title('Student Information')
        self.screen.configure(bg='azure2')
        self.screen.geometry('640x480+550+50')

# ----------------------Frame----------------

        self.EntryFrame = Frame(self.screen, bg='azure2', bd=2, relief=RIDGE)
        self.EntryFrame.place(x=130, y=10, width=330, height=230)

        self.photo_frame = Frame(self.screen, bg='azure2', bd=2, relief=GROOVE)
        self.photo_frame.place(x=490, y=10, width=120, height=120)

        self.image2 = Image.open("1.jpg")
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.ImageLabel2 = Label(self.screen, image=self.photo2)
        self.ImageLabel2.place(x=490, y=10)

        self.btn_frame = Frame(self.screen, bg='azure2', bd=2, relief=GROOVE)
        self.btn_frame.place(x=10, y=30, width=100, height=350)

# -----------------------Label--------------------
        self.firstframe = Label(self.EntryFrame, text='First Name', bg='azure2')
        self.firstframe.grid(row=0, column=1, padx=5, pady=5)

        self.lnamef = Label(self.EntryFrame, text='Last Name', bg='azure2')
        self.lnamef.grid(row=1, column=1, padx=5, pady=5)

        self.lblAdd = Label(self.EntryFrame, text="Student_id", bg='azure2')
        self.lblAdd.grid(row=2, column=1, padx=5, pady=5)

        self.lblage = Label(self.EntryFrame, text='Degree', bg='azure2')
        self.lblage.grid(row=3, column=1, padx=5, pady=5)

        self.GenderLabel = Label(self.EntryFrame, text='Gender', bg='azure2')
        self.GenderLabel.grid(row=4, column=1, padx=5, pady=8)

        self.MarkLabel = Label(self.EntryFrame, text='Address', bg='azure2')
        self.MarkLabel.grid(row=5, column=1, padx=5, pady=5)

        self.Contact = Label(self.EntryFrame, text='Contact no', bg='azure2')
        self.Contact.grid(row=6, column=1, padx=5, pady=5)


# ----------------------Entry----------------------------
        self.firsten = Entry(self.EntryFrame, width=35)
        self.firsten.grid(row=0, column=2, padx=5, pady=5)

        self.lasten = Entry(self.EntryFrame, width=35)
        self.lasten.grid(row=1, column=2, padx=5, pady=5)

        self.iden = Entry(self.EntryFrame, width=35)
        self.iden.grid(row=2, column=2, padx=5, pady=5)

        self.Degreeen = ttk.Combobox(self.EntryFrame, width=32)
        self.Degreeen['values'] = (' Ethical Hacking','Computing')
        self.Degreeen.grid(row=3, column=2, padx=5, pady=5)
        self.Degreeen.set('Ethical Hacking')

        self.GenderCombo = ttk.Combobox(self.EntryFrame, width=32)
        self.GenderCombo['values'] = (' Male', ' Female')
        self.GenderCombo.grid(row=4, column=2, padx=5, pady=5)
        self.GenderCombo.set('Male')

        self.AddressEntry = Entry(self.EntryFrame, width=35)
        self.AddressEntry.grid(row=5, column=2, padx=5, pady=5)

        self.contactentry = Entry(self.EntryFrame, width=35)
        self.contactentry.grid(row=6, column=2, padx=5, pady=5)

# ------------------------Button----------------------
        self.optionlbl = Label(self.screen, text='Option', font=('arial', 10), bg='azure2')
        self.optionlbl.place(x=30, y=8)

        self.AddBtn = Button(self.btn_frame, text='Add', command=self.add_info, width=10, height=2)
        self.AddBtn.place(x=8, y=15)

        self.UpdateBtn = Button(self.btn_frame, text='Update',command=self.update, width=10, height=2)
        self.UpdateBtn.place(x=8, y=80)

        self.DeleteBtn = Button(self.btn_frame, text='Delete', command=self.delete, width=10, height=2)
        self.DeleteBtn.place(x=8, y=145)

        self.ClearBtn = Button(self.btn_frame, text='Clear', command=self.clear, width=10, height=2)
        self.ClearBtn.place(x=8, y=210)

        self.back_button = Button(self.btn_frame, text='Back', command=self.back_me, width=10, height=2)
        self.back_button.place(x=8, y=270)

# ------------------ Table frame -----------------
        self.table_frame = Frame(self.screen, bd=4, relief=RIDGE)
        self.table_frame.place(x=130, y=250, width=500, height=230)

# -------scrollbar--------
        self.scroll_x = Scrollbar(self.table_frame, orient=HORIZONTAL)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)
        self.scroll_y.pack(side=RIGHT, fill=Y)


# --------------- --------Table-----------------------------
        self.student_table = ttk.Treeview(self.table_frame, columns=('First_Name', 'Last_Name', 'Student_id', 'Degree', 'Gender', 'Address',
                                                                     'Contact_no'),
                                          xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        self.student_table.heading('First_Name', text=' First_Name')
        self.student_table.heading('Last_Name', text='Last_Name')
        self.student_table.heading('Student_id', text='Student_id')
        self.student_table.heading('Degree', text='Degree')
        self.student_table.heading('Gender', text='Gender')
        self.student_table.heading('Address', text='Address')
        self.student_table.heading('Contact_no', text='Contact_no')

        self.student_table.pack(fill=BOTH, expand=True)

        self.student_table.column('First_Name', width=130)
        self.student_table.column('Last_Name', width=130)
        self.student_table.column('Student_id', width=120)
        self.student_table.column('Degree', width=150)
        self.student_table.column('Gender', width=100)

        self.student_table.column('Address', width=100)
        self.student_table.column('Contact_no', width=100)
        self.show()

        self.student_table['show'] = 'headings'
        self.student_table.bind('<ButtonRelease-1>', self.pointer)
        self.scroll_x.config(command=self.student_table.xview)
        self.scroll_y.config(command=self.student_table.yview)

    def back_function1(self):
        self.screen.withdraw()

    def back_me(self):
        self.back_function1()
        student.raise_main()

    def raise_me1(self):
        self.screen.deiconify()



class Search:
    """ Class name Search along with its interface """
    def __init__(self,root):
        self.root = root

        self.screen1 = Toplevel(root)
        self.screen1.protocol('WM_DELETE_WINDOW', self.CloseWindow)

        self.screen1.title('Search Student Details')
        self.screen1.geometry('580x500+700+100')
        self.screen1.configure(bg='azure2')

        self.detail_frame = Frame(self.screen1, bg='azure2', bd=4, relief=RIDGE)
        self.detail_frame.place(x=20, y=10, width=530, height=100)

        self.lblsearch = Label(self.detail_frame, text='Search By', bg='azure2', font=('arial', 10))
        self.lblsearch.grid(row=0, column=0, pady=5)

        self.searchcombo = ttk.Combobox(self.detail_frame, font=('arial', 10), state='readonly')
        self.searchcombo['values'] = ('First_Name', 'Last_Name', 'Student_id', 'Degree', 'Address')
        self.searchcombo.grid(row=0, column=1, pady=10, padx=20)
        self.searchcombo.set('First_Name')

        self.searchlbl = Label(self.detail_frame, text='Search text',bg='azure2', font=('arial', 10))
        self.searchlbl.grid(row=1, column=0, pady=5)

        self.searchentry = Entry(self.detail_frame, width=27)
        self.searchentry.grid(row=1, column=1, pady=10, padx=10)

        self.searchbtn = Button(self.detail_frame, text='Search', command=self.show1, font=('arial', 12), width=10)
        self.searchbtn.grid(row=0, column=3, pady=10, padx=10)

        self.back = Button(self.detail_frame, text='Back', command=self.back_me, font=('arial', 12), width=10)
        self.back.grid(row=0, column=4, pady=10, padx=10)

        self.table_frame1 = Frame(self.screen1, bd=4, relief=RIDGE)
        self.table_frame1.place(x=8, y=130, width=570, height=375)

        # -------scrollbar--------

        self.scroll_x = Scrollbar(self.table_frame1, orient=HORIZONTAL)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y = Scrollbar(self.table_frame1, orient=VERTICAL)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        # --------------Table---
        self.student_table = ttk.Treeview(self.table_frame1, columns=('First_Name', 'Last_Name', 'Student_id',
                                                                      'Degree', 'Gender', 'Address', 'Contact_no'),
                                          xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        self.student_table.heading('First_Name', text=' First_Name')
        self.student_table.heading('Last_Name', text='Last_Name')
        self.student_table.heading('Student_id', text='Student_id')
        self.student_table.heading('Degree', text='Degree')
        self.student_table.heading('Gender', text='Gender')
        self.student_table.heading('Address', text='Address')
        self.student_table.heading('Contact_no', text='Contact_no')

        self.student_table.pack(fill=BOTH, expand=True)

        self.student_table.column('First_Name', width=130)
        self.student_table.column('Last_Name', width=130)
        self.student_table.column('Student_id', width=130)
        self.student_table.column('Degree', width=150)
        self.student_table.column('Gender', width=120)

        self.student_table.column('Address', width=120)
        self.student_table.column('Contact_no', width=120)
        self.show2()

        self.student_table['show'] = 'headings'
        self.student_table.bind('<ButtonRelease-1>')
        self.scroll_x.config(command=self.student_table.xview)
        self.scroll_y.config(command=self.student_table.yview)

    def show2(self):
        query = 'select * from student_table1'
        cur.execute(query)
        rows = cur.fetchall()

        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())

        for row in rows:
            self.student_table.insert('', END, values=row)

    def CloseWindow(self):
        msg_box = messagebox.askquestion('Exit application', 'Are you sure you want to exit')
        if msg_box == 'yes':
            self.root.destroy()

    def show1(self):
        query = 'select * from student_table1'
        cur.execute(query)
        rows = cur.fetchall()
        list_a = self.search_item(rows)

        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
        for abc in list_a:
            self.student_table.insert('', END, value=abc)


    def back_function(self):
        self.screen1.withdraw()

    def back_me(self):
        self.back_function()
        student.raise_main()

    def raise_me(self):
        self.screen1.deiconify()

    def search_item(self, rows):
        """ linear search algorithm """

        a2 = self.searchentry.get()
        b=self.searchcombo.get()
        if a2 == ''or b == '':
            messagebox.showerror('Error','Please fill all entries')
        else:
            if b == 'First_Name':
                column_index = 0
            elif b == 'Last_Name':
                column_index = 1
            elif b == 'Student_id':
                column_index = 2
                a2=int(self.searchentry.get())
            elif b == 'Degree':
                column_index = 3
            elif b == 'Gender':
                column_index = 4
            elif b == 'Address':
                column_index = 5
            else:
                column_index = 6
                a2 = int(self.searchentry.get())


            found_list = []
            for xyz in rows:
                if a2 == xyz[column_index]:
                    found_list.append(xyz)
            return found_list

class Sort:

    """ Sort class along with interface """
    def __init__(self, root):
        self.root = root

        self.screen2 = Toplevel(root)
        self.screen2.protocol('WM_DELETE_WINDOW', self.CloseWindow)
        self.screen2.title('Sort Student Details')
        self.screen2.geometry('500x500+550+50')
        self.screen2.configure(bg='azure2')

        self.detail_frame = Frame(self.screen2, bg='azure2', bd=4, relief=RIDGE)
        self.detail_frame.place(x=70, y=10, width=400, height=100)

        self.LabelSort = Label(self.detail_frame, text='Sort By', bg='azure2', font=('arial', 10))
        self.LabelSort.place(x=30, y=25)

        self.sortCombo = ttk.Combobox(self.detail_frame, font=('arial', 10))
        self.sortCombo['values'] = ('First_Name', 'Last_Name', 'Student_id', 'Degree')
        self.sortCombo.set('First_Name')
        self.sortCombo.place(x=250, y=25,width=100)

        self.sortCombo1 = ttk.Combobox(self.detail_frame, font=('arial', 10))
        self.sortCombo1['values'] = ('Ascending', 'Descending')
        self.sortCombo1.set('Ascending')
        self.sortCombo1.place(x=100, y=25, width=100)

        self.back_btn = Button(self.detail_frame, command=self.back_me, text='Back', font=('arial', 10),
                               width=12, height=1)
        self.back_btn.place(x=250, y=55)

        self.SortButton = Button(self.detail_frame, text='Sort', font=('arial', 10), command=self.sort_i,
                                 width=12, height=1)
        self.SortButton.place(x=100,y=55)

        self.table_frame2 = Frame(self.screen2, bd=4, relief=RIDGE)
        self.table_frame2.place(x=8, y=140, width=490, height=350)

        # -------scrollbar--------

        self.scroll_x = Scrollbar(self.table_frame2, orient=HORIZONTAL)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y = Scrollbar(self.table_frame2, orient=VERTICAL)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        # --------------Table---
        self.student_table = ttk.Treeview(self.table_frame2, columns=('First_Name', 'Last_Name', 'Student_id',
                                                                      'Degree', 'Gender', 'Address', 'Contact_no'),
                                          xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        self.student_table.heading('First_Name', text=' First_Name')
        self.student_table.heading('Last_Name', text='Last_Name')
        self.student_table.heading('Student_id', text='Student_id')
        self.student_table.heading('Degree', text='Degree')
        self.student_table.heading('Gender', text='Gender')
        self.student_table.heading('Address', text='Address')
        self.student_table.heading('Contact_no', text='Contact_no')

        self.student_table.pack(fill=BOTH, expand=True)

        self.student_table.column('First_Name', width=130)
        self.student_table.column('Last_Name', width=130)
        self.student_table.column('Student_id', width=120)
        self.student_table.column('Degree', width=150)
        self.student_table.column('Gender', width=100)

        self.student_table.column('Address', width=100)
        self.student_table.column('Contact_no', width=100)
        self.show()

        self.student_table['show'] = 'headings'
        self.student_table.bind('<ButtonRelease-1>')
        self.scroll_x.config(command=self.student_table.xview)
        self.scroll_y.config(command=self.student_table.yview)

    def show(self):
        query = 'select * from student_table1'
        cur.execute(query)
        rows = cur.fetchall()

        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())

        for row in rows:
            self.student_table.insert('', END, values=row)

    def sort_i(self):
            query = "select * from student_table1"
            cur.execute(query)
            list_a = cur.fetchall()
            table = self.mergesort(list_a)
            if len(list_a) != 0:
                self.student_table.delete(*self.student_table.get_children())
            for a in table:
                self.student_table.insert('', END, values=a)



    def mergesort(self, list_a):
        """ merge sort algorithm """

        if len(list_a) <= 1:
            return list_a
        n = len(list_a)
        mid = n // 2
        left = self.mergesort(list_a[:mid])
        right = self.mergesort(list_a[mid:])
        final = []
        a, b = 0, 0
        SortCombo = self.sortCombo.get()
        SortCombo1 = self.sortCombo1.get()
        if SortCombo == 'First_Name':
            column_index = 0
        elif SortCombo == 'Last_Name':
            column_index = 1
        elif SortCombo == 'Student_id':
            column_index = 2
        elif SortCombo == 'Degree':
            column_index = 3
        elif SortCombo == 'Gender':
            column_index = 4
        elif SortCombo == 'Address':
            column_index = 5
        else:
            column_index = 6

        if SortCombo == '' or SortCombo1 == '':
            messagebox.showerror('Error', 'Please fill the entry box for sorting')
        elif SortCombo1 =='Ascending':
            while a < len(left) and b < len(right):
                if left[a][column_index] <= right[b][column_index]:
                    final.append(left[a])
                    a = a + 1
                else:
                    final.append(right[b])
                    b = b + 1
            final = final + left[a:]
            final = final + right[b:]
            return final

        else:
            while a < len(left) and b < len(right):
                if left[a][column_index] >= right[b][column_index]:
                    final.append(left[a])
                    a = a + 1
                else:
                    final.append(right[b])
                    b = b + 1
            final = final + left[a:]
            final = final + right[b:]
            return final

    def back_function(self):
        self.screen2.withdraw()

    def back_me(self):
        self.back_function()
        student.raise_main()

    def raise_me(self):
        student.back_main()
        self.screen2.deiconify()

    def CloseWindow(self):
        msg_box = messagebox.askquestion('Exit application', 'Are you sure you want to exit')
        if msg_box == 'yes':
            self.root.destroy()

root=Tk()
root.geometry('450x500')
root.title('Student Form')
root.configure(bg='azure2')
student = Student(root)
search = Search(root)
sort = Sort(root)

search.back_function()
sort.back_function()
root.mainloop()