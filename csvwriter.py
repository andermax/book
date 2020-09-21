import pyodbc
import csv
filename = 'report2.csv'

sql = (r'select tuser.id as ID, '
       r'tuser.name as Name, '
       r'tuser.cardnum as Card, '
       r'tuser.remark as Issue, '
       r'tgroup.name as Access, '
       r'tuser.company as Department, '
       r'tuser.dept as Company '
       r'from tuser left join tgroup on tuser.group_id = tgroup.id  '
       r'order by tuser.name;')
sql2 = ('select tuser.id as ID, tuser.name AS Employee, tuser.cardnum AS Card, tuser.company AS Departament, tuser.dept AS Company, tuser.remark AS Jira, tgroup.name AS Group from tuser inner join tgroup ON tgroup.id = tuser.group_id where dept Like "EU" order by tuser.name ASC')
conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=data\FPMS.mdb;'
    r'PWD=fdmsamho;'
)
data = conn.cursor()
data.execute(sql2)
csv.register_dialect('unixpwd', delimiter=';', quoting=csv.QUOTE_NONE)
with open(filename, 'w', newline='') as file_object:
    writer = csv.writer(file_object)
    writer.writerows(data)


