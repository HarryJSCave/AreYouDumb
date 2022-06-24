from mimetypes import init
from MySQLdb import Date
from flask import Flask, abort, redirect, render_template, request, session
from flask_wtf import FlaskForm
from wtforms   import  SubmitField
from flask_mysqldb import MySQL
from app import mysql
import util
from database import DatabaseConnection

import datetime

import time


class Question:
    def __init__(self,d category):
        # Indexing for the database 
        self.dbID   = 0
        self.dbtext = 1
        self.dba1   = 2
        self.dba2   = 3
        self.dba3   = 4
        self.dba4   = 5
        self.dbca   = 6
        
        # 
        self.category = category
        self.id = 0
        self.text = ""
        self.answer = ""
        self.options = []
        self.createQuestion()

        

    def createQuestion(self):
        c = DatabaseConnection()
        query = "SELECT * from questions where Category = \'{}\'".format(self.category) 
        data = c.query(query)
        question =  self.getQuestionOfTheDay(data)
        self.text = question[self.dbtext]
        self.answer = question[self.dbca]
        self.options  = [question[self.dba1],question[self.dba2],question[self.dba3],question[self.dba4]]
    
    def alreadyAnswered(self):
        return False

    def getQuestionOfTheDay(self,data):
        date = datetime.date.today()
        dateNum = self.convertDateToNum(date)
        questionNum =  (len(data)-1)%dateNum
        return data[questionNum]

    def convertDateToNum(self, date):
        return date.day + date.month + date.year 

class Result:
    def __init__(self, question, userAnswer, time):
        self.question = question
        self.userAnswer = userAnswer
        self.timeTaken  = time
        self.date = datetime.date.today()

    def isCorrect(self):
        return  str(self.question.answer) == str(self.userAnswer)

    def sendToDatabase(self):
        c = DatabaseConnection()
        userID = session["google_id"]
        questionID = self.question.id
        anwser = self.userAnswer
        time = self.timeTaken
        print(self.date)
        date =self.date
        correct = util.boolToBit(self.isCorrect())
        
        query =  "INSERT INTO user_responses (`UserID`, `QuestionID`, `Answer`, `TimeTaken`, `DateTaken`, `Correct`) VALUES ({}, {}, \'{}\', \'{}\', \'{}\', b\'{}\');".format(userID, questionID, anwser, time, date, correct)
        c.insert(query)

       
