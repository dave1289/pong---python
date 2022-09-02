from turtle import Turtle



class Ball(Turtle):

	def __init__(self):
		super().__init__()
		self.dot(20)
		self.pu()
		self.shape("circle")
		self.color("white")
		self.x_move = 10
		self.y_move = 10
		self.pace = 0.1


	def move(self):
		new_x = self.xcor() + self.x_move
		new_y = self.ycor() + self.y_move
		self.goto(new_x, new_y)

	def bounce(self):
		self.y_move *= -1

	def hit(self):
		self.x_move *= -1
		self.pace *= 0.9

	def miss(self):
		self.x_move *= -1
		self.home()
