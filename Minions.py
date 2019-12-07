import pygame
from pico2d import *

DASH_TIMER = range(1)



class IdleState:
    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.timer = 1000

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 200, 100, 100, boy.x, boy.y)


class RunState:
    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.dir = boy.velocity

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 800 -25)

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)


next_state_table = {
    IdleState: {RIGHT_DOWN: RunState, LEFT_DOWN : RunState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, SHIFT_DOWN: DashState},
    DashState: {SHIFT_UP: RunState, DASH_TIMER: RunState}

}
def load_image(name):
    image = pygame.image.load(name).convert_alpha()
    return image


class Goblin(object):
    image = None

    def __init__(self, number):
        self.number = number
        self.x, self.y = -20, 490
        self.dir = 3
        self.frame = 0
        self.helth = 100
        self.ADP = 10
        self.Attack_length = 10
        self.Attack_images = []
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_001.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_002.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_003.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_004.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_005.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_006.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_007.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_008.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_009.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_010.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_011.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_012.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_013.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_014.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_015.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_016.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_017.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_018.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_019.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_020.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_021.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_022.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_023.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_024.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_025.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_026.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_027.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_028.png"))
        self.Attack_images.append(load_image("resources/images/GK_walk/GK_walk_029.png"))
        if Goblin.image == None:
            self.image = self.Attack_images[self.frame]

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.x += self.dir
        self.frame += 1
        if self.frame >= len(self.Attack_images):
            self.frame = 0
        self.image = self.Attack_images[self.frame]

    def draw(self):
        self.cur_state.draw(self)




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
