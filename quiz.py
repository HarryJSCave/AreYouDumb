from mimetypes import init


class Quiz:
    def __init__(self) -> None:
        pass

class Question:
    
    def __init__(self, text, answer, options,category):
        self.text = text
        self.answer = answer
        self.options = options
        self.category = category

