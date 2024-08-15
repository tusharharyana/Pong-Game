from turtle import Turtle
import random
class Ball(Turtle):
    
    def __init__(self):
        super().__init__()       
        self.random_color()
        self.shape("circle")
        self.penup()
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.1
        
    def random_color(self):
        self.r = random.randint(0,255)
        self.g = random.randint(0,255)
        self.b = random.randint(0,255)
        self.color(self.r/255,self.g/255,self.b/255)
        
    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        
        self.goto(new_x,new_y)
        
    def bounce_y(self):
        self.move_y *= -1 #Reverse direction of ball
        self.move_speed *= 0.9
        
    def bounce_x(self):
        self.move_x *= -1 #Reverse direction of ball
        self.move_speed *= 0.9
        
    def reset_position(self):
        self.goto(0,0)
        self.random_color()
        self.move_speed = 0.1 
        self.bounce_x()