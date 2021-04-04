from turtle import Turtle
from typing import final


class Snake:
    UP: final(int) = 90
    DOWN: final(int) = 270
    LEFT: final(int) = 180
    RIGHT: final(int) = 0

    _segments = [(0, 0), (-20, 0), (-40, 0)]
    snake_body = []

    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def turtle_setup(self):
        for pos in self._segments:
            self.add_segments(pos)

    def add_segments(self, pos):
        segment = Turtle()
        segment.shape('square')
        segment.color('white')
        segment.up()
        segment.goto(pos)
        self.snake_body.append(segment)

    def extend(self):
        self.add_segments(self.snake_body[-1].position())

    def snake_move(self):

        for snake in range(len(self.snake_body) - 1, 0, -1):
            new_X = self.snake_body[snake - 1].xcor()
            new_Y = self.snake_body[snake - 1].ycor()
            self.snake_body[snake].goto(new_X, new_Y)
        self.snake_body[0].forward(20)

    def move(self, route, down_route):
        if self.snake_body[0].heading() != down_route:
            self.snake_body[0].setheading(route)

    def up(self):
        self.move(self.UP, self.DOWN)

    def down(self):
        self.move(self.DOWN, self.UP)

    def right(self):
        self.move(self.RIGHT, self.LEFT)

    def left(self):
        self.move(self.LEFT, self.RIGHT)
