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
        return stats

    