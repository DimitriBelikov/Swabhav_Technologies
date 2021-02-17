import mysql.connector as mysql

try:
    conn = mysql.connect(user='root', password='Urmil@2000',
                        host = '127.0.0.1', database='world')
    
    print('Connection '+str(conn.is_connected())+ '\n')

except Exception as ex:
    print(ex)

#Test Query-1
cursor = conn.cursor()
cursor.execute('''SELECT country.Code, country.Name, country.Population
                FROM country
                ORDER BY country.Population DESC
                LIMIT 5''')
records = cursor.fetchall()
print('{:4}\t{:10}\t{:15}'.format('Code','Country','Population'))
for record in records:
    print('{:4}\t{:10}\t{:<15}'.format(record[0], record[1], record[2]))