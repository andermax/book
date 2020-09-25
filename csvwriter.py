import pyodbc
import csv
outputFile = 'output/access_card_report.csv'

sql = (r'select tuser.id as ID, '
       r'tuser.name as Name, '
       r'tuser.cardnum as Card, '
       r'tuser.remark as Issue, '
       r'tgroup.name as Access, '
       r'tuser.company as Department, '
       r'tuser.dept as Company '
       r'from tuser left join tgroup on tuser.group_id = tgroup.id  '
       r'order by tuser.name;')

conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=data\FPMS.mdb;'
    r'PWD=fdmsamho;'
)
data = conn.cursor()
data.execute(sql)
for row in data:
            print( '|', row[0], '|', row[1], '|', row[2], '|', row[3], '|', row[4], '|', row[5], '|', row[6])


csv.register_dialect('unixpwd', delimiter=';', quoting=csv.QUOTE_NONE)
with open(outputFile, 'w', newline='') as file_object:
    writer = csv.writer(file_object)
    writer.writerows(data)

