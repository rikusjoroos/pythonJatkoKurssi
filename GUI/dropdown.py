# -*- coding: utf-8 -*-
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("Omg")
root.iconbitmap('icon.ico')
root.geometry("400x400")
clicked = StringVar()


def show():
    myLabel = Label(root, text = clicked.get())
    myLabel.pack()
    
options = ["monday",
           "tuesday",
           "wednesday",
           "thursday",
           "friday"
           ]

clicked.set(options[0])
drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text = "show selection", command = show)
myButton.pack()

root.mainloop()