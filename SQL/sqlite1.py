# -*- coding: utf-8 -*-
import sqlite3

con = sqlite3.connect("examble.db")

cur = con.cursor()

cur.execute('''CREATE TABLE STOCKS
            (date text, trans text, symbol text, qty real, price real)''')

cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

con.commit()

con.close()