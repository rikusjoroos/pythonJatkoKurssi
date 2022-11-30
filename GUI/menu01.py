# -*- coding: utf-8 -*-

from tkinter import *

root = Tk()
root.title("Menu")
root.geometry("320x150")

menubar = Menu(root)
root.config(menu = menubar)

file_menu = Menu(menubar, tearoff = 0)

file_menu.add_command(label = "New")
file_menu.add_command(label = "Open...")
file_menu.add_command(label = "Close")
file_menu.add_separator()

def color_themes():
    root.config(background = "black")

sub_menu = Menu(file_menu)
sub_menu.add_command(label = "Keyboard Shortcuts")
sub_menu.add_command(label = "Color Themes", command = color_themes)
file_menu.add_cascade(label = "Preferences", menu = sub_menu)

file_menu.add_command(label = "Exit", command = root.destroy)

help_menu = Menu(menubar, tearoff = 0)
help_menu.add_command(label = "Welcome")
help_menu.add_command(label = "About...")

menubar.add_cascade(label = "File", menu = file_menu)
menubar.add_cascade(label = "Help", menu = help_menu)

root.mainloop()