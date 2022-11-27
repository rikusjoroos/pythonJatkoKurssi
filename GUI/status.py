# -*- coding: utf-8 -*-
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Omg")
root.iconbitmap('icon.ico')

img1 =Image.open("images/photo1.jpg")
rimg1 = img1.resize((round(img1.width/6), round(img1.height/6)))

img2 =Image.open("images/photo2.jpg")
rimg2 = img2.resize((round(img2.width/6), round(img2.height/6)))

img3 =Image.open("images/photo3.jpg")
rimg3 = img3.resize((round(img3.width/6), round(img3.height/6)))

img4 =Image.open("images/photo4.png")
rimg4 = img4.resize((round(img4.width/6), round(img4.height/6)))

my_img1 = ImageTk.PhotoImage(rimg1)
my_img2 = ImageTk.PhotoImage(rimg2)
my_img3 = ImageTk.PhotoImage(rimg3)
my_img4 = ImageTk.PhotoImage(rimg4)

image_list = [my_img1, my_img2, my_img3, my_img4]

status = Label(root, text = "Image "  + "1" + " of " + str(len(image_list)), bd=1, relief = SUNKEN, anchor = E)



my_label = Label(image = my_img1)
my_label.grid(row = 0, column = 0, columnspan = 3)

def forward(image_number):
    global my_label
    global button_next
    global button_back
    global status
    #my_label.grid_forget()
    my_label.config(image = image_list[image_number-1])
    button_next.config(command = lambda: forward(image_number+1))
    button_back.config(command = lambda: back(image_number-1), state = NORMAL)
    status.config(text = "Image "  + str(image_number) + " of " + str(len(image_list)))
    
    if image_number == 4:
        button_next.config(state=DISABLED)

def back(image_number):
    global my_label
    global button_forward
    global button_back
    global status
    
    my_label.config(image = image_list[image_number-1])
    button_next.config(command = lambda: forward(image_number+1))
    button_back.config(command = lambda: back(image_number-1))
    status.config(text = "Image "  + str(image_number) + " of " + str(len(image_list)))
    
    if image_number == 1:
        button_back.config(state = DISABLED)

        

    

button_back = Button(root, text = "<<" , command =  back, state = DISABLED)
button_exit = Button(root, text = "Exit", command = root.destroy)
button_next = Button(root, text = ">>", command = lambda: forward(2))

button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)
button_next.grid(row = 1, column = 2, pady = 10)
status.grid(row = 2, column = 0, columnspan = 3, sticky = W+E)


root.mainloop()