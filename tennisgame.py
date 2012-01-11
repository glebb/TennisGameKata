class TennisGame(object):
    
    def __init__(self):
        self.scores = (0, 15, 30, 40, "deuce", "advantage", "wins")
        self.playerOneScore = 0
        self.playerTwoScore = 0

    def score(self):
        return (self.scores[self.playerOneScore], self.scores[self.playerTwoScore])

    def playerOneScores(self):
        self.playerOneScore += 1
        self.deuce()
        if self.checkIfAdvantage():
            self.playerTwoScore -= 1
            

    def playerTwoScores(self):
        self.playerTwoScore += 1
        self.deuce()
        if self.checkIfAdvantage():
            self.playerOneScore -= 1
        
    def deuce(self):
        if self.playerOneScore == 3 and self.playerTwoScore == 3:
            self.playerOneScore += 1
            self.playerTwoScore += 1

    def checkIfAdvantage(self):
        if self.playerOneScore == 5 or self.playerTwoScore == 5:
            return True
        if self.playerOneScore == 4 and self.playerTwoScore < 4:
            self.playerOneScore +=2
        if self.playerTwoScore == 4 and self.playerOneScore < 4:
            self.playerOneScore +=2
        else:
            return False
    
