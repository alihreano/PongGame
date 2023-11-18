from turtle import Turtle


class Ball(Turtle):  # our new class inherits the turtle class
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed=0.1
        self.color("white")
        self.shape("circle")
        self.penup()
        self.move()
        self.ybounce()
        self.xbounce()
        self.reset()
    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x, new_y)
    def ybounce(self):
        self.y_move *= -1  # reverse the direction of the movement on the y axis
    def xbounce(self):
        self.x_move *=-1 # reverse the direction of the movement on the x axis
        self.ball_speed*=0.9
    def reset(self):
        self.goto(0,0)
