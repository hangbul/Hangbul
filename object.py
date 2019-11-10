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
        # self.images = []

        # self.images.append(load_image())
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


class Goblin_Doom_catulpult:
    def __init__(self):
        self.x = 50
        self.y = 480
        self.width = 100
        self.height = 60
        self.dir = 1
        self.frame = 0
        self.images = []
        self.images.append(load_image("resources/images/GDC_move/GDC_move_000.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_001.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_002.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_003.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_004.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_005.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_006.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_007.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_008.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_009.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_010.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_011.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_012.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_013.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_014.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_015.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_016.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_017.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_018.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_019.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_020.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_021.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_022.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_023.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_024.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_025.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_026.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_027.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_028.png"))
        self.images.append(load_image("resources/images/GDC_move/GDC_move_029.png"))

        self.image = self.images[self.frame]

    def update(self, dir):
        self.dir = dir
        self.x += self.dir * 5
        self.frame += self.dir
        if self.frame <= -1:
            self.frame += len(self.images)
        elif self.frame >= len(self.images):
            self.frame = 0

        self.image = self.images[self.frame]


class Enemy_castle:
    def __init__(self):
        self.life = 100
        self.x, self.y = 850, 420
