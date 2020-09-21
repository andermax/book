import pyodbc
import csv
filename = 'report.csv'

sql = ('select tuser.id as ID, tuser.name as Name, tuser.cardnum as Card, tuser.remark as Issue, tgroup.name as Access, tuser.company as Department, tuser.dept as Company from tuser left join tgroup on tuser.group_id = tgroup.id order by tuser.name;')
conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=data\FPMS.mdb;'
    r'PWD=fdmsamho;'
)
cursor = conn.cursor()
cursor.execute(sql)

with open(filename, 'w') as file_object:
    writer = csv.writer(file_object)
    for row in cursor:
        writer.writerow(row)