# -*- coding: utf-8 -*-

from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text = "Clicked")
    myLabel.pack()

myButton = Button(root, text = "Click me!", state = NORMAL, padx = 50, pady = 50, command = myClick, fg = "blue", bg = "red")

myButton.pack()

root.mainloop()