import mysql.connector as mysql

try:
    conn = mysql.connect(user='root', password='Urmil@2000',
                        host = '127.0.0.1', database='world')
    
    print('Connection '+str(conn.is_connected()))

except Exception as ex:
    print(ex)

finally:
    if conn.is_connected():
        conn.close()
    print('Connection closed')