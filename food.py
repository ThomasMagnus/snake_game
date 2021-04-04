from turtle import Turtle
import random


class Food(Turtle):
    POS = random.randint(-350, 350)

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.up()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')

    def new_pos_food(self):
        POS = random.randint(-320, 320)
        self.goto(POS, POS)
