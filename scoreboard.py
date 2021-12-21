import turtle


class ScoreBoard:
	def __init__(self):
		self.locations = [(90, 150), (-90, 150)]
		self.turtles = []
		self.scores = [0, 0]

		for i in range(2):
			self.turtles.append(turtle.Turtle())
			self.turtles[i].penup()
			self.turtles[i].hideturtle()
			self.turtles[i].goto(self.locations[i])
			self.turtles[i].color("purple")
			self.turtles[i].write(self.scores[i], align="center", font=("Courier", 80, "normal"))

	def right_update_score(self):
		self.turtles[1].clear()
		self.scores[1] += 1
		self.turtles[1].write(self.scores[1], align="center", font=("Courier", 80, "normal"))

	def left_update_score(self):
		self.turtles[0].clear()
		self.scores[0] += 1
		self.turtles[0].write(self.scores[0], align="center", font=("Courier", 80, "normal"))
