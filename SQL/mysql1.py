# -*- coding: utf-8 -*-

import pymysql as mysql

mydb = mysql.connect(
    host='localhost',
    user = 'example_user',
    passwd = 'testpwd123',
    port=3307,
    )

mydb.autocommit = True

cursor = mydb.cursor()

create_database = True

if create_database:
    cursor.execute('DROP DATABASE IF EXISTS customers;')
    cursor.execute('CREATE DATABASE customers;')
    cursor.execute('SHOW DATABASES;')
    print('Databases:')
    for db in cursor:
        print(db[0])
    print(32*'-')
    
print('Use customer database')
cursor.execute('USE customers;')

if create_database:
    print ('Create customerinfo talbe')
    cursor.execute('''CREATE TABLE customer(
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255));''')
    
    cursor.execute('SHOW TABLES;')
    print('\nTables:')
    for tbl in cursor:
        print (tbl[0])
    print(32*'-')
    
    print('Insert data')
    
    data = [
        ('Eka', 'Asiakas'),
        ('Toka', 'Asiakas'),
        ('Kolmas','Tilaaja')]

    for cust in data:
        query = 'INSERT INTO customer (first_name, last_name) VALUES ("%s", "%s");' %cust
        print(query)
        cursor.execute(query)

print(32*'-')

query = 'SELECT * FROM customer;'
print(query)
cursor.execute(query)
print('\nColumns:')
for column in cursor.description:
    print(column[0], end=' ') 
    
print('\nData:')
for row in cursor:
    print(row)


    
    