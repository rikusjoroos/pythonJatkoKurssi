# -*- coding: utf-8 -*-
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("Omg")
root.iconbitmap('icon.ico')
root.geometry("400x400")

def show():
    myLabel = Label(root, text = var.get())
    myLabel.pack()
    
var = StringVar()

c = Checkbutton(root, text = "Check this box", variable = var, onvalue = "On", offvalue = "Off")
c.deselect()
c.pack()



myButton = Button(root, text ="show selection", command = show)
myButton.pack()

root.mainloop()