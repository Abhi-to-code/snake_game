from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open("py_programing/Turtle/snake_game/save_data.txt") as file:
            self.highscore = int(file.read())
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.write(f"Score: {self.score}      High Score {self.highscore}", align="center", font = ("Arail", 22,"normal"))
        self.hideturtle()
    
    def increse_score(self):
        self.score = self.score + 1
        self.clear()
        self.write(f"Score: {self.score}      High Score {self.highscore}", align="center", font = ("Arail", 22,"normal"))
    
    def game_over(self):
        game_over = Turtle()
        game_over.color("white")
        game_over.write(f"GAME OVER ", align="center", font = ("Arail", 22,"normal"))
        game_over.hideturtle()
    
    def check_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("py_programing/Turtle/snake_game/save_data.txt", mode = "w") as file:
                file.write(str(self.highscore))
        else:
            pass