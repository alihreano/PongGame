from turtle import  Turtle
ALIGNMENT="center"
FONT=('Courier', 20, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score=0
        self.r_score=0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()
    def update_scoreboard(self):
        self.clear()
        self.write(f"  left player:{self.l_score}              right player:{self.r_score} ",align=ALIGNMENT, font=FONT)
    def r_score_up(self):
        self.r_score+=1
        self.update_scoreboard()
    def l_score_up(self):
        self.l_score+=1
        self.update_scoreboard()
