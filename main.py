#Steps to creating the snake game
        #create body
        #move the snack
        #control the snack
        #detect collision with food
        #create a scoreboard
        #detect collision with wall
        #detect collision with tail

from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on =True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect wall collision
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    #detect collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()