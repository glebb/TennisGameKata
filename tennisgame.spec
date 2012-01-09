from tennisgame import *

def setScores(game, scoresForP1, scoresForP2):
    for i in range(0,scoresForP1):
        game.playerOneScores()
    for i in range(0,scoresForP2):
        game.playerTwoScores()

set up
    game = TennisGame()

game starts from 0 0
    game = TennisGame()
    game.score() == "0 - 0"

score is 15 0 when player one scores once
    game.playerOneScores()
    game.score() == "15 - 0"

score is 0 15 when palyer two scores once
    game.playerTwoScores()
    game.score() == "0 - 15"

score is 0 30 when player two scores twice
    setScores(game, 0, 2)
    game.score() == "0 - 30"

score progresses to 40 40
    setScores(game, 3, 3)
    game.score() == "40 - 40"    

player one wins
    setScores(game, 4, 0)
    game.score() == "wins - loses"    

player two wins
    setScores(game, 0, 4)
    game.score() == "loses - wins"    

player one gains advantage
    setScores(game, 3, 3)
    game.playerOneScores()
    game.score() == "adv - 40"

player two gains advantage
    setScores(game, 3, 3)
    game.playerTwoScores()
    game.score() == "40 - adv"

player two wins after advantage
    setScores(game, 3, 3)
    game.playerTwoScores()
    game.playerTwoScores()
    game.score() == "loses - wins"

player two loses advantage
    setScores(game, 3, 3)
    game.playerTwoScores()
    game.playerOneScores()
    game.score() == "40 - 40"

player one loses advantage
    setScores(game, 3, 3)
    game.playerOneScores()
    game.playerTwoScores()
    game.score() == "40 - 40"

