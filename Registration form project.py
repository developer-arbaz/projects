from tkinter import *
from tkinter import messagebox

screen = Tk()
screen.title("Registration Form")
screen.geometry('400x400')
screen.resizable(False, False)

screen.configure(bg="light blue")

def Save():
    name = name_info.get()
    age = age_info.get()
    phone = phone_info.get()
    email = email_info.get()

    if name == "":
        messagebox.showerror("Error", "Please Enter Your Name")
    elif age == "":
        messagebox.showerror("Error", "Please Enter Your Age")
    elif phone == "":
        messagebox.showerror("Error", "Please Enter Your Phone Number")
    elif email == "":
        messagebox.showerror("Error", "Please Enter your Email")
    else:
        Label(screen, text="Registration Successful", font="20", fg="green").place(x=135, y=285)

def Clear():
    name_info.set('')
    age_info.set('')
    phone_info.set('')
    email_info.set('')

# Label with background color
Label(screen, text="First Name:", font="20", bg="light blue", fg="black").place(x=41, y=75)
Label(screen, text="Last Name:", font="20", bg="light blue", fg="black").place(x=41, y=115)
Label(screen, text="Email:", font="20", bg="light blue", fg="black").place(x=40, y=155)
Label(screen, text="Age:", font="20", bg="light blue", fg="black").place(x=40, y=195)

# Entry
name_info = StringVar()
age_info = StringVar()
phone_info = StringVar()
email_info = StringVar()

name_entry = Entry(screen, font="10", bd=4, textvariable=name_info)
name_entry.place(x=140, y=75)

age_entry = Entry(screen, font="10", bd=4, textvariable=age_info)
age_entry.place(x=140, y=115)

phone_entry = Entry(screen, font="10", bd=4, textvariable=phone_info)
phone_entry.place(x=140, y=155)

email_entry = Entry(screen, font="10", bd=4, textvariable=email_info)
email_entry.place(x=140, y=195)

# Button
Button(screen, text="Save", font="20", command=Save, bg="orange").place(x=150, y=255)
Button(screen, text="Clear", font="20", command=Clear, bg="red", fg="white").place(x=215, y=255)

mainloop()
