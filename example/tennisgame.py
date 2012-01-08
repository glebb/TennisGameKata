class TennisGame(object):
    def __init__(self):
        self.scoreLiterals = ("0", "15", "30", "40", "wins", "loses", "adv")
        self.playerTwoProgress = 0
        self.playerOneProgress = 0

    def score(self):
        self._fixPlayerProgressInCaseOfAdvantage()
        self._fixPlayerProgressInCaseOfWin()
        return self.scoreLiterals[self.playerOneProgress] + " - " + self.scoreLiterals[self.playerTwoProgress]

    def playerOneScores(self):
        self.playerOneProgress += 1

    def playerTwoScores(self):
        self.playerTwoProgress += 1

    def _fixPlayerProgressInCaseOfWin(self):
        winner = self._playerShouldWin(self.playerOneProgress, self.playerTwoProgress)
        if winner == 1:
            self.playerTwoProgress = 5
            self.playerOneProgress = 4
        elif winner == 2:
            self.playerOneProgress = 5
            self.playerTwoProgress = 4

    def _fixPlayerProgressInCaseOfAdvantage(self):
        if self._playerShouldLoseAdvantage(self.playerOneProgress, self.playerTwoProgress):
            self.playerTwoProgress = 3
            self.playerOneProgress = 3

        advantages = self._playerShouldGainAdvantage(self.playerOneProgress, self.playerTwoProgress)
        if advantages == 1:
            self.playerOneProgress = 6
            self.playerTwoProgress = 3
        elif advantages == 2:
            self.playerTwoProgress = 6
            self.playerOneProgress = 3
        
    
    def _playerShouldWin(self, progress1, progress2):
        if progress1 == 4 and progress2 < 3:
            return 1
        elif progress2 == 4 and progress1 < 3:
            return 2
        elif progress1 == 5 and progress2 == 3:
            return 1
        elif progress2 == 5 and progress1 == 3:
            return 2
    
    def _playerShouldGainAdvantage(self, progress1, progress2):
        if progress1 == 4 and progress2 == 3:
            return 1
        elif progress2 == 4 and progress1 == 3:
            return 2

    def _playerShouldLoseAdvantage(self, progress1, progress2):
        if progress1 == 4 and progress2 == 4:
            return True
        else:
            return False