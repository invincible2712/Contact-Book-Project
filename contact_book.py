import mysql.connector
from mysql.connector import Error
from contact import Contact

class ContactBook:
    def __init__(self):
        self.connection = self.create_connection()

    def create_connection(self):
        try:
            connection = mysql.connector.connect(host='localhost',database='contact_book',user='root',password='Qwerty@2000')
            if connection.is_connected():
                return connection
        except Error as e:
            print(f"Error:{e}")
            return None
    
    def add_contact(self,contact):
        cursor = self.connection.cursor()
        query = "INSERT INTO contacts (name,phone,email) values(%s,%s,%s)"
        values = (contact.name,contact.phone,contact.email)
        cursor.execute(query,values)
        self.connection.commit()
        print("Contact added Successfully!")

    def display_all_contacts(self):
        cursor = self.connection.cursor(dictionary=True)
        query = "Select * from contacts"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            contact = Contact(row['name'],row['phone'],row['email'])
            contact.display_contact()
            print("----------")

    def search_contact(self,name):
        cursor = self.connec.cursor(dictionar=True)
        query = "select * from contacts where name = %s"
        cursor.execute(query,(name,))
        result = cursor.fetchone()
        if result:
            return Contact(result['name'],result['phone'],result['email'])
        return None

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed")

    