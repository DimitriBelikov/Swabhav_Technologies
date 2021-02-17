import mysql.connector as mysql

try:
    conn = mysql.connect(user='root', password='Urmil@2000',
                        host = '127.0.0.1', database='world')
    
    print('Connection '+str(conn.is_connected()))

except Exception as ex:
    print(ex)

#Test Query-1
cursor = conn.cursor()
cursor.execute('SELECT * FROM CITY')
records = cursor.fetchall()
for record in records:
    print(record)