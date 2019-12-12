from pico2d import *

GOBLIN_KNGIHT, GOBLIN_SPEAR, GOBLIN_BABARIAN, NOTMIN1, NOTMIN2 = range(5)


start = -20
class Mouse_UI:
    def __init__(self):
        #self.image = load_image("resources/images/UI/GK_botton.png")
        self.x = -20
        self.y = -20

    def draw(self):
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10 , self.x + 10 - 1, self.y + 10 -1

    def update(self):
        pass

class Goblin_knight_UI:
    def __init__(self):
        self.type = GOBLIN_KNGIHT
        self.image = load_image("resources/images/UI/GK_botton.png")
        self.x = start
        self.y = 540
        self.dir = 1
        self.spone_sound = load_wav('resources/sound/kngiht_gob_spone.wav')
        self.spone_sound.set_volume(64)

    def update(self):
        self.x += self.dir

    def draw(self):
        self.image.draw(self.x, self.y)

    def sound(self):
        self.spone_sound.play()

    def get_bb(self):
        return self.x - 40, self.y - 40 , self.x + 40 - 1, self.y + 40 -1

class Goblin_spear_UI:
    def __init__(self):
        self.type = GOBLIN_SPEAR
        self.image = load_image("resources/images/UI/GS_botton.png")
        self.x = start
        self.y = 540
        self.dir = 1
        self.spone_sound = load_wav('resources/sound/spear_gob_spone.wav')
        self.spone_sound.set_volume(64)

    def update(self):
        self.x += self.dir

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 40, self.y - 40 , self.x + 40 - 1, self.y + 40 -1

    def sound(self):
        self.spone_sound.play()

class Goblin_babarian_UI:
    def __init__(self):
        self.type = GOBLIN_BABARIAN
        self.image = load_image("resources/images/UI/GB_botton.png")
        self.x = start
        self.y = 540
        self.dir = 1
        self.spone_sound = load_wav('resources/sound/babarian_gob_spone.wav')
        self.spone_sound.set_volume(64)

    def update(self):
        self.x += self.dir


    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 40, self.y - 40 , self.x + 40 - 1, self.y + 40 -1

    def sound(self):
        self.spone_sound.play()

class UI_Case:
    def __init__(self):
        self.image = load_image("resources/images/UI/UI_case.png")
        self.x = 400
        self.y = 540
        self.w = self.image.w
        self.h = self.image.h

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x + 97, self.y - self.h//2 , self.x + self.w//2 - 1, self.y + self.h//2 -1

class pause_UI:
    def __init__(self):
        self.type = NOTMIN1
        self.image = load_image("resources/images/UI/pause_UI.png")
        self.x = get_canvas_width() - 225
        self.y = 540
        self.dir = 0

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 40, self.y - 40 , self.x + 40 - 1, self.y + 40 -1

class question_UI:
    def __init__(self):
        self.type = NOTMIN2
        self.image = load_image("resources/images/UI/question_UI.png")
        self.x = get_canvas_width() - 145
        self.y = 540
        self.dir = 0

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 40, self.y - 40 , self.x + 40 - 1, self.y + 40 -1


