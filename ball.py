import turtle
import random


class Ball(turtle.Turtle):
	def __init__(self):
		super().__init__("circle")
		self.color("green")
		self.x_move = 2
		self.y_move = 2
		self.penup()


	def move(self):
		self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

	def y_bounce(self):
		self.y_move *= -1
		print('ahhahha')

	def paddle_collition(self):
		self.x_move *= -1
		print("nahahaha")

	def reset(self):
		self.goto(0, 0)
		self.x_move *= -1
		self.y_move *= -1
