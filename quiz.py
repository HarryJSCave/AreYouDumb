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

    def getQuestionOfTheDay(self,data):
        date = datetime.date.today()
        dateNum = self.convertDateToNum(date)
        questionNum =  (len(data)-1)%dateNum
        print(len(data)-1)
        print(questionNum)
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
    
    def getSentiment(self):
        if self.isCorrect(): return "P"
        else: return "N"

    def getResponse(self):
        c = DatabaseConnection()
        query = "SELECT ResponseText from question_responses where Sentiment = \'{}\'".format(self.getSentiment()) 
        data = c.query(query)
        print(data)
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

       
def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1