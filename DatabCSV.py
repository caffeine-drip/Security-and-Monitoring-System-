import sqlite3
import csv


conn = sqlite3.connect('DB/datab2.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM fulldb')
names = list(map(lambda x: x[0], cursor.description))
data=list()
data.append(names)
for row in cursor:
    data.append(list(row))
print data
myFile = open('CSV/DataBase.csv', 'w+')  
with myFile:  
    writer = csv.writer(myFile)
    writer.writerows(data)


conn.close()
