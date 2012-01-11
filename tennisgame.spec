from tennisgame import *

def playerStartScores(playerOne, playerTwo, game):
    [game.playerOneScores() for x in range(playerOne)]
    [game.playerTwoScores() for x in range(playerTwo)]
        


set up
    game = TennisGame()

when game start score is 0 0
    game.score() == (0, 0)

at game start player one scores game is 15 0
    playerStartScores(1,0,game)
    game.score() == (15, 0)

at game start player two scores game is 0 15
    playerStartScores(0,1,game)
    game.score() == (0, 15)

when player two scores twice game is 0 30
    playerStartScores(0,2,game)
    game.score() == (0, 30)

when player one scores three and player two scores three game is deuce deuce
    playerStartScores(3,3,game)
    game.score() == ("deuce", "deuce")

when player one scores four and player two scores three game is adv 40
    playerStartScores(3,3,game)
    game.playerOneScores()
    game.score() == ("advantage", 40)

when player one advantage and player two wins game is deuce
    playerStartScores(3,3,game)
    game.playerOneScores()
    game.playerTwoScores()
    game.score() == ("deuce", "deuce")

when player one advantage and wins game is wins 40
    playerStartScores(3,3,game)
    game.playerOneScores()
    game.playerOneScores()
    game.score() == ("wins", 40)

when player one wins four balls player one wins
    playerStartScores(4,0,game)
    game.score() == ("wins", 0)
