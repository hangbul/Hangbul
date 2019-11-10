import pygame


def load_image(name):
    image = pygame.image.load(name).convert_alpha()
    return image


class Goblin(object):
    def __init__(self, number):
        self.number = number
        self.x, self.y = -20, 490
        self.dir = 3
        self.frame = 0
        self.helth = 100
        self.ADP = 10
        self.A_length = 10
        self.images = []
        self.images.append(load_image("resources/images/GK_walk/GK_walk_001.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_002.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_003.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_004.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_005.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_006.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_007.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_008.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_009.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_010.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_011.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_012.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_013.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_014.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_015.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_016.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_017.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_018.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_019.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_020.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_021.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_022.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_023.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_024.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_025.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_026.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_027.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_028.png"))
        self.images.append(load_image("resources/images/GK_walk/GK_walk_029.png"))
        self.image = self.images[self.frame]

    def update(self):
        self.x += self.dir
        self.frame += 1
        if self.frame >= len(self.images):
            self.frame = 0
        self.image = self.images[self.frame]


class Enemy(object):

    def __init__(self, number):
        self.number = number
        self.x, self.y = 1020, 500
        self.speed = 3
        self.frame = 0
        self.helth = 100
        self.ADP = 10
        self.A_length = 10

    def update(self):
        self.frame += 1
        self.x -= self.speed
