import pymunk as pm
import pygame
import random
from pymunk import *


class goblin_army:
	def __init__(self, enemyType, health, speed, money, Map, ID, healthFac, moneyFac):
		self.speed = float(speed)
		self.health = int(float(health) * healthFac)
		#self.image = pygame.image.load(enemyType + '.png')
		#self.rect = self.image.get_rect()
		self.x = 40.0
		self.y = 40.0
		#self.money = int(float(money) * moneyFac)
		#self.enemyType = enemyType



	def update(self):
		self.x += (self.speed * 1.25)
