from mimetypes import init


class Question():
    def __init__(self, text, answers, category):
        self.text = text
        self.answers = answers
        self.category = category