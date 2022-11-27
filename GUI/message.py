# -*- coding: utf-8 -*-
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Omg")
root.iconbitmap('icon.ico')

#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
    #messagebox.showinfo("This is my popup","Hello world!")
    #messagebox.showwarning("This is my popup","Hello world!")
    #messagebox.showerror("This is my popup","Hello world!")
    #messagebox.askquestion("This is my popup","Hello world!")
    #messagebox.askokcancel("This is my popup","Hello world!")
    response = messagebox.askyesno("This is my popup","Hello world!")
    myLabel = Label(root, text = response)
    myLabel.pack()

    #if response == 1:
    #    myLabel = Label(root, text = "You clicked yes")
    #    myLabel.pack()
    #else:
    #    myLabel = Label(root, text = "You clicked no")
    #    myLabel.pack()
        
        
    

btn = Button(root, text = "Popup", command = popup)
btn.pack()

root.mainloop()