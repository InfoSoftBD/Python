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
        'CREATE TABLE IF NOT EXISTS vendor_master('
        'idno INTEGER PRIMARY KEY,'
        'datestamp TEXT, '
        'vendor_name TEXT, '
        'address TEXT, '
        'town TEXT, '
        'post_code TEXT, '
        'contact TEXT)')


def show_ID():
    frmList = tk.Tk()
    frmList.title("List of Vendor")
    width = 665
    height = 500
    screenwidth = frmList.winfo_screenwidth()
    screenheight = frmList.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    frmList.geometry(alignstr)
    frmList.resizable(width=False, height=False)
    VendorID = txtID.get()
    txtName.focus_set()
    txtName.insert(INSERT,"Hello")
    data_set = my_conn.execute("SELECT * FROM vendor_master WHERE idno=?", (VendorID,))
    # btnFullName.grid(columnspan=2, padx=15, pady=15)
    output_data(data_set, frmList)
    clear_form()

def set_text(text):
    text= "Rakib"
    txtName.insert(0,text)
    return

def show_Name():
    frmList = tk.Tk()
    frmList.title("List of Vendor")
    width = 665
    height = 500
    screenwidth = frmList.winfo_screenwidth()
    screenheight = frmList.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    frmList.geometry(alignstr)
    frmList.resizable(width=False, height=False)
    VendorName = txtName.get()
    data_set = my_conn.execute("SELECT * FROM vendor_master WHERE vendor_name like?", (VendorName,))
    # btnFullName.grid(columnspan=2, padx=15, pady=15)
    output_data(data_set, frmList)
    clear_form()


def show_Contact():
    frmList = tk.Tk()
    frmList.title("List of Vendor")
    width = 665
    height = 500
    screenwidth = frmList.winfo_screenwidth()
    screenheight = frmList.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    frmList.geometry(alignstr)
    frmList.resizable(width=False, height=False)
    contact = txtContact.get()
    data_set = my_conn.execute("SELECT * FROM vendor_master WHERE contact like?", (contact,))
    # btnFullName.grid(columnspan=2, padx=15, pady=15);2
    output_data(data_set, frmList)
    clear_form()


def update_record():
    with my_conn:
        vendor_id = txtID.get()
        vendor_name = txtName.get()
        address = txtAddress.get()
        town = txtTown.get()
        post_code = txtPostCode.get()
        contact = txtContact.get()
        cdb.execute("UPDATE vendor_master SET vendor_name=?, address=?, town=?, post_code=?, contact=? WHERE idno=?",
                    (vendor_name, address, town, post_code, contact, vendor_id))
        my_conn.commit()
        msg = f'Record Successfully Saved!'
        showinfo(title='Information', message=msg)
    clear_form()


def delete_record():
    with my_conn:
        vendor_id = txtID.get()
        cdb.execute("DELETE FROM vendor_master WHERE idno=?", (vendor_id,))
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

frmVendorUpdate = tk.Tk()
frmVendorUpdate.title("Vendor Update")
width = 513
height = 364
screenwidth = frmVendorUpdate.winfo_screenwidth()
screenheight = frmVendorUpdate.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
frmVendorUpdate.geometry(alignstr)
frmVendorUpdate.resizable(width=False, height=False)

txtID = tk.Entry(frmVendorUpdate)
txtID["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
txtID["font"] = ft
txtID["fg"] = "#333333"
txtID["justify"] = "center"
txtID["text"] = "Vendor ID"
txtID.place(x=100, y=60, width=251, height=30)

txtName = tk.Entry(frmVendorUpdate)
txtName["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
txtName["font"] = ft
txtName["fg"] = "#333333"
txtName["justify"] = "left"
txtName["text"] = "Vendor Name"
txtName.place(x=100, y=110, width=251, height=30)

txtAddress = tk.Entry(frmVendorUpdate)
txtAddress["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
txtAddress["font"] = ft
txtAddress["fg"] = "#333333"
txtAddress["justify"] = "left"
txtAddress["text"] = "Address"
txtAddress.place(x=100, y=160, width=250, height=30)

txtTown = tk.Entry(frmVendorUpdate)
txtTown["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
txtTown["font"] = ft
txtTown["fg"] = "#333333"
txtTown["justify"] = "left"
txtTown["text"] = "Town"
txtTown.place(x=100, y=210, width=248, height=30)

txtPostCode = tk.Entry(frmVendorUpdate)
txtPostCode["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
txtPostCode["font"] = ft
txtPostCode["fg"] = "#333333"
txtPostCode["justify"] = "left"
txtPostCode["text"] = "Post Code"
txtPostCode.place(x=100, y=260, width=248, height=30)

txtContact = tk.Entry(frmVendorUpdate)
txtContact["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
txtContact["font"] = ft
txtContact["fg"] = "#333333"
txtContact["justify"] = "left"
txtContact["text"] = "Contact"
txtContact.place(x=100, y=310, width=247, height=30)

lblID = tk.Label(frmVendorUpdate)
ft = tkFont.Font(family='Times', size=10)
lblID["font"] = ft
lblID["fg"] = "#333333"
lblID["justify"] = "left"
lblID["text"] = "Vendor ID"
lblID.place(x=10, y=60, width=89, height=30)

lblName = tk.Label(frmVendorUpdate)
ft = tkFont.Font(family='Times', size=10)
lblName["font"] = ft
lblName["fg"] = "#333333"
lblName["justify"] = "left"
lblName["text"] = "Vendor Name"
lblName.place(x=10, y=110, width=91, height=30)

lblAddress = tk.Label(frmVendorUpdate)
ft = tkFont.Font(family='Times', size=10)
lblAddress["font"] = ft
lblAddress["fg"] = "#333333"
lblAddress["justify"] = "left"
lblAddress["text"] = "Address"
lblAddress.place(x=10, y=160, width=91, height=30)

lblTown = tk.Label(frmVendorUpdate)
ft = tkFont.Font(family='Times', size=10)
lblTown["font"] = ft
lblTown["fg"] = "#333333"
lblTown["justify"] = "left"
lblTown["text"] = "Town"
lblTown.place(x=10, y=210, width=92, height=30)

lblPostCode = tk.Label(frmVendorUpdate)
ft = tkFont.Font(family='Times', size=10)
lblPostCode["font"] = ft
lblPostCode["fg"] = "#333333"
lblPostCode["justify"] = "left"
lblPostCode["text"] = "Post Code"
lblPostCode.place(x=10, y=260, width=91, height=30)

lblContact = tk.Label(frmVendorUpdate)
ft = tkFont.Font(family='Times', size=10)
lblContact["font"] = ft
lblContact["fg"] = "#333333"
lblContact["justify"] = "left"
lblContact["text"] = "Mobile No."
lblContact.place(x=10, y=310, width=91, height=30)

lblTitle = tk.Label(frmVendorUpdate)
ft = tkFont.Font(family='Times', size=22)
lblTitle["font"] = ft
lblTitle["fg"] = "#333333"
lblTitle["justify"] = "center"
lblTitle["text"] = "VENDOR UPDATE"
lblTitle.place(x=10, y=10, width=488, height=37)

btnVendorID = tk.Button(frmVendorUpdate)
btnVendorID["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
btnVendorID["font"] = ft
btnVendorID["fg"] = "#000000"
btnVendorID["justify"] = "center"
btnVendorID["text"] = "Search Vendor ID"
btnVendorID.place(x=370, y=60, width=130, height=30)
btnVendorID["command"] = show_ID

btnVendorName = tk.Button(frmVendorUpdate)
btnVendorName["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
btnVendorName["font"] = ft
btnVendorName["fg"] = "#000000"
btnVendorName["justify"] = "center"
btnVendorName["text"] = "Search Vendor Name"
btnVendorName.place(x=370, y=110, width=130, height=30)
btnVendorName["command"] = show_Name

btnMobile = tk.Button(frmVendorUpdate)
btnMobile["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
btnMobile["font"] = ft
btnMobile["fg"] = "#000000"
btnMobile["justify"] = "center"
btnMobile["text"] = "Search Mobile No."
btnMobile.place(x=370, y=160, width=129, height=30)
btnMobile["command"] = show_Contact

btnUpdate = tk.Button(frmVendorUpdate)
btnUpdate["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
btnUpdate["font"] = ft
btnUpdate["fg"] = "#000000"
btnUpdate["justify"] = "center"
btnUpdate["text"] = "Update"
btnUpdate.place(x=370, y=210, width=128, height=30)
btnUpdate["command"] = update_record

btnDelete = tk.Button(frmVendorUpdate)
btnDelete["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
btnDelete["font"] = ft
btnDelete["fg"] = "#000000"
btnDelete["justify"] = "center"
btnDelete["text"] = "Delete"
btnDelete.place(x=370, y=260, width=126, height=30)
btnDelete["command"] = delete_record

btnClose = tk.Button(frmVendorUpdate)
btnClose["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
btnClose["font"] = ft
btnClose["fg"] = "#000000"
btnClose["justify"] = "center"
btnClose["text"] = "Close"
btnClose.place(x=370, y=310, width=126, height=30)
btnClose["command"] = btnClose_Command

frmVendorUpdate.mainloop()  # run form by default
