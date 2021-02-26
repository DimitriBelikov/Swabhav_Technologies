import mysql.connector as mysql

class contact_services:
    def __init__(self):
        self.database = None
        self.connect_database()
        self.create_table()
        self.total_contacts = self.count_contacts()

    def connect_database(self): #Connects to Database and returns database object
        try:
            self.database = mysql.connect(user='root', password='Urmil@2000',
                        host = '127.0.0.1')
            print('Connection '+ str(self.database.is_connected()))
        
            cursor = self.database.cursor()
            cursor.execute('CREATE DATABASE IF NOT EXISTS Contact_DB')
            cursor.execute('USE Contact_DB')

        except Exception as ex:
            print(ex)
        
    def create_table(self): #Create Table if Not Exists or if Database gets deleted
        cursor = self.create_cursor()

        cursor.execute(''' CREATE TABLE IF NOT EXISTS profile_data(
            id INT NOT NULL,
            f_name VARCHAR(20) NOT NULL,
            l_name VARCHAR(30) NOT NULL,
            organization VARCHAR(30),
            PRIMARY KEY(id)
        )''')

        cursor.execute(''' CREATE TABLE IF NOT EXISTS user_address(
            user_id INT NOT NULL,
            pincode VARCHAR(6) NOT NULL,
            city VARCHAR(20) NOT NULL,
            state VARCHAR(20) NOT NULL,
            PRIMARY KEY(user_id, pincode),
            FOREIGN KEY (user_id) REFERENCES profile_data(id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
        ) ''')

        cursor.execute(''' CREATE TABLE IF NOT EXISTS user_contact(
            user_id INT NOT NULL,
            contact_no VARCHAR(10) NOT NULL,
            PRIMARY KEY(user_id, contact_no),
            FOREIGN KEY (user_id) REFERENCES profile_data(id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
        ) ''')

    def count_contacts(self): #Counts Number of contacts in Book
        cursor = self.create_cursor()
        cursor.execute('SELECT COUNT(*) FROM profile_data')
        return cursor.fetchone()[0]
    
    def create_cursor(self): #Create Cursor for Database
        return self.database.cursor()
    
    def insert_profile(self, profile_data):
        cursor = self.create_cursor()

        profile_query = ('''INSERT INTO profile_data (id, f_name, l_name, organization)
                        VALUES (%(id)s,%(f_name)s,%(l_name)s,%(organization)s)''')
        cursor.execute(profile_query,{'id':self.total_contacts + 1,'f_name':profile_data[0], 'l_name':profile_data[1],
                                    'organization':profile_data[2]})
        self.total_contacts += 1
        
        self.database.commit()

    def insert_contact(self, profile_data, number_data, address_data):
        self.insert_profile(profile_data)
        self.insert_contact_address(address_data, number_data)
    
    def insert_contact_address(self, address_data, number_data):
        cursor = self.create_cursor()

        contact_query = ('''INSERT INTO user_contact (user_id, contact_no)
                    VALUES (%(user_id)s, %(contact_no)s)''')
        address_query = ('''INSERT INTO user_address (user_id, pincode, city, state)
                    VALUES (%(user_id)s, %(pincode)s, %(city)s, %(state)s)''')
        
        for number in number_data:
            cursor.execute(contact_query, {'user_id':self.total_contacts, 'contact_no':number})
        
        for address in address_data:
            cursor.execute(address_query, {'user_id':self.total_contacts, 'pincode':address[0],'city':address[1],'state':address[2]})
        
        self.database.commit()

    def retrive_one(self, user_id): #Fetches Data From Conact Book
        cursor = self.create_cursor()

        cursor.execute('SELECT * FROM profile_data WHERE id = %(user_id)s',{'user_id':user_id})
        record = cursor.fetchone()
        #Fetch User Contacts and Address for each User
        cursor.execute('SELECT contact_no FROM user_contact WHERE user_id = %(user_id)s',{'user_id':user_id})
        contacts = cursor.fetchall()
        record += tuple(contacts)

        cursor.execute('SELECT city, state, pincode FROM user_address WHERE user_id = %(user_id)s',{'user_id':record[0]})
        address = cursor.fetchall()
        record += tuple(address)
        
        return record
    
    def retrive_all(self):
        cursor = self.create_cursor()
        records = []

        #Fetch User ID's
        cursor.execute('SELECT id FROM profile_data')
        user_ids = cursor.fetchone()

        for user_id in user_ids:
            records.append(self.retrive_one(user_id))
        
        return records

    def delete_records(self, user_ids):
        cursor = self.create_cursor()
        if user_ids[0] != 'all':
            for user_id in user_ids:
                cursor.execute('DELETE FROM profile_data AS t1 WHERE t1.id = %(id)s',{'id':user_id})
    
        else:
            cursor.execute('DELETE FROM profile_data')
        
        self.database.commit()


k = contact_services()
print(k.retrive_all())