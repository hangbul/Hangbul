import math
import pygame
import pymunk as pm
from pymunk import Vec2d
import sys
def load_image(name):
	image = pygame.image.load(name)
	return image

class Doom_diver(object):

	def __init__(self, distance, angle, x, y, space):
		self.life = 20
		super(Doom_diver, self).__init__()
		#self.images = []

		#self.images.append(load_image())
		mass = 5
		radius = 12
		inertia = pm.moment_for_circle(mass, 0, radius, (0, 0))
		body = pm.Body(mass, inertia)
		body.position = x, y
		power = distance * 53
		impulse = power * Vec2d(1, 0)
		angle = -angle
		body.apply_impulse_at_local_point(impulse.rotated(angle))
		shape = pm.Circle(body, radius, (0, 0))
		shape.elasticity = 0.95
		shape.friction = 1
		shape.collision_type = 0
		space.add(body, shape)
		self.body = body
		self.shape = shape

class Goblin_Doom_Catulpult:
	def __init__(self):
		self.x = 50
		self.y = 480
		self.width = 100
		self.height = 60
		self.dir = 5
		self.frame = 0
		self.images = []
		self.images.append(load_image("resources/images/GK_walk/GK_walk_001.png"))

		self.image = self.images[self.frame]

	def update(self):
		self.x += self.speed
		self.frame += 1
		if self.frame >= len(self.images):
			self.frame = 0
		self.image = self.images[self.frame]

class Enemy_castle:
	def __init__(self):
		self.life = 100
		self.x, self.y = 850, 420