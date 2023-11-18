from turtle import Turtle,Screen
from paddle import Paddle
from  ball import Ball
from scoreboard import Scoreboard
import time
POSITIONS=[(-350,0),(350,0)]
screen=Screen()
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
screen.setup(width=800,height=600)
left_paddle=Paddle(POSITIONS[0])
right_paddle=Paddle(POSITIONS[1])
ball=Ball()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")
screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down,"s")
game_is_on=True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    #to detect collision with the wall:
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.ybounce()
    #to detect collision with the one of the paddles:
    if (ball.distance(right_paddle)<50 and ball.xcor()>320) or (ball.distance(left_paddle)<50 and ball.xcor()<-320):
        ball.xbounce()
    #to detect a miss of the R paddle:
    if ball.xcor()>380:
        ball.reset()
        ball.xbounce()
        scoreboard.l_score_up()
        scoreboard.update_scoreboard()
    #to detect a miss of the L paddle:
    if  ball.xcor()<-380:
        ball.reset()
        ball.xbounce()
        scoreboard.r_score_up()
        scoreboard.update_scoreboard()
screen.exitonclick()
