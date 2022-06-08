from mimetypes import init
from flask_wtf import FlaskForm
from wtforms   import  SubmitField


class Question:
    def __init__(self, text, answer, options,category):
        self.text = text
        self.answer = answer
        self.options = options
        self.category = category

    
    
        
class QuestionForm(FlaskForm):
    selection = SubmitField('Question')

