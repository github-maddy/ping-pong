from turtle import Turtle

t = Turtle()
class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.x= x
        self.y = y

        self.penup()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5,stretch_len=1)
        self.setposition(self.x,self.y)

    def go_up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(),self.new_y)

    def go_down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(),self.new_y)

    
