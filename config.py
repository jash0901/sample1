import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-NTSH49DG;'
                      'Database=master;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM Employee')

for i in cursor:
    print(i)