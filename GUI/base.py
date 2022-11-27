# -*- coding: utf-8 -*-
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Omg")
root.iconbitmap('icon.ico')
def open_():
    global my_img1
    top = Toplevel()
    top.title("Toplevel")
    top.iconbitmap("icon.ico")

    img1 =Image.open("images/photo1.jpg")
    rimg1 = img1.resize((round(img1.width/6), round(img1.height/6)))
    my_img1 = ImageTk.PhotoImage(rimg1)

    myLabel = Label(top, image = my_img1)
    myLabel.pack()
    
    btn2 = Button(top, text = "close window", command = top.destroy)
    btn2.pack()
    
btn = Button(root, text = "open second window", command = open_)

btn.pack()
root.mainloop()