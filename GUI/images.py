# -*- coding: utf-8 -*-
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Omg")
root.iconbitmap('icon.ico')

my_img = ImageTk.PhotoImage(Image.open("photo1.jpg"))

my_label = Label(image = my_img)

my_label.pack()

quit_button = Button(root, text ="exit", command = root.destroy)
quit_button.pack()


root.mainloop()