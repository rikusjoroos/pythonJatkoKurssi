from tkinter import *
import sqlite3
db_file='my_db.db'

root = Tk()
root.geometry("100x100")
lbl = Label(root)
lbl.pack()
conn = sqlite3.connect(db_file)
c = conn.cursor()
c.execute("SELECT data FROM textdata;")
results = c.fetchall()
print(results)
counter = 0

#tekee muutokst
conn.commit()

#suljetaan yhteys
conn.close()

#kursori

def getdata():
    global results
    global counter
#   print (results[counter][0])
    lbl.config(text = str(results[counter][0]))
    counter = counter + 1
    if counter == len(results):
        counter = 0

btn = Button(root, text = "Get row", command = getdata)
btn.pack()



#Don't modify lines below
if __name__ == "__main__":
    root.mainloop()
