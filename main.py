from TextFiles import Readfile
import pyodbc


sql = (r'select tuser.id as ID, '
       r'tuser.name as Name, '
       r'tuser.cardnum as Card, '
       r'tuser.remark as Issue, '
       r'tgroup.name as Access, '
       r'tuser.company as Department, '
       r'tuser.dept as Company '
       r'from tuser left join tgroup on tuser.group_id = tgroup.id  '
       r'order by tuser.name;')




def dbconnect(sql):
    conn = pyodbc.connect(
        r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=data/FPMS.mdb;'
        r'PWD=fdmsamho;'
    )
    data = conn.cursor()
    data.execute(sql)
    return data

def readFile(self,link):
    with open(link) as file_object:
        for line in file_object:
            print(line.rstrip())


def writeFile(self, data, link):
    with open(link, 'w') as file_object:
        file_object.write(data)

data = dbconnect(sql)
counter =0
branch = 'BANK'

for row in data:
        if branch in row[6]:
            counter += 1
            print('|', counter, '|', row[0], '|', row[1], '|', row[2], '|', row[3], '|', row[4], '|', row[5], '|',
                  row[6])