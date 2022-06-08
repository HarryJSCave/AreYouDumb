from mimetypes import init
from flask_wtf import FlaskForm
from wtforms   import  SubmitField
#import pyodbc

# Trusted Connection to Named Instance
# PLEASE DON'T CHANGE ANY OF THIS FOR NOW OR I MIGHT CRY
#connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=.\SQLEXPRESS;INITIALCATALOG=DESKTOP-IA2HB36\grace\DC2060;Trusted_Connection=yes;')
#print("connected")
#cursor=connection.cursor()
#print("cursor created")

# At the moment just selects the entire table of questions
# Currently trying to figure out how to get it to select a particular row with no ID or primary key
#cursor.execute("SELECT * FROM DC2060.dbo.questions")
#for row in cursor.fetchall():
#    print(row)


# Close connection
#cursor.close()
#connection.close()

class Question:
    def __init__(self, category):
        self.category = category
        self.createQuestion()

    def createQuestion(self):
       self.text = "what is 1+1"
       self.answer = 2
       self.options  = ["1","2","3","I give up on Life"]



class Result:
    def __init__(self, question, userAnswer):
        self.question = question
        self.userAnswer = userAnswer 
        self.timeTaken  = 0
    
    def isCorrect(self):
        return  str(self.question.answer) == str(self.userAnswer)


        



    

