from database import DatabaseConnection

class UserStats:
    def __init__(self, id):
        self.id = id
        self.stats =  { "Georaphy":        self.grabStats("Geography"),
                    "Entertainment":  self.grabStats("Entertainment"), 
                    "History":        self.grabStats("Histort"),
                    "Art":            self.grabStats("Art"),
                    "Science":        self.grabStats("Science"),
                    "Sport":          self.grabStats("Sports")}


    
    def calcAvg():
        return 0

    def calcScore():
        return 0

    def grabStats(self, category): 
        stats = {
            "numOfTries":   12,
            "totalScore": 10000,
            "averageTime":  6.56
            }

        c = DatabaseConnection()
        query = "SELECT * from questions where Category = \'{}\'".format(self.category) 
        
        data = c.query(query)
        return stats

class Leaderboard:
    def __init__(self):
        self.board =  { "Georaphy":        self.getRanking("Geography"), #[playername:score]
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
    