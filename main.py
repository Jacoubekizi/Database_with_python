from tkinter import *
from tkinter import ttk
# from .validate import validate_number
import os
from data_base import Database
from tkinter import messagebox
db = Database('employee.db')

# انشاء نافذة

root = Tk()
root.title('Employee Management System')
# تحديد المساحة(+100+100 هو مركز تشغيل البرنامج على شاشة الحاسوب)
root.geometry('1250x615+100+100')
# root.resizable(من الاسفل , من اليسار)من اجل ايقاف خاصية التكبير للبرنامج 
# root.resizable(False, False)
root.configure(bg='#2c3e50')


name = StringVar()
age = IntVar()
job = StringVar()
gender = StringVar()
email = StringVar()
phone = IntVar()

script_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(script_dir, 'logo.jpg')
lbl_logo = Label(root, image=PhotoImage(file=logo_path), bg='#2c3e50')
lbl_logo.place(x=80, y=520)

# #--------------------Enties Frame
entries_frame = Frame(root, bg='#2c3e50')
entries_frame.place(x=1, y=1, width=360,height='510')
title = Label(entries_frame, text='Employee Comapany', font=('Calibri', 18,'bold'),bg='#2c3e50', fg='white')
title.place(x=10, y=1)

lblName = Label(entries_frame, text='Name', font=('Calibri', 16),bg='#2c3e50', fg='white')
lblName.place(x=10, y=50)
txtName = Entry(entries_frame, textvariable=name, width=20, font=('Calibri', 16))
txtName.place(x=120,y=50)

lblJob = Label(entries_frame, text='Job', font=('Calibri', 16),bg='#2c3e50', fg='white')
lblJob.place(x=10, y=90)
txtJob = Entry(entries_frame, textvariable=job, width=20, font=('Calibri', 16))
txtJob.place(x=120,y=90)

lblGender = Label(entries_frame, text='Gender', font=('Calibri', 16),bg='#2c3e50', fg='white')
lblGender.place(x=10, y=130)
# ينشأ حقل من اجل الاختيار من متعدد
comboGender = ttk.Combobox(entries_frame, textvariable=gender, width=18, font=('Calibri', 16), state='readonly')
comboGender['values'] = ('Male', 'Female')
comboGender.place(x=120, y=130)

lblAge = Label(entries_frame, text='Age', font=('Calibri', 16),bg='#2c3e50', fg='white')
lblAge.place(x=10, y=170)
txtAge = Entry(entries_frame, textvariable=age, width=20, font=('Calibri', 16))
txtAge.place(x=120,y=170)
# txtAge.config(validate="key", validatecommand=(validate_number, "%d", "%i", "%P", "%s"))

lblEmail = Label(entries_frame, text='Email', font=('Calibri', 16),bg='#2c3e50', fg='white')
lblEmail.place(x=10, y=210)
txtEmail = Entry(entries_frame, textvariable=email, width=20, font=('Calibri', 16))
txtEmail.place(x=120,y=210)

lblPhonenumber = Label(entries_frame, text='Mobile', font=('Calibri', 16),bg='#2c3e50', fg='white')
lblPhonenumber.place(x=10, y=250)
txtPhonenumber = Entry(entries_frame, textvariable=phone, width=20, font=('Calibri', 16))
txtPhonenumber.place(x=120,y=250)

lblAddress= Label(entries_frame, text='Address :', font=('Calibri', 16),bg='#2c3e50', fg='white')
lblAddress.place(x=10, y=290)
txtAddress = Text(entries_frame, width=30, height=2, font=('Calibri', 16))
txtAddress.place(x=10, y=330)

# ===============Define

def hide():
    root.geometry("360x515")
def show():
    root.geometry("1250x615")

btn_hide = Button(entries_frame, text='HIDE',bg='white', bd=1, relief=SOLID, command=hide, cursor='hand2')
btn_hide.place(x=270, y=10)
btn_show = Button(entries_frame, text='SHOW',bg='white', bd=1, relief=SOLID, command=show, cursor='hand2')
btn_show.place(x=310, y=10)

def getData(event):
#    tree_view جلب البيانات من ال 
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data['values']
    name.set(row[1])
    job.set(row[2])
    gender.set(row[3])
    age.set(row[4])
    email.set(row[5])
    phone.set(row[6])
    txtAddress.delete(1.0, END)
    txtAddress.insert(END, row[7])

def displayAll():
    #tree_view حذفلي وبعدين جبلي كلشي داخل ال 
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)\

def add_employee():
    if txtName.get() == '' or txtAge.get() == '' or txtJob.get() == '' or txtAddress.get(1.0,END) == '' or txtEmail.get() == '' or txtPhonenumber.get() == '' or comboGender.get() == '':
        messagebox.showerror("Error", "please fill all the entry")
        return
    db.insert(
        txtName.get(),
        txtAge.get(),
        txtJob.get(),
        txtEmail.get(),
        comboGender.get(),
        txtPhonenumber.get(),
        txtAddress.get(1.0,END)
    )
    messagebox.showinfo("Success", "Added New Employee")
    Clear()
    displayAll()

def Clear():
    name.set("")
    age.set("")
    job.set("")
    gender.set("")
    email.set("")
    phone.set("")
    txtAddress.delete(1.0,END)
    get_Employee()

def get_Employee():
    id = row[0]
    data = db.get_employee(id)

def Delete():
    id = row[0]
    db.remove(id)
    Clear()
    displayAll()

def update_employee():
    id = row[0]
    db.update(
        id,
        txtName.get(),
        txtAge.get(),
        txtJob.get(),
        txtEmail.get(),
        comboGender.get(),
        txtPhonenumber.get(),
        txtAddress.get(1.0,END)
    )
    Clear()
    displayAll()

# -------------------- Buttons Frame
btn_frame = Frame(entries_frame, bg='#2c3e50')
btn_frame.place(x=10, y=400, width=335, height=100)

btn_add = Button(btn_frame,
                text='Add Details',
                width=14,
                height=1,
                font=('Calibri', 16),
                fg='white',
                bg='#16a085',
                bd=0,
                cursor='hand2',
                command=add_employee
                ).place(x=4, y=5)

btn_edit = Button(btn_frame,
                text='Update Details',
                width=14,
                height=1,
                font=('Calibri', 16),
                fg='white',
                bg='#2980b9',
                bd=0,
                cursor='hand2',
                command=update_employee
                ).place(x=4, y=50)

btn_clear = Button(btn_frame,
                text='Clear Details',
                width=14,
                height=1,
                font=('Calibri', 16),
                fg='white',
                bg='#f39c12',
                bd=0,
                cursor='hand2',
                command=Clear
                ).place(x=170, y=50)

btn_delete = Button(btn_frame,
                text='Delete Details',
                width=14,
                height=1,
                font=('Calibri', 16),
                fg='white',
                bg='#c0392b',
                bd=0,
                cursor='hand2',
                command=Delete
                ).place(x=170, y=5)


# -----------------------------Table Frame
tree_frame =Frame(root, background='white')
tree_frame.place(x=365, y=1, width=875, height=610)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 13), rowheight=50)
style.configure("mystyle.Treeview.Heading", font=('Calibri', 13))

tv = ttk.Treeview(tree_frame, columns=(1,2,3,4,5,6,7,8), style='mystyle.Treeview')
tv.heading("1", text='ID')
tv.column("1", width=40)
tv.heading("2", text='Name')
tv.column("2", width=140)
tv.heading("3", text='Age')
tv.column("3", width=50)

tv.heading("4", text='Job')
tv.column("4", width=120)

tv.heading("5", text='Email')
tv.column("5", width=150) 

tv.heading("6", text='Gender')
tv.column("6", width=90)

tv.heading("7", text='Contact')
tv.column("7", width=150)

tv.heading("8", text='Address')
tv.column("8", width=150)
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.place(x=1, y=1, height=610, width=875)

# entries_frame.pack(fill=X, expand=True)
displayAll()
# امر تشغيل النافذة
root.mainloop()