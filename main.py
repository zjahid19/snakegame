from snake import Snake
from food import Food
from score import Scoreboard
import time
from turtle import Turtle
import random


new_snake = Snake()
food = Food()
bonus_food = Food()

score = Scoreboard()

# Move Snake as per user action

new_snake.screen.listen()
new_snake.screen.onkey(new_snake.Up, "Up")
new_snake.screen.onkey(new_snake.Down, "Down")
new_snake.screen.onkey(new_snake.Left, "Left")
new_snake.screen.onkey(new_snake.Right, "Right")

is_game_on = True
food_count = 0
sleep_time = 0.08
food.create_food()
while is_game_on:
    new_snake.seg_move()
    # Add Bonus Food and detect food

    if new_snake.segment_list[0].distance(food) < 20 and food_count == 4:
        food.create_food()
        bonus_food.bonus_food()
        food_count = 0
        sleep_time = sleep_time - 0.002
    if new_snake.segment_list[0].distance(bonus_food) < 20:
        food_count = 0
        bonus_food.goto(-900, -900)
        score.bonus_update_score()
        sleep_time = sleep_time - 0.001
        print(food_count)
    elif new_snake.segment_list[0].distance(food) < 20:
        food.create_food()
        food_count = food_count + 1
        score.update_score()
        sleep_time = sleep_time - 0.001

# Append New Segment
        print(food_count)
        new_snake.new_segment = Turtle("square")
        new_snake.new_segment.color("red", random.choice(new_snake.color_list))
        new_snake.new_segment.shapesize(0.5)
        new_snake.new_segment.penup()
        new_snake.segment_list.append(new_snake.new_segment)

    # print(new_snake.segment_list)
    time.sleep(sleep_time)
    new_snake.screen.update()

# Detect Snake Collision with Wall
    if new_snake.segment_list[0].xcor() > 230\
            or new_snake.segment_list[0].xcor() < -230 or \
            new_snake.segment_list[0].ycor() > 230 or new_snake.segment_list[0].ycor() < -230:
        score.game_over()
        is_game_on = False

# Detect Tail Collision
    for is_collide in new_snake.segment_list[1:]:
        if new_snake.segment_list[0].distance(is_collide) < 5:
            score.game_over()
            is_game_on = False









new_snake.screen.exitonclick()
