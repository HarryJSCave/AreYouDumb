from flask import  session
import util
from database import DatabaseConnection
import datetime
import random


class Question:
    def __init__(self, category):
        # Indexing for the database 
        self.dbID   = 0
        self.dbtext = 1
        self.dba1   = 2
        self.dba2   = 3
        self.dba3   = 4
        self.dba4   = 5
        self.dbca   = 6
        
        # just the defualts
        self.category = category
        self.id = 0
        self.text = "Error"
        self.answer = "Error"
        self.options = [" ", " ", " ", " "]
        self.createQuestion()


    def createQuestion(self):
        c = DatabaseConnection()
        query = "SELECT * from questions where Category = \'{}\'".format(self.category) 
        data = c.query(query)
        # only runs if there is no error
        if len(data) != 0: 
            question =  self.getQuestionOfTheDay(data)
            self.id   = question[self.dbID]
            self.text = question[self.dbtext]
            self.answer = question[self.dbca]
            self.options  = [question[self.dba1],question[self.dba2],question[self.dba3],question[self.dba4]]
    
    def alreadyAnswered(self):
        # uncomment if you want to test
        #return False
        c = DatabaseConnection()
        query = "SELECT count(*) from user_responses where QuestionID = \'{}\' and DateTaken = \'{}\'".format(self.id, datetime.date.today()) 
        count = c.query(query)
        if (count[0][0] != 0): return True
        else: return False

    def getQuestionOfTheDay(self, data):
        date = datetime.date.today()
        dateNum = self.convertDateToNum(date)
        questionNum =  dateNum%(len(data))
        return data[questionNum]

    def convertDateToNum(self, date):
        return int(str(date.year) + str(date.month) + str(date.day))
        

class Result:
    def __init__(self, question, userAnswer, time):
        self.question = question
        self.userAnswer = userAnswer
        self.timeTaken  = time
        self.date = datetime.date.today()

    def isCorrect(self):
        return  str(self.question.answer) == str(self.userAnswer)
    
    def getSentiment(self):
        if self.isCorrect(): return "P"
        else: return "N"

    def calcScore(self):
        if self.isCorrect():
            return round(1000/(1+(float(self.timeTaken)*5)))
        else:
            return 0

    def getResponse(self):
        c = DatabaseConnection()
        query = "SELECT ResponseText from question_responses where Sentiment = \'{}\'".format(self.getSentiment()) 
        data = c.query(query)
        index = random.randint(1, len(data))-1
        return data[index][0]

    def sendToDatabase(self):
        c = DatabaseConnection()
        userID = session["google_id"]
        questionID = self.question.id
        anwser = self.userAnswer
        time = self.timeTaken
        date =self.date
        correct = util.boolToBit(self.isCorrect())
        query =  "INSERT INTO user_responses (UserID, QuestionID, Answer, TimeTaken, DateTaken, Correct) VALUES ({}, {}, \'{}\', \'{}\', \'{}\', b\'{}\');".format(userID, questionID, anwser, time, date, correct)
        c.insert(query)

