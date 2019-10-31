import math
import pygame
import pymunk as pm
from pymunk import Vec2d

class Doom_diver(object):
	def __init__(self, distance, angle, x, y, space):
		self.life = 20
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

class Enemy_castle:
	def __init__(self):
		self.life = 100
		self.x, self.y = 850, 420