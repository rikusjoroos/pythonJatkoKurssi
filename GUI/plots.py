# -*- coding: utf-8 -*-
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title("Omg")
root.iconbitmap('icon.ico')
root.geometry("400x200")
myLabel = Label(root)

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 50)
    plt.show()
    
my_button = Button(root,text = "graph", command = graph)
my_button.pack()

root.mainloop()