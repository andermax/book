import pyodbc
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Ron\Desktop\Test\testdb.accdb;')
cursor = conn.cursor()
cursor.execute('select * from tracking_sales')

for row in cursor.fetchall():
    print(row)
