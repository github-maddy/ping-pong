from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_paddle = 0
        self.l_paddle = 0
        self.update()

    def update(self):
        self.goto(-100,200)
        self.write(self.l_paddle,align="center",font=("courier",50,"normal"))

        self.goto(100,200)
        self.write(self.r_paddle,align="center",font=("courier",50,"normal"))

    def l_update(self):
        self.l_paddle+=1
        self.clear()
        self.update()

    def r_update(self):
        self.r_paddle+=1
        self.clear()
        self.update()
