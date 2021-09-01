import random
from turtle import Turtle
from turtle import Screen
from snake import Snake
import random

class Food(Turtle):
    """ This Class is responsible for creating Food and Bonus Food for snake"""
    def __init__(self):
        super().__init__()
        # self.create_food()


    def create_food(self):
        """ This Method Create Food for Snake"""
        self.penup()
        self.shape("circle")
        self.color("green")
        self.x_cordinates = random.randint(-210, 210)
        self.y_cordinates = random.randint(-210, 210)
        self.goto(self.x_cordinates, self.y_cordinates)
        print(f"This Is Food {self.x_cordinates} and {self.y_cordinates}")
        # self.stamp()


    def bonus_food(self):
        """ This Method Create Bonus Food for Snake"""
        self.penup()
        self.shape("turtle")
        self.color("red")
        self.x_cordinates = random.randint(-210, 210)
        self.y_cordinates = random.randint(-210, 210)
        self.goto(self.x_cordinates, self.y_cordinates)
        print(f"This Is Bonus Food {self.x_cordinates} and {self.y_cordinates}")