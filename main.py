import os
from tkinter import *
import tkinter as tk
from tkinter.messagebox import showinfo
import sqlite3

name_of_db = 'inventory_master.db'
my_conn = sqlite3.connect(name_of_db)
cdb = my_conn.cursor()


def frmCustomer():
    os.system('python CustomerInfo.py')

def frmVendor():
    os.system('python VendorInfo.py')

def frmProduct():
    os.system('python ProductEntry.py')

def frmProdSales():
    os.system('python ProductSale.py')

def frmProdSearch():
    os.system('python ProductSearch.py')

def show_all_product():
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

def output_data(data_set, frmList):
    i = 0  # row value inside the loop
    for person in data_set:
        for j in range(len(person)):
            e = Entry(frmList, width=15, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, person[j])
        i = i + 1
    return frmList

def frmVendorUpdate():
    os.system('python VendorUpdate.py')

def frmVendorSearch():
    os.system('python VendorSearch.py')

def frmCustomerSearch():
    os.system('python CustomerSearch.py')

def frmCustomerSearch():
    os.system('python CustomerSearch.py')

def frmCustomerUpdate():
    os.system('python CustomerUpdate.py')

def exit_command():
    msg = f'Thank you and have a nice day!'
    showinfo(title='Exit', message=msg)
    root.destroy()

root = Tk()
root.title('Inventory Management System')
width = 900
height = 700
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.state('zoomed')

bg = PhotoImage(file="back.png")
label1 = Label(root, image=bg)
label1.place(x=0, y=0)

# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create the file_menu
product_menu = Menu(menubar, tearoff=0)

# add menu items to the product menu
product_menu.add_command(label='New Product Entry', command=frmProduct)
product_menu.add_separator()
product_menu.add_command(label='Product Sale Entry', command=frmProdSales)
product_menu.add_separator()
product_menu.add_command(label='Product Search', command=frmProdSearch)
product_menu.add_separator()
product_menu.add_command(label='List of All Products', command=show_all_product)
menubar.add_cascade(label="Manage Product", menu=product_menu)

# create the Customer menu
customer_menu = Menu(menubar, tearoff=0)
customer_menu.add_command(label='Customer Information Entry', command=frmCustomer)
customer_menu.add_separator()
customer_menu.add_command(label='Customer Information Update', command=frmCustomerUpdate)
customer_menu.add_separator()
customer_menu.add_command(label='Customer Search', command=frmCustomerSearch)

menubar.add_cascade(label="Manage Customer", menu=customer_menu)

# create the Help menu
vendor_menu = Menu(menubar, tearoff=0)
vendor_menu.add_command(label='Vendor Information Entry', command=frmVendor)
vendor_menu.add_separator()
vendor_menu.add_command(label='Vendor Information Update', command=frmVendorUpdate)
vendor_menu.add_separator()
vendor_menu.add_command(label='Vendor Search', command=frmVendorSearch)
menubar.add_cascade(label="Manage Vendor", menu=vendor_menu)

exit_menu = Menu(menubar, tearoff=0)
exit_menu.add_command(label='Exit', command=exit_command)
menubar.add_cascade(label="Exit", menu=exit_menu)


root.mainloop()