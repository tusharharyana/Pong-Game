from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.move_x = 10
        self.move_y = 10
        
    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        
        self.goto(new_x,new_y)
        
    def bounce_y(self):
        self.move_y *= -1 #Reverse direction of ball
        
    def bounce_x(self):
        self.move_x *= -1 #Reverse direction of ball
        