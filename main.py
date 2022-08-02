from turtle import Turtle,Screen
import paddle
import ball
import time
from scoreboard import Scoreboard
#screen setup
wn = Screen()
wn.setup(height=600,width=800)
wn.bgcolor("black")
wn.title("PONG")
wn.tracer(0)

right_paddle = paddle.Paddle(350,0)
left_paddle = paddle.Paddle(-350,0)

scoreboard = Scoreboard()

wn.listen()
wn.onkey(right_paddle.go_up,"Up")
wn.onkey(right_paddle.go_down,"Down")
wn.onkey(left_paddle.go_up,"w")
wn.onkey(left_paddle.go_down,"s")

ball = ball.Ball()



is_on = True
while is_on:
    time.sleep(ball.move_speed) 
    wn.update()

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle)<50 and ball.xcor()>320 or ball.distance(left_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.l_update()

    
    if ball.xcor() < -380:
        ball.reset_position()
        ball.bounce_y()
        scoreboard.r_update()


wn.exitonclick()




