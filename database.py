from flask import session
from app import mysql

# put this in the database.py and fix 
class DatabaseConnection: 
    def __init__(self):
        sql = "sql"

    def query(self, query):
        print(query)
        try:
            self.cursor = mysql.connection.cursor()
            self.cursor.execute(query)
            data = self.cursor.fetchall()
        except mysql.connection.Error as error:
            print("Failed to query MySQL table {}".format(error))
            data = []
        finally:
            self.cursor.close()
            return data
    
    def insert(self, query):
        print(query)
        try:
            self.cursor = mysql.connection.cursor()
            self.cursor.execute(query)
            mysql.connection.commit()
        except mysql.connection.Error as error:
            print("Failed to insert into MySQL table {}".format(error))
        finally:
            self.cursor.close()