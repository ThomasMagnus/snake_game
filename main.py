import time
from turtle import Screen
from snake_class import Snake
from food import Food
from score_file import Score

run_game = True

screen = Screen()
screen.setup(700, 700)
screen.bgcolor('black')
screen.tracer(0)
food = Food()
score = Score()

snake = Snake('snake', 'white')
snake.turtle_setup()

screen.listen()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')


def game_field():
    if snake.snake_body[0].pos()[0] >= screen.screensize()[0] - 50 or snake.snake_body[0].pos()[1] >= \
            screen.screensize()[1] + 50 or snake.snake_body[0].pos()[0] <= -(screen.screensize()[0] - 50) \
            or snake.snake_body[0].pos()[1] <= -(screen.screensize()[1] + 50):
        score.hight_score_table()
        snake.refresh_snake()
        snake.snake_move()


score.write_score()

while run_game:

    screen.update()
    time.sleep(0.1)
    snake.snake_move()

    if snake.snake_body[0].distance(food) < 15:
        food.new_pos_food()
        score.refresh_score()
        snake.extend()

    for x in range(len(snake.snake_body) - 2, 0, -1):
        if snake.snake_body[0].distance(snake.snake_body[x]) < 10:
            run_game = False

    game_field()


screen.exitonclick()
