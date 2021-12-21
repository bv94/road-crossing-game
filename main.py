from turtle import Screen
import ball
import paddle
import scoreboard

paddle_1 = paddle.Paddle(-350, )
paddle_2 = paddle.Paddle(350, )
ball = ball.Ball()
screen = Screen()
screen.listen()
screen.setup(1600, 1200)
screen.bgcolor("black")
game_running = True
ball.speed("fastest")
scoreboard = scoreboard.ScoreBoard()
while game_running:
	screen.onkey(paddle_1.up, "w")
	screen.onkey(paddle_1.down, "s")
	screen.onkey(paddle_2.up, "Up")
	screen.onkey(paddle_2.down, "Down")
	ball.move()
	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.y_bounce()
		print(ball.position)
	if (ball.distance(paddle_2) < 50 and ball.xcor() > 335) or (ball.distance(paddle_1) < 50 and ball.xcor() < -330):
		# (ball.xcor() > 340 and ball.distance(paddle_1) < 50) and (ball.xcor() > -340 and ball.distance(paddle_2) < 50)
		ball.paddle_collition()
	if ball.xcor() > 380:
		ball.reset()
		scoreboard.right_update_score()
	if ball.xcor() < -380:
		ball.reset()
		scoreboard.left_update_score()

	screen.update()

screen.exitonclick()
