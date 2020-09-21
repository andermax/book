import pyodbc
def get_dbconn(file, password):
    pyodbc.pooling = False
    driver = '{Microsoft Access Driver (*.mdb)}'
    dbdsn = f'Driver={driver};Dbq={file};'
    if password:
        dbdsn += f'Pwd={password};'
    return pyodbc.connect(dbdsn)