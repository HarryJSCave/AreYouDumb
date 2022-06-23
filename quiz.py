from mimetypes import init
from flask import Flask, abort, redirect, render_template, request, session
from flask_wtf import FlaskForm
from wtforms   import  SubmitField
from flask_mysqldb import MySQL
from app import mysql


class Question:
    def __init__(self, category):
        self.category = category
        self.id = 0
        self.text = ""
        self.answer = ""
        self.options = []
        self.createQuestion()

        # Indexing for the database 
        self.dbID   = 0
        self.dbtext = 1
        self.dba1   = 2
        self.dba2   = 3
        self.dba3   = 4
        self.dba4   = 5
        self.dbca   = 6

    def createQuestion(self):
        c = DatabaseConnection()
        query = "SELECT * from questions where Category = \'{}\'".format(self.category) 
        data = c.query(query)
        question =  self.getQuestionOfTheDay(self, data)
        self.text = question[self.dbtext]
        self.answer = question[self.dbca]
        self.options  = [question[self.dba1],question[self.dba2],question[self.dba3],question[self.dba4]]
    
    def alreadyAnswered(self):
        return False

    def getQuestionOfTheDay(self,data):
        return data[0]

class Result:
    def __init__(self, question, userAnswer):
        self.question = question
        self.userAnswer = userAnswer
        self.timeTaken  = 0

    def isCorrect(self):
        return  str(self.question.answer) == str(self.userAnswer)

    def sendToDatabase(self):
        c = DatabaseConnection()
        userID = session["google_id"]
        questionID = self.question.id
        query =  "INSERT INTO user_responses VALUES({}, {}, {}, {}, {}, {}, {});".format()

# put this in the 
class DatabaseConnection: 
    def __init__(self):
        self.connection = mysql.connection.cursor()

    def query(self, query):
        self.connection.execute(query)
        data = self.connection.fetchall()
        self.connection.close()
        return data