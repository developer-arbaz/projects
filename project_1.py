import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector

root = Tk()
root.title("Insert Data")

connection = mysql.connector.connect(host='localhost', user='root', password='',
                                     port='3306', database='text_2')
c = connection.cursor()

bkg = "#636e72"


frame = tk.Frame(root, bg=bkg)

label_firstname = tk.Label(frame, text="First Name: ", font=('verdana',12), bg=bkg)
entry_firstname = tk.Entry(frame, font=('verdana',12))

label_lastname = tk.Label(frame, text="Last Name: ", font=('verdana',12), bg=bkg)
entry_lastname = tk.Entry(frame, font=('verdana',12))

label_email = tk.Label(frame, text="Email: ", font=('verdana',12), bg=bkg)
entry_email = tk.Entry(frame, font=('verdana',12))

label_age = tk.Label(frame, text="Age: ", font=('verdana',12), bg=bkg)
entry_age = tk.Entry(frame, font=('verdana',12))


def insertData():
    firstname = entry_firstname.get()
    lastname = entry_lastname.get()
    email = entry_email.get()
    age = entry_age.get()

    insert_query = "INSERT INTO `users_4`(`First Name`, `Last name`, `Email`, `age`) VALUES (%s, %s, %s, %s)"
    vals = (firstname, lastname, email, age)
    c.execute(insert_query, vals)
    connection.commit()



button_insert = tk.Button(frame, text="Insert", font=('verdana',14), bg='orange',
                          command = insertData)

label_firstname.grid(row=0, column=0)
entry_firstname.grid(row=0, column=1, pady=10, padx=10)

label_lastname.grid(row=1, column=0)
entry_lastname.grid(row=1, column=1, pady=10, padx=10)

label_email.grid(row=2, column=0, sticky='e')
entry_email.grid(row=2, column=1, pady=10, padx=10)

label_age.grid(row=3, column=0, sticky='e')
entry_age.grid(row=3, column=1, pady=10, padx=10)

button_insert.grid(row=4,column=0, columnspan=2, pady=10, padx=10, sticky='nsew')

frame.grid(row=0, column=0)


root.mainloop()
