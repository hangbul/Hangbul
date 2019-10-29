from pico2d import *


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class catetpult:
    def __init__(self):
        self.x, self.y = 30, 80
        self.image = load_image('goblin_doom_diver_caterpult.png')
        self.dir = 0
        self.frame = 0
        self.sling_x, self.sling_y = self.x+60, self.y + 36
        self.sling2_x, self.sling2_y = self.x + 70, self.y +36

    def draw(self):
        self.frame += self.dir
        if self.frame % 30 == 0:
            self.frame = 0
        elif self.frame < 0:
            self.frame = 30
        self.x += (self.dir / 10)
        self.sling_x = self.sling_x + (self.dir / 10)
        self.sling2_x = self.sling_x + (self.dir / 10)
        self.image.clip_draw(self.frame * 123, 0, 123, 77, self.x, self.y)
