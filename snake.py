from turtle import Turtle
from turtle import Screen
import random
import time
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """ This Class Create and Initiate Snake"""
    def __init__(self):
        self.screen = Screen()
        self.initial_coordinates = [(0, 0), (-20, 0), (-40, 0)]
        self.segment_list = []
        self.color_list = ["red", "yellow", "green", "white", "orange", "blue", "violet"]
        self.initial_setup()


    def initial_setup(self):
        """ This Methode perform all the initial setup required to build initial Snake"""
        self.screen.setup(width=500, height=500)
        self.screen.bgcolor("black")
        self.screen.title("New Snake Game")
        self.screen.tracer(0)
        for cordinate in self.initial_coordinates:
            self.new_segment = Turtle("square")
            self.new_segment.color("red", random.choice(self.color_list))
            self.new_segment.shapesize(0.5)
            self.new_segment.penup()
            self.new_segment.goto(cordinate)
            self.segment_list.append(self.new_segment)
        print(self.segment_list)
        self.screen.update()



    def seg_move(self):
        """ This Methode Move the Snake in forward direction"""
        for seg in range(len(self.segment_list)-1, 0, -1):
            x = self.segment_list[seg - 1].xcor()
            y = self.segment_list[seg - 1].ycor()
            self.segment_list[seg].goto(x, y)
        self.segment_list[0].forward(10)
        self.screen.update()
        # self.segment_list[0].right(90)


    def Up(self):
        """ This Method Change Snake Direction to Up"""
        if self.segment_list[0].heading() != DOWN:
            self.segment_list[0].setheading(UP)

    def Down(self):
        """ This Method Change Snake Direction to Down"""
        if self.segment_list[0].heading() != UP:
            self.segment_list[0].setheading(DOWN)

    def Right(self):
        """ This Method Change Snake Direction to Right"""
        if self.segment_list[0].heading() != LEFT:
            self.segment_list[0].setheading(RIGHT)

    def Left(self):
        """ This Method Change Snake Direction to Left"""
        if self.segment_list[0].heading() != RIGHT:
            self.segment_list[0].setheading(LEFT)
