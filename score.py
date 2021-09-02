from turtle import Turtle
import os

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.read_file = open('score.txt', mode='r')
        self.score = -50
        self.high_score = self.read_file.read()
        self.read_file.close()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=-30, y=230)
        self.write(f"Score : {self.score} ", "center", font=("calibri", 10, "normal"))

    def update_score(self):
        self.score = self.score + 10
        self.clear()
        self.goto(x=-30, y=230)
        self.write(f"Score : {self.score}  HighScore : {self.high_score} ", "center", font=("calibri", 10, "normal"))

    def bonus_update_score(self):
        self.score = self.score + 50
        self.clear()
        self.goto(x=-30, y=230)
        self.write(f"Score : {self.score}  HighScore : {self.high_score} ", "center", font=("calibri", 10, "normal"))


    def game_over(self):
        if self.score > int(self.high_score):
            self.write_file = open('score.txt', mode='w')
            self.high_score = self.write_file.write(str(self.score))
            self.write_file.close()
            self.goto(x=-30, y=230)
            self.clear()
            self.write(f"Score : {self.score} HighScore : {self.score} ", "center", font=("calibri", 10, "normal"))
            self.goto(-10, 0)
            self.write(f"GAME OVER", "center", font=("calibri", 10, "normal"))
        else:
            self.goto(-10, 0)
            self.write(f"GAME OVER", "center", font=("calibri", 10, "normal"))


