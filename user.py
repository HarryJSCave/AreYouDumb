#
from ast import Return
from itertools import count
from flask import session


class User:
    def __init__(self, id, name):
        self.id = id 
        self.name = name 

    def addUserToDatabase(self): 
        from database import DatabaseConnection
        c = DatabaseConnection()
        q = """INSERT INTO users (GoogleID, Username)
                VALUES ({}, \'{}\')
                ON DUPLICATE KEY UPDATE Username = \'{}\'""".format(self.id,self.name,self.name) 
        c.insert(q)


#stats = {
#            "plays":   len(plays),
#            "totalScore": self.calcScore(category),
#            "averageTime":  self.calcAvg(plays)
#        }        
        

class UserStats:
    def __init__(self, id):
        
        
        self.id = id
        self.stats =  { "Geography":          self.grabStats("Geography"),
                        "Entertainment":      self.grabStats("Entertainment"), 
                        "History":            self.grabStats("History"),
                        "Art & Literature":   self.grabStats("Art"),
                        "Science":            self.grabStats("Science"),
                        "Sport":              self.grabStats("Sports")}
        self.updateLeaderboardDatabase()

    def  entryExists(self, category):
        from database import DatabaseConnection
        c = DatabaseConnection()
        query = "SELECT COUNT(*) from leaderboard where Category = \'{}\' AND UserID = {}".format(category, self.id) 
        count = c.query(query)
        if (count[0][0] != 0): return True
        else: return False

    def updateLeaderboardDatabase(self):
        from database import DatabaseConnection
        c = DatabaseConnection()

        for category in self.stats:
            
            entryExists = self.entryExists(category)
            if (entryExists):
                query =  """UPDATE `leaderboard`
                            SET `TotalScore`= {}, `AverageTime` = {}, `TotalPlays` = {}
                            WHERE UserID = \'{}\' AND Category = \'{}\'  ;""".format(self.stats[category]['totalScore'], self.stats[category]['averageTime'], self.stats[category]['plays'], self.id, category)
                c.insert(query)
            else:
                query =  """INSERT INTO `leaderboard` (`UserID`, `TotalScore`, `AverageTime`, `TotalPlays`, `Category`) 
                VALUES (\'{}\', {}, {}, {}, \'{}\');""".format(self.id, self.stats[category]['totalScore'], self.stats[category]['averageTime'], self.stats[category]['plays'], category)
                c.insert(query)

    def calcAvg(self, list):
        totalTime = 0 
        
        for time in list:
            totalTime += time[0]
        if len(list):
            return round(totalTime/len(list),1)
        else: return "0"

    def calcScore(self, category):
        from database import DatabaseConnection
        c = DatabaseConnection()
        score = 0 

        correctPlaysQ = """
                        SELECT TimeTaken FROM (SELECT * FROM `user_responses` WHERE UserID = {} AND Correct = 1) A 
                        INNER JOIN (select * from questions WHERE Category = \'{}\') B
                        ON A.`QuestionID` = B.`QuestionID`
                        """.format(session["google_id"],category) 
        
        correctPlays = c.query(correctPlaysQ)
        for time in correctPlays:
            score += 1000/(1+(time[0]*5))
        
        return round(score)


    def grabStats(self, category): 
        from database import DatabaseConnection
        c = DatabaseConnection()

        totalPlaysCountQ = """
                            SELECT  TimeTaken FROM (SELECT * FROM `user_responses` WHERE UserID = {}   ) A 
                            INNER JOIN (select * from questions WHERE Category = \'{}\') B
                            ON A.`QuestionID` = B.`QuestionID`
                            """.format(session["google_id"], category) 


        plays =  c.query(totalPlaysCountQ)
        stats = {
            "plays":   len(plays),
            "totalScore": self.calcScore(category),
            "averageTime":  self.calcAvg(plays)
        }
        return stats





class Leaderboard:
    def __init__(self):
        self.board =  { "Geography":       self.getRanking("Geography"), #[playername:score]
                        "Entertainment":  self.getRanking("Entertainment"), 
                        "History":        self.getRanking("History"),
                        "Art":            self.getRanking("Art & Literature"),
                        "Science":        self.getRanking("Science"),
                        "Sport":          self.getRanking("Sport")}
        pass

    # gets the user name for the leader board
    def getUsername(self, userID):
        from database import DatabaseConnection
        c = DatabaseConnection()
        q = """ SELECT Username FROM users WHERE  GoogleID = \'{}\'
                        """.format(userID) 
        data = c.query(q)
        return data[0][0]

    # gets the leader board ranking for the a cataegory 
    def getRanking(self, category):
        from database import DatabaseConnection
        c = DatabaseConnection()
        q = """ SELECT TotalScore, UserID FROM leaderboard WHERE  Category = \'{}\'
                        """.format(category) 
        data = c.query(q)
        ranking= []
        for user in data: 
            entry = (self.getUsername(user[1]), user[0])
            ranking.append(entry)
     
        if (len(ranking) < 4):
            # dumby data for if there are no players should really put this in the sql 
            ranking.append(("Hero",14000))
            ranking.append(("Noob",100))
            ranking.append(("WhatsMyName",50))
            ranking.append(("Xen",2000))
            ranking.append(("Xen2.0",4000))
        self.sortRanking(ranking)
        return ranking

    # actully sorts the list using a merge sort 
    def sortRanking(self, ranking):
        if len(ranking) > 1: 
            # Finding the mid of the array
            mid = len(ranking)//2
            # Dividing the array elements
            L = ranking[:mid]
            # into 2 halves
            R = ranking[mid:]
            # Sorting the first half
            self.sortRanking(L)
            # Sorting the second half
            self.sortRanking(R)
            i = j = k = 0
            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i][1] > R[j][1]:
                    ranking[k] = L[i]
                    i += 1
                else:
                    ranking[k] = R[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(L):
                ranking[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                ranking[k] = R[j]
                j += 1
                k += 1

        

