from Tkinter import *
from tennisgame import *
import time

'''
TKinter code based on Fredrik Lundh’s A Simple Animation Engine
'''

class Presenter(object):
    
    def __init__(self, model):
        self.views = []
        self.model = model

    def ballGoesOverRightSide(self):
        try:
            self.model.playerOneScores()
        except AttributeError:
            print 'implement playerOneScores() or adapt...'
        self.updateScore()

    def ballGoesOverLeftSide(self):
        try:
            self.model.playerTwoScores()
        except AttributeError:
            print 'implement playerTwoScores() or adapt...'
        self.updateScore()

    def addView(self, view):
        self.views.append(view)

    def updateScore(self):
        score = ""
        try:
            score = self.model.score() 
            if type(score) == tuple:
                score = self._prettyPrint(score)
        except AttributeError:
            print 'implement score() or adapt'
        except:
            pass #use default value for any other error
        for view in self.views:
            view.setScore(score)

    def _prettyPrint(self, result):
        return str(result[0]) + " - " + str(result[1])        
            

class TennisBall:
    '''Draws the moving ball to canvas, takes view to inform
    when out of bounds'''
    def __init__(self, canvas, xy, color, delta, view):
        self.canvas = canvas
        self.view = view

        self.id = self.canvas.create_oval(
            -10, -10,
            10, 10,
            fill=color
            )
		
        self.canvas.move(self.id, xy[0], xy[1])
        self.delta = delta
        self.start = self.right

    def __call__(self, wins = True):
        return self.start # get things going

    def right(self, wins = True):
        '''wins is for scripted game, if True, will stop when ball has moved to right side'''
        xy = self.canvas.coords(self.id)
        if xy[2] >= self.canvas.winfo_width():
            if not wins:
                return self.left()

        if xy[2] >= self.canvas.winfo_width() + 20:
            if wins:
                self.view.ballOnTheEdge(wins)
                self.wait()
                self.canvas.move(self.id, -self.canvas.winfo_width()-20, 0)
                return self.right()
            return self.left()

        self.canvas.move(self.id, self.delta, 0)
        return self.right

    def left(self, wins = True):
        xy = self.canvas.coords(self.id)
        if xy[0] < -20:
            self.view.ballOnTheEdge(wins)
            self.wait()
            return self.right()

        self.canvas.move(self.id, -self.delta, 0)
        return self.left

    def wait(self):
        time.sleep(2)



class Simulator(object):
    def __init__(self, presenter):
        self.presenter = presenter
        self.presenter.addView(self)

        self.root = Tk()
        self.root.title("Tennis Simulator")
        self.root.resizable(0, 0)

        self.scoreframe = Frame(self.root, bd=5, relief=SUNKEN)
        self.playerOneName = Label(self.scoreframe, text="Player 1", font=("Helvetica", 16))
        self.playerTwoName = Label(self.scoreframe, text="Player 2", font=("Helvetica", 16))
        self.scoreVar = StringVar()
        self.playerScores = Label(self.scoreframe, textvariable=self.scoreVar, font=("Helvetica", 16))
        self.playerOneName.pack(side=LEFT)
        self.playerTwoName.pack(side=RIGHT)
        self.playerScores.pack(side=BOTTOM)
        self.scoreframe.pack(fill=BOTH)

        self.gameframe = Frame(self.root, bd=5, relief=SUNKEN)
        self.gameframe.pack()

        self.canvas = Canvas(self.gameframe, width=500, height=200, bd=0, highlightthickness=0, background='green')
        self.canvas.pack()

        self.net = self.canvas.create_line(250, 0, 250, 200)
        self.root.update() # fix geometry

        self.finished = False

        self.ball = TennisBall(self.canvas, (100, 100), "gold", 10, self)

        self.timeToQuit = False

        self.presenter.updateScore()
        
        # Script, True means player one wins. False player two wins.
        self.script = (True, False, True, True, True)

    def run(self):
        try:
            for scripted_win in self.script:
                wins = scripted_win
                while True and not self.timeToQuit:
                    self.ball = self.ball(wins)
                    self.updateScreen()
                    time.sleep(0.05)
                    if self.finished:
                        self.finished = False
                        break
                    
        except TclError:
            pass # avoid errors when the window is closed        

    def setScore(self, score):
        if score.find('win') != -1: #hack to end simulator and print dialog about winning player
            message = 'wins'
            if score.startswith('win'):
                message = 'Player 1 ' + message
            else:
                message = 'Player 2 ' + message
            top = Toplevel()
            top.title("FINAL RESULT")

            msg = Message(top, text=message, width=400)
            msg.pack()
            self.timeToQuit = True

        self.scoreVar.set(score)

    def ballOnTheEdge(self, wins):
        self.finished = True
        if wins:
            self.presenter.ballGoesOverRightSide()
        else:
            self.presenter.ballGoesOverLeftSide()
        self.updateScreen()
            
    def updateScreen(self):
        self.root.update_idletasks() # redraw
        self.root.update() # process events

if __name__ == '__main__':
    model = TennisGame()
    presenter = Presenter(model)
    s = Simulator(presenter)
    s.run()
