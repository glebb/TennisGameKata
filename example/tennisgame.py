class TennisGame(object):
    
    def __init__(self):
        self.result = "0 - 0"
        self.scoreValues = ("0", "15", "30", "40", "adv", "wins", "loses")
        self.scoresForPlayerOne = 0
        self.scoresForPlayerTwo = 0
    
    def score(self):
        return self.scoreValues[self.scoresForPlayerOne] + " - " + self.scoreValues[self.scoresForPlayerTwo]
        
    def playerOneScores(self):
        if self.scoresForPlayerTwo == 4:
            self.scoresForPlayerTwo -= 1
            return
        if self.scoresForPlayerOne == 3 and self.scoresForPlayerTwo < 3:
            self.scoresForPlayerOne += 2
            self.scoresForPlayerTwo = 6    
        else:
            self.scoresForPlayerOne += 1
        if self.scoresForPlayerOne == 5:
            self.scoresForPlayerTwo = 6
    
    def playerTwoScores(self):
        if self.scoresForPlayerOne == 4:
            self.scoresForPlayerOne -= 1
            return
        if self.scoresForPlayerTwo == 3 and self.scoresForPlayerOne < 3:
            self.scoresForPlayerTwo += 2
            self.scoresForPlayerOne = 6
        else:
            self.scoresForPlayerTwo += 1        
        if self.scoresForPlayerTwo == 5:
            self.scoresForPlayerOne = 6