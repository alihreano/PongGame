from turtle import  Turtle
class Paddle(Turtle):  # our new class inherits the turtle class
    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(pos)
        self.go_up()
        self.go_down()
    def go_up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)
    def go_down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)

