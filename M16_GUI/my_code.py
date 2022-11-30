from tkinter import *
import math

def calculate():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())
        if (b*b)-(4*a*c) < 0:
            label_root1.config(text = "-")
            label_root2.config(text = "-")
        else:
            result1 = (-b+(math.sqrt(b*b-4*a*c)))/(2*a)
            result2 = (-b-(math.sqrt(b*b-4*a*c)))/(2*a)
            label_root1.config(text = str(result1))
            label_root2.config(text = str(result2))
    except:
        label_root1.config(text = "-")
        label_root2.config(text = "-")


    

root = Tk()

entry_a = Entry(root, width = 20)
entry_b = Entry(root, width = 20)
entry_c = Entry(root, width = 20)

label_root1 = Label(root)
label_root2 = Label(root)

btn = Button(root, text = "calculate", command = calculate)

entry_a.grid(row = 0, column = 1)
entry_b.grid(row = 0, column = 2)
entry_c.grid(row = 0, column = 3)
label_root1.grid(row = 1, column = 0)
label_root2.grid(row = 1, column = 1)
btn.grid(row = 2, column = 0)
#Don't modify lines below
if __name__ == "__main__":
    root.mainloop()
