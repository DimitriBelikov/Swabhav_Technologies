import mysql.connector as mysql

try:
    conn = mysql.connect(user='root', password='Urmil@2000',
                        host = '127.0.0.1', database='test')
    
    print('Connection '+str(conn.is_connected()))

except Exception as ex:
    print(ex)

cursor = conn.cursor()
cursor.execute('SELECT COUNT(*) FROM test_tb')
records = cursor.fetchone()
print(records)