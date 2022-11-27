# -*- coding: utf-8 -*-
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("Omg")
root.iconbitmap('icon.ico')



def open_():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir = "C:/Users/riku.sjoroos", title = "Select a file", filetypes =(("jpg files","*.jpg"),("all files","*.*")))

    my_label = Label(root, text = root.filename)
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label= Label(root, image = my_image)
    my_image_label.pack()
    

my_btn = Button(root, text = "open file", command = open_)
my_btn.pack()
root.mainloop()