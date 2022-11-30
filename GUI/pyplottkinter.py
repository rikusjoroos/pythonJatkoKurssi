# -*- coding: utf-8 -*-

from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()
root.title("Menu")
root.geometry("320x150")

def graph():
    global my_label
    house_prices = np.random.normal(200000, 2500, 5000)
    fig = plt.Figure()
    ax = fig.add_subplot()
    ax.hist(house_prices, 50)
    
    canvas = FigureCanvasTkAgg(fig, master = my_label)
    canvas.draw()
    canvas.get_tk_widget().pack()

my_button = Button(root, text = "Show Graph", command = graph)
my_button.pack()

my_label = Label(root, width = 250, height = 250)
my_label.pack()

root.mainloop()