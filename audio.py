import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root=Tk()
root.title("Text to Speech")
root.geometry("1100x750")
root.resizable(False,False)
root.configure(bg="#305065")

engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if(text):
        if (speed == "Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()
    

def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
    if(text):
        if (speed == "Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()


#icon
image_icon=PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)

#Top Frame
Top_frame=Frame(root,bg="white",width=1300,height=360)
Top_frame.place(x=0,y=0)

Logo=PhotoImage(file="logo2.png")
Label(Top_frame,image=Logo,bg="white").place(x=10,y=5)


#############
text_area=Text(root,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=20,y=420,width=600,height=300)

Label(root,text="VOICE",font="arial 15 bold",bg="#305065",fg="white").place(x=730,y=460)
Label(root,text="SPEED",font="arial 15 bold",bg="#305065",fg="white").place(x=910,y=460)

gender_combobox=Combobox(root,values=['Male','Female'],font="arial 14",state='r',width=10)
gender_combobox.place(x=700,y=500)
gender_combobox.set('Select')

speed_combobox=Combobox(root,values=['Fast','Normal','Slow'],font="arial 14",state='r',width=10)
speed_combobox.place(x=890,y=500)
speed_combobox.set('Select')


imageicon=PhotoImage(file="")
btn=Button(root,text="Speak",width=130,compound=LEFT,image=imageicon,bg="#FF9912",font="arial 20 bold",command=speaknow)
btn.place(x=700,y=570)


imageicon2=PhotoImage(file="")
save=Button(root,text="Save",compound=LEFT,image=imageicon2,width=130,bg="#39c790",font="arial 20 bold",command=download)
save.place(x=890,y=570)






root.mainloop()
