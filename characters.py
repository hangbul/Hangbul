import pymunk as pm
from pymunk import Vec2d
from pico2d import *

class Goblin():
    def __init__(self):
        self.x, self.y = 20, 90
        self.image = load_image('doom_diver.png')
        self.mass = 5

    def draw(self):
        self.image.clip_draw(0, 0, 40, 40, self.x, self.y)


