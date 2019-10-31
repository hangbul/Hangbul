

class Goblin(object):
	def __init__(self, number):
		self.number = number
		self.x, self.y = 20, 500
		self.speed = 3
		self.frame= 0
		self.helth = 100
		self.ADP = 10
		self.A_length =  10

	def update(self):
		self.frame += 1
		self.x += self.speed

class Enemy(object):
	def __init__(self, number):
		self.number = number
		self.x, self.y = 1020, 500
		self.speed = 3
		self.frame= 0
		self.helth = 100
		self.ADP = 10
		self.A_length =  10

	def update(self):
		self.frame += 1
		self.x -= self.speed

