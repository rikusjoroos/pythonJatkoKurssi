from tkinter import *

def myclick():
    global lbl
    lbl.config(text = "Button pressed!")
    
root = Tk()

btn = Button(root,text = "Press this", command = myclick)

lbl = Label(root, text = "Button not pressed!")

btn.pack()
lbl.pack()


    
#Don't modify lines below
if __name__ == "__main__":
    root.mainloop()
