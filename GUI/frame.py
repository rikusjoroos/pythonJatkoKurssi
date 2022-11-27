# -*- coding: utf-8 -*-
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Omg")
root.iconbitmap('icon.ico')

frame = LabelFrame(root, text = "this is my frame", padx = 5, pady = 5)

frame.pack(padx = 10, pady = 10)

b = Button(frame, text = "Don't click here!")
b1 = Button(frame, text = "Don't click here!")

b.grid(row = 0, column = 0)
b1.grid(row = 0, column = 2)

root.mainloop()