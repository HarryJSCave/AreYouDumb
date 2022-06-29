#
from flask import session


class UserStats:
    def __init__(self, id):
        self.id = id
        self.stats =  { "Georaphy":        self.grabStats("Geography"),
                    "Entertainment":  self.grabStats("Entertainment"), 
                    "History":        self.grabStats("History"),
                    "Art":            self.grabStats("Art"),
                    "Science":        self.grabStats("Science"),
                    "Sport":          self.grabStats("Sports")}


    
    def calcAvg(self, list):
        totalTime = 0 
        
        for time in list:
            totalTime += time[0]
        if len(list):
            return round(totalTime/len(list),1)
        else: return "0"

    def calcScore(self,list):
        score = 0 
        for time in list:
            score += 1000/(1+(time[0]*10))
        
        return round(score)

    def grabStats(self, category): 
        from database import DatabaseConnection
        c = DatabaseConnection()

        correctPlaysQ = """
SELECT TimeTaken FROM (SELECT * FROM `user_responses` WHERE UserID = \'{}\' AND Correct = 1) A 
INNER JOIN (select * from questions WHERE Category = \'{}\') B
ON A.`QuestionID` = B.`QuestionID`
""".format(session["google_id"],category) 
        
        correctPlays = c.query(correctPlaysQ)

        totalPlaysCountQ = """
SELECT  TimeTaken FROM (SELECT * FROM `user_responses` WHERE UserID = \'{}\') A 
INNER JOIN (select * from questions WHERE Category = \'{}\') B
ON A.`QuestionID` = B.`QuestionID`
""".format(session["google_id"], category) 


        plays =  c.query(totalPlaysCountQ)
        stats = {
            "plays":   len(plays),
            "totalScore": self.calcScore(correctPlays),
            "averageTime":  self.calcAvg(plays)
            
        }

        return stats

class Leaderboard:
    def __init__(self):
        self.board =  { "Georaphy":       self.getRanking("Geography"), #[playername:score]
                        "Entertainment":  self.getRanking("Entertainment"), 
                        "History":        self.getRanking("Histort"),
                        "Art":            self.getRanking("Art"),
                        "Science":        self.getRanking("Science"),
                        "Sport":          self.getRanking("Sports")}
        pass

    def getRanking(self, category):
        ranking = []
        ranking = [("first",1000),("2",5000),("3",200),("4",100), ("5",100),("6",100),("4345",100) ]
        return ranking
    