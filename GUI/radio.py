# -*- coding: utf-8 -*-
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Omg")
root.iconbitmap('icon.ico')

#r = IntVar()
#r.set("2")

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushrooms", "Mushrooms"),
    ("Onion", "Onion")
    ]

pizza = StringVar()
pizza.set("Pepperoni")
buttons = []
for text, mode in MODES:
    btn = Radiobutton(root, text = text, variable = pizza, value = mode)
    buttons.append(btn)

for btn in buttons:
    btn.pack(anchor = W)
    

def clicked(value):
    myLabel = Label(root, text = value)
    myLabel.pack()
    
#r1 = Radiobutton(root, text="Option 1", variable = r, value = 1, command = lambda: clicked(r.get()))
#r2 = Radiobutton(root, text="Option 2", variable = r, value = 2, command = lambda: clicked(r.get()))
#r1.pack()
#r2.pack()

myLabel = Label(root, text = pizza.get())
myLabel.pack()

myButton = Button(root, text ="Click me", command = lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()