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
        'CREATE TABLE IF NOT EXISTS product_master('
        'idno INTEGER PRIMARY KEY,'
        'datestamp TEXT, '
        'prod_name TEXT, '
        'stock NUMBER, '
        'price NUMBER, '
        'amount NUMBER)')

def show_ID():
    frmList = tk.Tk()
    frmList.title("List of Product")
    width = 665
    height = 500
    screenwidth = frmList.winfo_screenwidth()
    screenheight = frmList.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    frmList.geometry(alignstr)
    frmList.resizable(width=False, height=False)
    ProductID = txtID.get()
    data_set = my_conn.execute("SELECT * FROM product_master WHERE idno=?", (ProductID,))
    # btnFullName.grid(columnspan=2, padx=15, pady=15)
    output_data(data_set, frmList)
    clear_form()


def show_Name():
    frmList = tk.Tk()
    frmList.title("List of Product")
    width = 665
    height = 500
    screenwidth = frmList.winfo_screenwidth()
    screenheight = frmList.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    frmList.geometry(alignstr)
    frmList.resizable(width=False, height=False)
    ProductName = txtName.get()
    data_set = my_conn.execute("SELECT * FROM product_master WHERE Prod_Name like?", (ProductName,))
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


create_table()

frmProdSearch = tk.Tk()
frmProdSearch.title("Product Search")
width = 513
height = 171
screenwidth = frmProdSearch.winfo_screenwidth()
screenheight = frmProdSearch.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
frmProdSearch.geometry(alignstr)
frmProdSearch.resizable(width=False, height=False)

txtID=tk.Entry(frmProdSearch)
txtID["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
txtID["font"] = ft
txtID["fg"] = "#333333"
txtID["justify"] = "center"
txtID["text"] = "Product ID"
txtID.place(x=100,y=60,width=251,height=30)

txtName=tk.Entry(frmProdSearch)
txtName["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
txtName["font"] = ft
txtName["fg"] = "#333333"
txtName["justify"] = "left"
txtName["text"] = "Entry"
txtName.place(x=100,y=110,width=251,height=30)

lblID=tk.Label(frmProdSearch)
ft = tkFont.Font(family='Times',size=10)
lblID["font"] = ft
lblID["fg"] = "#333333"
lblID["justify"] = "left"
lblID["text"] = "Product ID"
lblID.place(x=10,y=60,width=89,height=30)

lblName=tk.Label(frmProdSearch)
ft = tkFont.Font(family='Times',size=10)
lblName["font"] = ft
lblName["fg"] = "#333333"
lblName["justify"] = "left"
lblName["text"] = "Product Name"
lblName.place(x=10,y=110,width=91,height=30)


lblTitle = tk.Label(frmProdSearch)
ft = tkFont.Font(family='Times', size=22)
lblTitle["font"] = ft
lblTitle["fg"] = "#333333"
lblTitle["justify"] = "center"
lblTitle["text"] = "PRODUCT SEARCH"
lblTitle.place(x=10,y=10,width=488,height=37)

btnProdID=tk.Button(frmProdSearch)
btnProdID["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
btnProdID["font"] = ft
btnProdID["fg"] = "#000000"
btnProdID["justify"] = "center"
btnProdID["text"] = "Search Product ID"
btnProdID.place(x=370,y=60,width=130,height=30)
btnProdID["command"] = show_ID

btnProdName=tk.Button(frmProdSearch)
btnProdName["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
btnProdName["font"] = ft
btnProdName["fg"] = "#000000"
btnProdName["justify"] = "center"
btnProdName["text"] = "Search Product Name"
btnProdName.place(x=370,y=110,width=130,height=30)
btnProdName["command"] = show_Name

frmProdSearch.mainloop()  # run form by default