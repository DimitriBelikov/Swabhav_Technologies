import mysql.connector as mysql

try:
    conn = mysql.connect(user='root', password='Urmil@2000',
                        host = '127.0.0.1', database='world')
    
    print('Connection '+str(conn.is_connected()))

except Exception as ex:
    print(ex)

code = input('Enter Country COde')
query = "SELECT * FROM COUNTRY WHERE CODE = '"+ code + "'"
print(query)

cursor = conn.cursor()
cursor.execute(query)
records = cursor.fetchall()

for row in records:
    print(row)