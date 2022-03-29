import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import tkinter.font as tkFont
import sqlite3, time, datetime, random

name_of_db = 'inventory_master.db'
my_conn = sqlite3.connect(name_of_db)
cdb = my_conn.cursor()


def create_table():
    cdb.execute(
        'CREATE TABLE IF NOT EXISTS customer_master('
        'idno INTEGER PRIMARY KEY,'
        'datestamp TEXT, '
        'customer_name TEXT, '
        'address TEXT, '
        'town TEXT, '
        'post_code TEXT, '
        'contact TEXT)')


def show_ID():
    frmList = tk.Tk()
    frmList.title("List of customer")
    width = 665
    height = 500
    screenwidth = frmList.winfo_screenwidth()
    screenheight = frmList.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    frmList.geometry(alignstr)
    frmList.resizable(width=False, height=False)
    customerID = txtID.get()
    txtName.focus_set()
    txtName.insert(INSERT,"Hello")
    data_set = my_conn.execute("SELECT * FROM customer_master WHERE idno=?", (customerID,))
    # btnFullName.grid(columnspan=2, padx=15, pady=15)
    output_data(data_set, frmList)
    clear_form()


def show_Name():
    frmList = tk.Tk()
    frmList.title("List of customer")
    width = 665
    height = 500
    screenwidth = frmList.winfo_screenwidth()
    screenheight = frmList.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    frmList.geometry(alignstr)
    frmList.resizable(width=False, height=False)
    customerName = txtName.get()
    data_set = my_conn.execute("SELECT * FROM customer_master WHERE customer_name like?", (customerName,))
    # btnFullName.grid(columnspan=2, padx=15, pady=15)
    output_data(data_set, frmList)
    clear_form()


def show_Contact():
    frmList = tk.Tk()
    frmList.title("List of customer")
    width = 665
    height = 500
    screenwidth = frmList.winfo_screenwidth()
    screenheight = frmList.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    frmList.geometry(alignstr)
    frmList.resizable(width=False, height=False)
    contact = txtContact.get()
    data_set = my_conn.execute("SELECT * FROM customer_master WHERE contact like?", (contact,))
    # btnFullName.grid(columnspan=2, padx=15, pady=15);2
    output_data(data_set, frmList)
    clear_form()


def update_record():
    with my_conn:
        customer_id = txtID.get()
        customer_name = txtName.get()
        address = txtAddress.get()
        town = txtTown.get()
        post_code = txtPostCode.get()
        contact = txtContact.get()
        cdb.execute("UPDATE customer_master SET customer_name=?, address=?, town=?, post_code=?, contact=? WHERE idno=?",
                    (customer_name, address, town, post_code, contact, customer_id))
        my_conn.commit()
        msg = f'Record Successfully Saved!'
        showinfo(title='Information', message=msg)
    clear_form()


def delete_record():
    with my_conn:
        customer_id = txtID.get()
        cdb.execute("DELETE FROM customer_master WHERE idno=?", (customer_id,))
        my_conn.commit()
        clear_form()


def output_data(data_set, frmList):
    i = 0  # row value inside the loop
    for person in data_set:
        for j in range(len(person)):
            e = Entry(frmList, width=15, fg='black')
            e.grid(row=i, column=j)
            e.insert(END, person[j])
        i = i + 1
    return frmList


def clear_form():
    txtID.delete(0, END)
    txtName.delete(0, END)
    txtAddress.delete(0, END)
    txtTown.delete(0, END)
    txtContact.delete(0, END)
    txtPostCode.delete(0, END)


def btnClose_Command():
    clear_form()
    exit()


create_table()

frmCustomerUpdate = tk.Tk()
frmCustomerUpdate.title("Customer Update")
width = 513
height = 364
screenwidth = frmCustomerUpdate.winfo_screenwidth()
screenheight = frmCustomerUpdate.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
frmCustomerUpdate.geometry(alignstr)
frmCustomerUpdate.resizable(width=False, height=False)

txtID = tk.Entry(frmCustomerUpdate)
txtID["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
txtID["font"] = ft
txtID["fg"] = "#333333"
txtID["justify"] = "center"
txtID["text"] = "Customer ID"
txtID.place(x=100, y=60, width=251, height=30)

txtName = tk.Entry(frmCustomerUpdate)
txtName["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
txtName["font"] = ft
txtName["fg"] = "#333333"
txtName["justify"] = "left"
txtName["text"] = "Customer Name"
txtName.place(x=100, y=110, width=251, height=30)

txtAddress = tk.Entry(frmCustomerUpdate)
txtAddress["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
txtAddress["font"] = ft
txtAddress["fg"] = "#333333"
txtAddress["justify"] = "left"
txtAddress["text"] = "Address"
txtAddress.place(x=100, y=160, width=250, height=30)

txtTown = tk.Entry(frmCustomerUpdate)
txtTown["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
txtTown["font"] = ft
txtTown["fg"] = "#333333"
txtTown["justify"] = "left"
txtTown["text"] = "Town"
txtTown.place(x=100, y=210, width=248, height=30)

txtPostCode = tk.Entry(frmCustomerUpdate)
txtPostCode["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
txtPostCode["font"] = ft
txtPostCode["fg"] = "#333333"
txtPostCode["justify"] = "left"
txtPostCode["text"] = "Post Code"
txtPostCode.place(x=100, y=260, width=248, height=30)

txtContact = tk.Entry(frmCustomerUpdate)
txtContact["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
txtContact["font"] = ft
txtContact["fg"] = "#333333"
txtContact["justify"] = "left"
txtContact["text"] = "Contact"
txtContact.place(x=100, y=310, width=247, height=30)

lblID = tk.Label(frmCustomerUpdate)
ft = tkFont.Font(family='Times', size=10)
lblID["font"] = ft
lblID["fg"] = "#333333"
lblID["justify"] = "left"
lblID["text"] = "Customer ID"
lblID.place(x=10, y=60, width=89, height=30)

lblName = tk.Label(frmCustomerUpdate)
ft = tkFont.Font(family='Times', size=10)
lblName["font"] = ft
lblName["fg"] = "#333333"
lblName["justify"] = "left"
lblName["text"] = "Customer Name"
lblName.place(x=10, y=110, width=91, height=30)

lblAddress = tk.Label(frmCustomerUpdate)
ft = tkFont.Font(family='Times', size=10)
lblAddress["font"] = ft
lblAddress["fg"] = "#333333"
lblAddress["justify"] = "left"
lblAddress["text"] = "Address"
lblAddress.place(x=10, y=160, width=91, height=30)

lblTown = tk.Label(frmCustomerUpdate)
ft = tkFont.Font(family='Times', size=10)
lblTown["font"] = ft
lblTown["fg"] = "#333333"
lblTown["justify"] = "left"
lblTown["text"] = "Town"
lblTown.place(x=10, y=210, width=92, height=30)

lblPostCode = tk.Label(frmCustomerUpdate)
ft = tkFont.Font(family='Times', size=10)
lblPostCode["font"] = ft
lblPostCode["fg"] = "#333333"
lblPostCode["justify"] = "left"
lblPostCode["text"] = "Post Code"
lblPostCode.place(x=10, y=260, width=91, height=30)

lblContact = tk.Label(frmCustomerUpdate)
ft = tkFont.Font(family='Times', size=10)
lblContact["font"] = ft
lblContact["fg"] = "#333333"
lblContact["justify"] = "left"
lblContact["text"] = "Mobile No."
lblContact.place(x=10, y=310, width=91, height=30)

lblTitle = tk.Label(frmCustomerUpdate)
ft = tkFont.Font(family='Times', size=22)
lblTitle["font"] = ft
lblTitle["fg"] = "#333333"
lblTitle["justify"] = "center"
lblTitle["text"] = "CUSTOMER UPDATE"
lblTitle.place(x=10, y=10, width=488, height=37)

btncustomerID = tk.Button(frmCustomerUpdate)
btncustomerID["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
btncustomerID["font"] = ft
btncustomerID["fg"] = "#000000"
btncustomerID["justify"] = "center"
btncustomerID["text"] = "Search Customer ID"
btncustomerID.place(x=370, y=60, width=130, height=30)
btncustomerID["command"] = show_ID

btncustomerName = tk.Button(frmCustomerUpdate)
btncustomerName["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
btncustomerName["font"] = ft
btncustomerName["fg"] = "#000000"
btncustomerName["justify"] = "center"
btncustomerName["text"] = "Search Customer Name"
btncustomerName.place(x=370, y=110, width=130, height=30)
btncustomerName["command"] = show_Name

btnMobile = tk.Button(frmCustomerUpdate)
btnMobile["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
btnMobile["font"] = ft
btnMobile["fg"] = "#000000"
btnMobile["justify"] = "center"
btnMobile["text"] = "Search Mobile No."
btnMobile.place(x=370, y=160, width=129, height=30)
btnMobile["command"] = show_Contact

btnUpdate = tk.Button(frmCustomerUpdate)
btnUpdate["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
btnUpdate["font"] = ft
btnUpdate["fg"] = "#000000"
btnUpdate["justify"] = "center"
btnUpdate["text"] = "Update"
btnUpdate.place(x=370, y=210, width=128, height=30)
btnUpdate["command"] = update_record

btnDelete = tk.Button(frmCustomerUpdate)
btnDelete["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
btnDelete["font"] = ft
btnDelete["fg"] = "#000000"
btnDelete["justify"] = "center"
btnDelete["text"] = "Delete"
btnDelete.place(x=370, y=260, width=126, height=30)
btnDelete["command"] = delete_record

btnClose = tk.Button(frmCustomerUpdate)
btnClose["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
btnClose["font"] = ft
btnClose["fg"] = "#000000"
btnClose["justify"] = "center"
btnClose["text"] = "Close"
btnClose.place(x=370, y=310, width=126, height=30)
btnClose["command"] = btnClose_Command

frmCustomerUpdate.mainloop()  # run form by default
