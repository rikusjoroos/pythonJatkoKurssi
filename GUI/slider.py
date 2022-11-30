# -*- coding: utf-8 -*-
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("Omg")
root.iconbitmap('icon.ico')
root.geometry("400x400")

def slide():
    myLabel = Label(root, text = horizontal.get())
    myLabel.pack()
    root.geometry(str(horizontal.get())+"x"+ str(vertical.get()))

vertical = Scale(root, from_ = 0, to = 200)

vertical.pack()

#horizontal = Scale(root, from_ = 0, to = 200, orient = HORIZONTAL, command = slide) slide funktio tarvitsee muuttujan
horizontal = Scale(root, from_ = 0, to = 200, orient = HORIZONTAL)

horizontal.pack()

myLabel = Label(root, text = horizontal.get())


    
    
my_btn = Button(root, text ="click here", command = slide)
my_btn.pack()

root.mainloop()