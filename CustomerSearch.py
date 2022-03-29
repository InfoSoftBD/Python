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
        'CREATE TABLE IF NOT EXISTS Customer_master('
        'idno INTEGER PRIMARY KEY,'
        'datestamp TEXT, '
        'Customer_name TEXT, '
        'address TEXT, '
        'town TEXT, '
        'post_code TEXT, '
        'contact TEXT)')


def show_ID():
    frmList = tk.Tk()
    frmList.title("List of Customer")
    width = 665
    height = 500
    screenwidth = frmList.winfo_screenwidth()
    screenheight = frmList.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    frmList.geometry(alignstr)
    frmList.resizable(width=False, height=False)
    CustomerID = txtID.get()
    data_set = my_conn.execute("SELECT * FROM customer_master WHERE idno=?", (CustomerID,))
    # btnFullName.grid(columnspan=2, padx=15, pady=15)
    output_data(data_set, frmList)
    clear_form()


def show_Name():
    frmList = tk.Tk()
    frmList.title("List of Customer")
    width = 665
    height = 500
    screenwidth = frmList.winfo_screenwidth()
    screenheight = frmList.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    frmList.geometry(alignstr)
    frmList.resizable(width=False, height=False)
    CustomerName = txtName.get()
    data_set = my_conn.execute("SELECT * FROM customer_master WHERE customer_name like?", (CustomerName,))
    # btnFullName.grid(columnspan=2, padx=15, pady=15)
    output_data(data_set, frmList)
    clear_form()

def show_Contact():
    frmList = tk.Tk()
    frmList.title("List of Customer")
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

def show_PostCode():
    frmList = tk.Tk()
    frmList.title("List of Customer")
    width = 665
    height = 500
    screenwidth = frmList.winfo_screenwidth()
    screenheight = frmList.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    frmList.geometry(alignstr)
    frmList.resizable(width=False, height=False)
    PostCode = txtPostCode.get()
    data_set = my_conn.execute("SELECT * FROM customer_master WHERE Post_code like?", (PostCode,))
    # btnFullName.grid(columnspan=2, padx=15, pady=15)
    output_data(data_set, frmList)
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
    txtContact.delete(0, END)
    txtPostCode.delete(0, END)

create_table()

frmCustomerSearch = tk.Tk()
frmCustomerSearch.title("Customer Search")
width = 517
height = 273
screenwidth = frmCustomerSearch.winfo_screenwidth()
screenheight = frmCustomerSearch.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
frmCustomerSearch.geometry(alignstr)
frmCustomerSearch.resizable(width=False, height=False)


txtID=tk.Entry(frmCustomerSearch)
txtID["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
txtID["font"] = ft
txtID["fg"] = "#333333"
txtID["justify"] = "center"
txtID["text"] = "Customer ID"
txtID.place(x=100,y=60,width=251,height=30)


txtName=tk.Entry(frmCustomerSearch)
txtName["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
txtName["font"] = ft
txtName["fg"] = "#333333"
txtName["justify"] = "left"
txtName["text"] = "Customer Name"
txtName.place(x=100,y=110,width=251,height=30)


txtContact=tk.Entry(frmCustomerSearch)
txtContact["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
txtContact["font"] = ft
txtContact["fg"] = "#333333"
txtContact["justify"] = "left"
txtContact["text"] = "Contact"
txtContact.place(x=100,y=160,width=250,height=30)


txtPostCode=tk.Entry(frmCustomerSearch)
txtPostCode["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
txtPostCode["font"] = ft
txtPostCode["fg"] = "#333333"
txtPostCode["justify"] = "left"
txtPostCode["text"] = "Post Code"
txtPostCode.place(x=100,y=210,width=248,height=30)


lblID=tk.Label(frmCustomerSearch)
ft = tkFont.Font(family='Times',size=10)
lblID["font"] = ft
lblID["fg"] = "#333333"
lblID["justify"] = "left"
lblID["text"] = "Customer ID"
lblID.place(x=10,y=60,width=89,height=30)


lblName=tk.Label(frmCustomerSearch)
ft = tkFont.Font(family='Times',size=10)
lblName["font"] = ft
lblName["fg"] = "#333333"
lblName["justify"] = "left"
lblName["text"] = "Customer Name"
lblName.place(x=10,y=110,width=91,height=30)


lblContact=tk.Label(frmCustomerSearch)
ft = tkFont.Font(family='Times',size=10)
lblContact["font"] = ft
lblContact["fg"] = "#333333"
lblContact["justify"] = "left"
lblContact["text"] = "Mobile No."
lblContact.place(x=10,y=160,width=91,height=30)


lblPostCode= tk.Label(frmCustomerSearch)
ft = tkFont.Font(family='Times', size=10)
lblPostCode["font"] = ft
lblPostCode["fg"] = "#333333"
lblPostCode["justify"] = "left"
lblPostCode["text"] = "Post Code"
lblPostCode.place(x=10, y=210, width=92, height=30)


lblTitle = tk.Label(frmCustomerSearch)
ft = tkFont.Font(family='Times', size=22)
lblTitle["font"] = ft
lblTitle["fg"] = "#333333"
lblTitle["justify"] = "center"
lblTitle["text"] = "CUSTOMER SEARCH"
lblTitle.place(x=10,y=10,width=488,height=37)


btnCustomerID=tk.Button(frmCustomerSearch)
btnCustomerID["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
btnCustomerID["font"] = ft
btnCustomerID["fg"] = "#000000"
btnCustomerID["justify"] = "center"
btnCustomerID["text"] = "Search Customer ID"
btnCustomerID.place(x=370,y=60,width=130,height=30)
btnCustomerID["command"] = show_ID


btnCustomerName=tk.Button(frmCustomerSearch)
btnCustomerName["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
btnCustomerName["font"] = ft
btnCustomerName["fg"] = "#000000"
btnCustomerName["justify"] = "center"
btnCustomerName["text"] = "Search Customer Name"
btnCustomerName.place(x=370,y=110,width=130,height=30)
btnCustomerName["command"] = show_Name


btnMobile = tk.Button(frmCustomerSearch)
btnMobile["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
btnMobile["font"] = ft
btnMobile["fg"] = "#000000"
btnMobile["justify"] = "center"
btnMobile["text"] = "Search Mobile No."
btnMobile.place(x=370, y=160, width=129, height=30)
btnMobile["command"] = show_Contact


btnPostCode=tk.Button(frmCustomerSearch)
btnPostCode["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
btnPostCode["font"] = ft
btnPostCode["fg"] = "#000000"
btnPostCode["justify"] = "center"
btnPostCode["text"] = "Search Post Code"
btnPostCode.place(x=370,y=210,width=128,height=30)
btnPostCode["command"] = show_PostCode


frmCustomerSearch.mainloop()  # run form by default