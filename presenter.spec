import mock
from tennisgame import *
from simulator import Presenter

set up
    mock_view = mock.Mock()
    mock_model = mock.Mock()
    p = Presenter(mock_view, mock_model)
    

when ball goes over right side player one scores
    p.ballGoesOverRightSide()
    mock_model.playerOneScores.assert_called_once_with()

when ball goes over right side it gets score from model
    p.ballGoesOverRightSide()
    mock_model.score.assert_called_once_with()

when ball goes over right side it updates view with score
    mock_model.score.return_value = "15 - 0"
    p.ballGoesOverRightSide()
    mock_view.setScore.assert_called_once_with("15 - 0")

when ball goes over left side player two scores
    p.ballGoesOverLeftSide()
    mock_model.playerTwoScores.assert_called_once_with()

when ball goes over left side it gets score from model
    p.ballGoesOverLeftSide()
    mock_model.score.assert_called_once_with()

when ball goes over left side it updates view with score
    mock_model.score.return_value = "0 - 15"
    p.ballGoesOverLeftSide()
    mock_view.setScore.assert_called_once_with("0 - 15")