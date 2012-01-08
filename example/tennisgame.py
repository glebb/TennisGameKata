class TennisGame(object):
    
    def __init__(self):
        self.scoreLiterals = ("0", "15", "30", "40", "adv", "wins", "loses")
        self.playerOneProgress = 0
        self.playerTwoProgress = 0
    
    def score(self):
        return self.scoreLiterals[self.playerOneProgress] + " - " + self.scoreLiterals[self.playerTwoProgress]
        
    def playerOneScores(self):
        if self._otherPlayerLosesAdvantage(1):
            return
        elif self._playerWins(1):
            return        
        else:
            self.playerOneProgress += 1
    
    def playerTwoScores(self):
        if self._otherPlayerLosesAdvantage(2):
            return
        elif self._playerWins(2):
            return
        else:
            self.playerTwoProgress += 1                
        
    def _otherPlayerLosesAdvantage(self, player):
        if player == 1 and self.playerTwoProgress == self.scoreLiterals.index("adv"):
            self.playerTwoProgress = self.scoreLiterals.index("40")
            return True
        if player == 2 and self.playerOneProgress == self.scoreLiterals.index("adv"):
            self.playerOneProgress = self.scoreLiterals.index("40")
            return True
        return False

    def _playerWins(self, player):
        if player == 1:
            if self.playerOneProgress == self.scoreLiterals.index("40") and self.playerTwoProgress < self.scoreLiterals.index("40") \
            or self.playerOneProgress == self.scoreLiterals.index("adv"):
                self.playerOneProgress = self.scoreLiterals.index("wins")
                self.playerTwoProgress = self.scoreLiterals.index("loses")
                return True
        if player == 2:
            if self.playerTwoProgress == self.scoreLiterals.index("40") and self.playerOneProgress < self.scoreLiterals.index("40") \
            or self.playerTwoProgress == self.scoreLiterals.index("adv"):
                self.playerTwoProgress = self.scoreLiterals.index("wins")
                self.playerOneProgress = self.scoreLiterals.index("loses")
                return True
        return False


