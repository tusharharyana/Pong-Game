from turtle import Turtle, Screen

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.create_paddle_shape()
        self.shape("rectangle_paddle")
        self.color("gray")
        self.penup()
        self.goto(position)
        
    def create_paddle_shape(self):
        shape = (
            (5,-5),
            (-50, 5),(-55, 5),(-60, 0),
            (-60, 0),(-55, -5),(-50, -5),
            (50, -5),(55, -5),(60, 0),
            (60, 0),(55, 5),(50, 5),(-50, 5)
            
        )
        screen = Screen()
        screen.register_shape("rectangle_paddle", shape)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

