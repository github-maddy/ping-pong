from selectors import SelectorKey
from turtle import Turtle, delay
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.shapesize(0.8)
        self.move_speed = 0.1
        
        self.x_move = 10
        self.y_move = 10
    def move(self):
        self.penup()
        self.new_x = self.xcor()+ self.x_move
        self.new_y = self.ycor()+ self.y_move
        self.goto(self.new_x,self.new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed  = 0.1
        



        


