from mimetypes import init
from flask_wtf import FlaskForm
from wtforms   import  SubmitField
from flask_mysqldb import MySQL
from app import mysql


class Question:
    def __init__(self, category):
        self.category = category
        self.createQuestion()

    def createQuestion(self):
        c = mysql.connection.cursor()
        query = "SELECT * from questions where Category = \'{}\'".format(self.category) 
        c.execute(query)
        data = c.fetchall()
        c.close()
        print(data[0])
        self.text = data[0][0]
        self.answer = data[0][5]
        self.options  = [data[0][1],data[0][2],data[0][3],data[0][4]]
    


    def alreadyAnswered(self):
        return False



class Result:
    def __init__(self, question, userAnswer):
        self.question = question
        self.userAnswer = userAnswer
        self.timeTaken  = 0

    def isCorrect(self):
        return  str(self.question.answer) == str(self.userAnswer)
