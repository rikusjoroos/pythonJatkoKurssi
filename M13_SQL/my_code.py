import sqlite3

db_file='my_db.db'

con = sqlite3.connect(db_file)

cur = con.cursor()

for row in cur.execute("SELECT name FROM texttable;"):
    print(row)

