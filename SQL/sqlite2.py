# -*- coding: utf-8 -*-
import sqlite3

con = sqlite3.connect("examble.db")

cur = con.cursor()

res = cur.execute('SELECT count(rowid) FROM stocks')
print(res.fetchone())

data = [
        ('2006-03-23', 'BUY', 'IBM', 1000, 45.0),
        ('2006-04-05','BUY', 'MSFT', 1000, 72.0),
        ('2006-04-06', 'SELL', 'IBM', 500, 53),
        ]

cur.executemany('INSERT INTO stocks VALUES(?, ?, ?, ?, ?)', data)

con.commit()

for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)