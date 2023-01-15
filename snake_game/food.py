from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("Purple")
        self.speed("fastest")
        self.number = 0
    
    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)
    
    def big_food(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.shapesize(stretch_len=3,stretch_wid=3)
        self.goto(random_x,random_y)
