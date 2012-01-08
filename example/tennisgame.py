class TennisGame(object):
    
    def __init__(self):
        self.scoreLiterals = ("0", "15", "30", "40", "adv", "wins", "loses")
        self.playerOneProgress = 0
        self.playerTwoProgress = 0
    
    def score(self):
        return self.scoreLiterals[self.playerOneProgress] + " - " + self.scoreLiterals[self.playerTwoProgress]
        
    def playerOneScores(self):
        if self.playerTwoProgress == self.scoreLiterals.index("adv"):
            self.playerTwoProgress = self.scoreLiterals.index("40")
            return
        if self.playerOneProgress == self.scoreLiterals.index("40") and self.playerTwoProgress < self.scoreLiterals.index("30"):
            self.playerOneProgress = self.scoreLiterals.index("wins")
            self.playerTwoProgress = self.scoreLiterals.index("loses")    
        else:
            self.playerOneProgress += 1
        if self.playerOneProgress == self.scoreLiterals.index("wins"):
            self.playerTwoProgress = self.scoreLiterals.index("loses")
    
    def playerTwoScores(self):
        if self.playerOneProgress == self.scoreLiterals.index("adv"):
            self.playerOneProgress = self.scoreLiterals.index("40")
            return
        if self.playerTwoProgress == self.scoreLiterals.index("40") and self.playerOneProgress < self.scoreLiterals.index("30"):
            self.playerTwoProgress = self.scoreLiterals.index("wins")
            self.playerOneProgress = self.scoreLiterals.index("loses")
        else:
            self.playerTwoProgress += 1        
        if self.playerTwoProgress == self.scoreLiterals.index("wins"):
            self.playerOneProgress = self.scoreLiterals.index("loses")
