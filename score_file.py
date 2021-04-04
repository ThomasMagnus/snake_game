from turtle import Turtle
from typing import final


class Score(Turtle):
    ALIGN: final(str) = 'center'
    FONT: final(tuple) = ('Arial', 24, 'normal')

    def __init__(self):
        super().__init__()
        self.score = 0

        self.color('white')
        self.up()
        self.goto(0, 300)
        self.hideturtle()

    def write_score(self):
        self.write(arg=f'Score: {self.score}', align=self.ALIGN, font=self.FONT)

    def fail(self):
        self.goto(0, 0)
        self.write(arg='Game over', align='center', font=self.FONT)

    def refresh_score(self):
        self.score += 1
        self.clear()
        self.write_score()
