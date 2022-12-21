from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

score = ScoreBoard()
game_is_on = True
# set turtle screen and attributes for game
screen = Screen()
screen.listen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
ball = Ball()

r_paddle = Paddle(350)

l_paddle = Paddle(-350)

# key controls for player 1 and player 2
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

# player 2 key controls
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

# game loop
while game_is_on:
	time.sleep(ball.pace)
	screen.update()
	ball.move()
	# contains all potential ball interactions with proximity to paddles and edges
	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce()
	if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
		ball.hit()
	if ball.xcor() > 400:
		ball.miss()
		score.l_point()
	if ball.xcor() < -400:
		ball.miss()
		score.r_point()
	# game ends when 1 player hits 5 points
	if score.l_score > 5 or score.r_score > 5:
		game_is_on = False



# click to exit functionality
screen.exitonclick()
