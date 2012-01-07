from tennisgame import *

def setScores(game, winsForP1, winsForP2):
    for i in range (0, winsForP1):
        game.playerOneScores()
    for i in range (0, winsForP2):
        game.playerTwoScores()

set up
    game = TennisGame()
        

score is 15 0 afeter playerOne scores
    game.playerOneScores()
    game.score() == "15 - 0"

game starts from zero zero    
    game.score() == "0 - 0"

score is 30 0 after player one scores twice
    setScores(game, 2, 0)
    game.score() == "30 - 0"

player one wins scoring once after 40 0
    setScores(game, 4, 0)
    game.score() == "wins - loses"

player one gains advantage
    setScores(game, 3, 3)
    game.playerOneScores()
    game.score() == "adv - 40"

player one loses advantage
    setScores(game, 3, 3)    
    setScores(game, 1, 1)    
    game.score() == "40 - 40"

player one loses advantage and player two wins
    setScores(game, 3, 3)    
    game.playerOneScores()
    setScores(game, 0, 3)    
    game.score() == "loses - wins"
