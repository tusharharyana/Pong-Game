from turtle import Turtle
import time

ALIGNEMT = "center"
FONT = ("courier",30,"normal")

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        
    
    def update_scoreboard(self):
        self.clear()
        self.color("white")
        self.goto(-100,240)
        self.write(self.l_score,align="center",font=("Courier",30,"bold"))
        self.goto(100,240)
        self.write(self.r_score,align="center",font=("Courier",30,"bold"))
        self.goto(0,240)
        self.write(":",align="center",font=("Courier",30,"bold"))
        for i in range(180,-240,-10):
            self.color("purple")
            self.goto(0,i)
            self.write("|",align="center",font=("Courier",30,"bold"))
    
    
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
    
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
        
    def check_winner(self):
        if self.l_score == 5 or self.r_score == 5:
            return True
        
        return False
        
    def game_over(self):
            self.color("white")
            self.goto(0,0)
            self.write(f"Game Over",align=ALIGNEMT,font = FONT)