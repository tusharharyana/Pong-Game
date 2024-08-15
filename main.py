#The Pong Game
#@tusharharyana
from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


def initialize_game():
    global right_paddle, screen, left_paddle, ball, scoreboard,game_is_on
    screen.clear()
    screen.bgcolor("black")
    screen.tracer(0)

    right_paddle = Paddle((350, 0))
    left_paddle = Paddle((-350, 0))
    ball = Ball()
    scoreboard = ScoreBoard()
    game_is_on = True
    
    screen.listen()
    screen.onkey(right_paddle.go_up, "Up")
    screen.onkey(right_paddle.go_down, "Down")
    screen.onkey(left_paddle.go_up, "w")
    screen.onkey(left_paddle.go_down, "s")

def detect_collision():
    # Detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle.
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

def detect_miss():
    # Detect Right_paddle miss.
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect Left_paddle miss.
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

def game_over():
    global game_is_on
    scoreboard.game_over()
    screen.update()
    time.sleep(0.5) 
    
     #Prompt user to play again.
    
    response = screen.textinput("Game Over", "Do you want to play again? (Yes/No)").lower()
    if response == "yes":  
        initialize_game()
    else:
        screen.bye()


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


initialize_game()

game_is_on = True

while True:
        if game_is_on:  
                screen.update()
                time.sleep(ball.move_speed)
                ball.move()
                detect_collision()
                detect_miss()

                if scoreboard.check_winner():
                    game_is_on = False
                    scoreboard.game_over()
                    game_over()
        else:
            game_over()

            
screen.mainloop()

#@tusharharyana