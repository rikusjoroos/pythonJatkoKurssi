import sqlite3

db_file='my_db.db'

con = sqlite3.connect(db_file)

cur = con.cursor()

cur.execute('CREATE TABLE texttable (id INTEGER PRIMARY KEY,name TEXT NOT NULL);')

cur.execute("INSERT INTO texttable (name) VALUES('Matti'),('Ville'),('Kaisa'),('Mikko');")

con.commit()
con.close()