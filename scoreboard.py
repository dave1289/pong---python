from turtle import Turtle


class ScoreBoard(Turtle):
"""scoreboard class for scoreboard object in main.py game"""
	def __init__(self):
		super().__init__()
		self.color("white")
		self.pu()
		self.hideturtle()
		self.l_score = 0
		self.r_score = 0
		self.display_score()

# displays score at beginning of game when scoreboard object is created
	def display_score(self):
		self.goto(-100, 200)
		self.write(self.l_score, align="center", font=("Courier", 60, "bold"))
		self.goto(100, 200)
		self.write(self.r_score, align="center", font=("Courier", 60, "bold"))
# point keeping functionality for both players
	def l_point(self):
		self.l_score += 1
		self.clear()
		self.display_score()

	def r_point(self):
		self.r_score += 1
		self.clear()
		self.display_score()



