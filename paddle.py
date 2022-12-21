from turtle import Turtle


class Paddle(Turtle):
"""paddle turtle object for gameboard/player control
	def __init__(self, position):
		super().__init__()
		self.pu()
		self.shape("square")
		self.shapesize(stretch_wid=5, stretch_len=1)
		self.color("white")
		self.setx(position)
		self.showturtle()
# movement methods for up and down moving by increments of 20
	def up(self):
		new_y = self.ycor() + 20
		self.goto(self.xcor(), new_y)

	def down(self):
		new_y = self.ycor() - 20
		self.goto(self.xcor(), new_y)
