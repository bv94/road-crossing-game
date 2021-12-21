import turtle


class Paddle(turtle.Turtle):
	def __init__(self, x_cord):
		super().__init__("square")

		self.color("white")
		self.penup()
		self.goto(x_cord, 0)
		self.turtlesize(stretch_wid=5, stretch_len=1, outline=1)

	def up(self):
		self.goto(self.xcor(), self.ycor() + 10)

	def down(self):
		self.goto(self.xcor(), self.ycor() - 10)
