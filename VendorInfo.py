import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from tkinter.messagebox import showinfo
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


def show_all():
    frmList = tk.Tk()
    frmList.title("List of Vendors")
    width = 665
    height = 500
    screenwidth = frmList.winfo_screenwidth()
    screenheight = frmList.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    frmList.geometry(alignstr)
    frmList.resizable(width=False, height=False)
    data_set = my_conn.execute("SELECT * FROM vendor_master")
    # btnFullName.grid(columnspan=2, padx=15, pady=15)
    output_data(data_set, frmList)
    clear_form()


def output_data(data_set, frmList):
    i = 0  # row value inside the loop
    for person in data_set:
        for j in range(len(person)):
            e = Entry(frmList, width=15, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, person[j])
        i = i + 1
    return frmList


def clear_form():
    txtVendor_name.delete(0, END)
    txtAddress.delete(0, END)
    txtTown.delete(0, END)
    txtPost_code.delete(0, END)
    txtContact.delete(0, END)


def btnClose_Command():
    clear_form()
    exit()


def putRecord():
    with my_conn:
        currtime = time.time()
        date = datetime.datetime.fromtimestamp(currtime).strftime('%c')
        vendor_name = txtVendor_name.get()
        address = txtAddress.get()
        town = txtTown.get()
        post_code = txtPost_code.get()
        contact = txtContact.get()

        cdb.execute("INSERT INTO vendor_master(datestamp, vendor_name, address, town, post_code, contact) "
                    "VALUES (?, ?, ?, ?, ?, ?)",
                    (date, vendor_name, address, town, post_code, contact))

        my_conn.commit()

        msg = f'Record Successfully Saved!'
        showinfo(title='Information', message=msg)

    clear_form()


create_table()

frmVendor = tk.Tk()
frmVendor.title("Vendor Information Form")
width = 500
height = 378
screenwidth = frmVendor.winfo_screenwidth()
screenheight = frmVendor.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
frmVendor.geometry(alignstr)
frmVendor.resizable(width=False, height=False)

txtVendor_name = tk.Entry(frmVendor)
txtVendor_name["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
txtVendor_name["font"] = ft
txtVendor_name["fg"] = "#333333"
txtVendor_name["justify"] = "left"
txtVendor_name["text"] = "Vendor Name"
txtVendor_name.place(x=120, y=80, width=355, height=30)

txtAddress = tk.Entry(frmVendor)
txtAddress["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
txtAddress["font"] = ft
txtAddress["fg"] = "#333333"
txtAddress["justify"] = "left"
txtAddress["text"] = "Address"
txtAddress.place(x=120, y=130, width=355, height=30)

txtTown = tk.Entry(frmVendor)
txtTown["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
txtTown["font"] = ft
txtTown["fg"] = "#333333"
txtTown["justify"] = "left"
txtTown["text"] = "Town"
txtTown.place(x=120, y=180, width=355, height=30)

txtPost_code = tk.Entry(frmVendor)
txtPost_code["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
txtPost_code["font"] = ft
txtPost_code["fg"] = "#333333"
txtPost_code["justify"] = "left"
txtPost_code["text"] = "Post Code"
txtPost_code.place(x=120, y=230, width=355, height=30)

txtContact = tk.Entry(frmVendor)
txtContact["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
txtContact["font"] = ft
txtContact["fg"] = "#333333"
txtContact["justify"] = "left"
txtContact["text"] = "Entry"
txtContact.place(x=120, y=280, width=355, height=30)

lblVendor_name = tk.Label(frmVendor)
ft = tkFont.Font(family='Times', size=10)
lblVendor_name["font"] = ft
lblVendor_name["fg"] = "#333333"
lblVendor_name["justify"] = "left"
lblVendor_name["text"] = "Vendor Name"
lblVendor_name.place(x=20, y=80, width=101, height=30)

lblAddress = tk.Label(frmVendor)
ft = tkFont.Font(family='Times', size=10)
lblAddress["font"] = ft
lblAddress["fg"] = "#333333"
lblAddress["justify"] = "left"
lblAddress["text"] = "Address"
lblAddress.place(x=20, y=130, width=103, height=31)

lblTown = tk.Label(frmVendor)
ft = tkFont.Font(family='Times', size=10)
lblTown["font"] = ft
lblTown["fg"] = "#333333"
lblTown["justify"] = "left"
lblTown["text"] = "Town"
lblTown.place(x=20, y=180, width=103, height=33)

lblPostCode = tk.Label(frmVendor)
ft = tkFont.Font(family='Times', size=10)
lblPostCode["font"] = ft
lblPostCode["fg"] = "#333333"
lblPostCode["justify"] = "left"
lblPostCode["text"] = "Post Code"
lblPostCode.place(x=20, y=230, width=103, height=31)

lblContact = tk.Label(frmVendor)
ft = tkFont.Font(family='Times', size=10)
lblContact["font"] = ft
lblContact["fg"] = "#333333"
lblContact["justify"] = "left"
lblContact["text"] = "Contact No."
lblContact.place(x=20, y=280, width=103, height=32)

lblTitle = tk.Label(frmVendor)
ft = tkFont.Font(family='Times', size=22)
lblTitle["font"] = ft
lblTitle["fg"] = "#333333"
lblTitle["justify"] = "center"
lblTitle["text"] = "VENDOR INFORMATION ENTRY"
lblTitle.place(x=0, y=20, width=500, height=30)

btnSave = tk.Button()
btnSave["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
btnSave["font"] = ft
btnSave["fg"] = "#000000"
btnSave["justify"] = "center"
btnSave["text"] = "Save"
btnSave.place(x=120, y=330, width=100, height=25)
btnSave["command"] = putRecord

btnShow = tk.Button()
btnShow["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
btnShow["font"] = ft
btnShow["fg"] = "#000000"
btnShow["justify"] = "center"
btnShow["text"] = "Show Record"
btnShow.place(x=230, y=330, width=100, height=25)
btnShow["command"] = show_all

btnClose = tk.Button()
btnClose["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
btnClose["font"] = ft
btnClose["fg"] = "#000000"
btnClose["justify"] = "center"
btnClose["text"] = "Close"
btnClose.place(x=340, y=330, width=100, height=25)
btnClose["command"] = btnClose_Command

frmVendor.mainloop()  # run form by default