from turtle import Turtle
from typing import final


class Score(Turtle):
    ALIGN: final(str) = 'center'
    FONT: final(tuple) = ('Arial', 24, 'normal')

    def __init__(self):
        super().__init__()
        self.score = 0

        with open('files/score.txt', 'r') as file:
            self.hight_score = file.read()

        self.color('white')
        self.up()
        self.goto(0, 300)
        self.hideturtle()

    def write_score(self):
        self.write(arg=f'Score: {self.score}. Hight score: {self.hight_score}', align=self.ALIGN, font=self.FONT)

    def hight_score_table(self):
        if self.score > int(self.hight_score):
            self.hight_score = self.score
            with open('files/score.txt', 'w') as file:
                file.write(str(self.hight_score))
        self.score = 0
        self.clear()
        self.write_score()

    def refresh_score(self):
        self.score += 1
        self.clear()
        self.write_score()
