from mimetypes import init
from MySQLdb import Date
from flask import Flask, abort, redirect, render_template, request, session
from flask_wtf import FlaskForm
from wtforms   import  SubmitField
from flask_mysqldb import MySQL
from app import mysql




# put this in the database.py and fix 
class DatabaseConnection: 
    def __init__(self):
        sql = "sql"

    def query(self, query):
        self.cursor = mysql.connection.cursor()
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        self.cursor.close()
        return data
    
    def insert(self, query):
        print(query)
        try:
            self.cursor = mysql.connection.cursor()
            self.cursor.execute(query)
            mysql.connection.commit()
        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))
        finally:
            self.cursor.close()