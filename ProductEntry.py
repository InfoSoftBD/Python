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


def show_all():
    frmList = tk.Tk()
    frmList.title("List of Product")
    width = 665
    height = 500
    screenwidth = frmList.winfo_screenwidth()
    screenheight = frmList.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    frmList.geometry(alignstr)
    frmList.resizable(width=False, height=False)
    data_set = my_conn.execute("SELECT * FROM product_master")
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
    txtVendor_id.delete(0, END)
    txtVendor_name.delete(0, END)
    txtAddress.delete(0, END)
    txtContact.delete(0, END)
    txtProduct_name.delete(0, END)
    txtQty.delete(0, END)
    txtPrice.delete(0, END)
    txtAmount.delete(0, END)

def btnClose_Command():
    clear_form()
    exit()


def putRecord():
    with my_conn:
        currtime = time.time()
        date = datetime.datetime.fromtimestamp(currtime).strftime('%c')
        product_name = txtProduct_name.get()
        stock = int(txtQty.get())
        price = int(txtPrice.get())
        amount = stock * price

        cdb.execute("INSERT INTO product_master(datestamp, prod_name, stock, price, amount) "
                    "VALUES (?, ?, ?, ?, ?)",
                    (date, product_name, stock, price, amount))

        my_conn.commit()
        msg = f'Record Successfully Saved!'
        showinfo(title='Information', message=msg)
    clear_form()


create_table()

frmProduct = tk.Tk()
frmProduct.title("Product Information Form")
width = 561
height = 351
screenwidth = frmProduct.winfo_screenwidth()
screenheight = frmProduct.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
frmProduct.geometry(alignstr)
frmProduct.resizable(width=False, height=False)

txtVendor_id=tk.Entry(frmProduct)
txtVendor_id["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
txtVendor_id["font"] = ft
txtVendor_id["fg"] = "#333333"
txtVendor_id["justify"] = "left"
txtVendor_id.place(x=30,y=100,width=91,height=30)

txtVendor_name=tk.Entry(frmProduct)
txtVendor_name["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
txtVendor_name["font"] = ft
txtVendor_name["fg"] = "#333333"
txtVendor_name["justify"] = "left"
txtVendor_name.place(x=130,y=100,width=409,height=30)

txtAddress = tk.Entry(frmProduct)
txtAddress["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
txtAddress["font"] = ft
txtAddress["fg"] = "#333333"
txtAddress["justify"] = "left"
txtAddress["text"] = "Address"
txtAddress.place(x=30,y=160,width=279,height=30)

txtContact = tk.Entry(frmProduct)
txtContact["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
txtContact["font"] = ft
txtContact["fg"] = "#333333"
txtContact["justify"] = "left"
txtContact["text"] = "Contact"
txtContact.place(x=320,y=160,width=218,height=30)

txtProduct_name=tk.Entry(frmProduct)
txtProduct_name["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
txtProduct_name["font"] = ft
txtProduct_name["fg"] = "#333333"
txtProduct_name["justify"] = "left"
txtProduct_name["text"] = "Product_Name"
txtProduct_name.place(x=30,y=220,width=278,height=30)

txtQty=tk.Entry(frmProduct)
txtQty["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
txtQty["font"] = ft
txtQty["fg"] = "#333333"
txtQty["justify"] = "center"
txtQty["text"] = "Qty"
txtQty.place(x=320,y=220,width=64,height=30)

txtPrice=tk.Entry(frmProduct)
txtPrice["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
txtPrice["font"] = ft
txtPrice["fg"] = "#333333"
txtPrice["justify"] = "right"
txtPrice["text"] = "Price"
txtPrice.place(x=390,y=220,width=68,height=30)

txtAmount=tk.Entry(frmProduct)
txtAmount["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
txtAmount["font"] = ft
txtAmount["fg"] = "#333333"
txtAmount["justify"] = "right"
txtAmount["text"] = "Amount"
txtAmount.place(x=470,y=220,width=69,height=30)

lblVendorID=tk.Label(frmProduct)
ft = tkFont.Font(family='Times',size=10)
lblVendorID["font"] = ft
lblVendorID["fg"] = "#333333"
lblVendorID["justify"] = "left"
lblVendorID["text"] = "Vendor ID"
lblVendorID.place(x=30,y=70,width=91,height=30)

lblVendorName=tk.Label(frmProduct)
ft = tkFont.Font(family='Times',size=10)
lblVendorName["font"] = ft
lblVendorName["fg"] = "#333333"
lblVendorName["justify"] = "left"
lblVendorName["text"] = "Vendor Name"
lblVendorName.place(x=130,y=70,width=412,height=30)

lblAddress=tk.Label(frmProduct)
ft = tkFont.Font(family='Times',size=10)
lblAddress["font"] = ft
lblAddress["fg"] = "#333333"
lblAddress["justify"] = "left"
lblAddress["text"] = "Address"
lblAddress.place(x=30,y=130,width=282,height=30)

lblContact=tk.Label(frmProduct)
ft = tkFont.Font(family='Times',size=10)
lblContact["font"] = ft
lblContact["fg"] = "#333333"
lblContact["justify"] = "left"
lblContact["text"] = "Contact No."
lblContact.place(x=320,y=130,width=219,height=32)

lblProduct=tk.Label(frmProduct)
ft = tkFont.Font(family='Times',size=10)
lblProduct["font"] = ft
lblProduct["fg"] = "#333333"
lblProduct["justify"] = "left"
lblProduct["text"] = "Product Description"
lblProduct.place(x=30,y=190,width=278,height=30)

lblQty=tk.Label(frmProduct)
ft = tkFont.Font(family='Times',size=10)
lblQty["font"] = ft
lblQty["fg"] = "#333333"
lblQty["justify"] = "center"
lblQty["text"] = "Quantity"
lblQty.place(x=320,y=190,width=67,height=30)


lblPrice=tk.Label(frmProduct)
ft = tkFont.Font(family='Times',size=10)
lblPrice["font"] = ft
lblPrice["fg"] = "#333333"
lblPrice["justify"] = "center"
lblPrice["text"] = "Unit Price"
lblPrice.place(x=380,y=190,width=71,height=30)


lblAmount=tk.Label(frmProduct)
ft = tkFont.Font(family='Times',size=10)
lblAmount["font"] = ft
lblAmount["fg"] = "#333333"
lblAmount["justify"] = "center"
lblAmount["text"] = "Total Price"
lblAmount.place(x=470,y=190,width=70,height=30)

lblTitle = tk.Label(frmProduct)
ft = tkFont.Font(family='Times', size=22)
lblTitle["font"] = ft
lblTitle["fg"] = "#333333"
lblTitle["justify"] = "center"
lblTitle["text"] = "PRODUCT INFORMATION ENTRY"
lblTitle.place(x=20, y=20, width=500, height=30)

btnSave = tk.Button()
btnSave["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
btnSave["font"] = ft
btnSave["fg"] = "#000000"
btnSave["justify"] = "center"
btnSave["text"] = "Save"
btnSave.place(x=60,y=280,width=114,height=30)
btnSave["command"] = putRecord

btnShow = tk.Button()
btnShow["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
btnShow["font"] = ft
btnShow["fg"] = "#000000"
btnShow["justify"] = "center"
btnShow["text"] = "Show Record"
btnShow.place(x=220,y=280,width=116,height=30)
btnShow["command"] = show_all

btnClose = tk.Button()
btnClose["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
btnClose["font"] = ft
btnClose["fg"] = "#000000"
btnClose["justify"] = "center"
btnClose["text"] = "Close"
btnClose.place(x=380,y=280,width=115,height=30)
btnClose["command"] = btnClose_Command

frmProduct.mainloop()  # run form by default