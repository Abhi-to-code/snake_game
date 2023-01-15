from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increse_score()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
            score.check_score()
            score.game_over()
            game_is_on = False
    
    if snake.head.xcor() >= 300:
        snake.head.goto(-300, snake.head.ycor())
    elif snake.head.xcor() <= -300:
        snake.head.goto(300, snake.head.ycor())
    elif snake.head.ycor() >= 300:
        snake.head.goto(snake.head.xcor(), -300)
    elif snake.head.ycor() <= -300:
        snake.head.goto(snake.head.xcor(), 300)

    
screen.exitonclick()