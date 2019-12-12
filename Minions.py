import game_framework
from pico2d import *
import game_world

# Minion Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 0.2  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Minion Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

# Minion Type
GOBLIN_KNGIHT, GOBLIN_SPEAR, GOBLIN_BABARIAN, DWARF_WORRIR, DWARF_BABARIAN = range(5)

# Minion Event
ATTACK_TIME, IDLE_TIME = range(2)

key_event_table = {
    #   (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN
}


# Minion States

class IdleState:

    @staticmethod
    def enter(minion, event):
        if minion.type == GOBLIN_KNGIHT:
            minion.image = load_image('resources/images/Goblins/GK_walk.png')
        elif minion.type == GOBLIN_SPEAR:
            minion.image = load_image('resources/images/Goblins/GS_walk.png')
        elif minion.type == GOBLIN_BABARIAN:
            minion.image = load_image('resources/images/Goblins/GB_walk.png')
        elif minion.type == DWARF_WORRIR:
            minion.image = load_image('resources/images/Dwarfs/DW_walk.png')
        elif minion.type == DWARF_BABARIAN:
            minion.image = load_image('resources/images/Dwarfs/DB_walk.png')

        minion.w = minion.image.w // 30
        minion.h = minion.image.h

    @staticmethod
    def exit(minion, event):
        pass

    @staticmethod
    def do(minion):
        minion.frame = (minion.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 30
        minion.x += minion.dir
        minion.x = clamp(25, minion.x, 1600 - 25)
        if minion.state == 1:
            minion.add_event(ATTACK_TIME)

    @staticmethod
    def draw(minion):

        minion.HPimage0.draw(0 - minion.window_left + minion.x, 50 + minion.y)
        minion.HPimage1.clip_draw(0, 0, (int)(90 *(minion.Health_point/minion.Max_HP)), 20, -(int)(90 *(1-(minion.Health_point/minion.Max_HP)))//2 - minion.window_left + minion.x, 50 + minion.y)

        minion.image.clip_draw(int(minion.frame) * minion.w, 0, minion.w, minion.h, 0 - minion.window_left + minion.x,
                               0 + minion.y)


class AttackState:

    @staticmethod
    def enter(minion, event):
        minion.y += 15
        if minion.type == GOBLIN_KNGIHT:
            minion.image = load_image('resources/images/Goblins/GK_attack.png')
        elif minion.type == GOBLIN_SPEAR:
            minion.image = load_image('resources/images/Goblins/GS_attack.png')
        elif minion.type == GOBLIN_BABARIAN:
            minion.image = load_image('resources/images/Goblins/GB_attack.png')
        elif minion.type == DWARF_WORRIR:
            minion.image = load_image('resources/images/Dwarfs/DW_attack.png')
        elif minion.type == DWARF_BABARIAN:
            minion.image = load_image('resources/images/Dwarfs/DB_attack.png')

        minion.w = minion.image.w // 30
        minion.h = minion.image.h

    @staticmethod
    def exit(minion, event):
        pass

    @staticmethod
    def do(minion):
        minion.frame = (minion.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 30
        minion.x = clamp(25, minion.x, 1600 - 25)

        if minion.state == 0:
            minion.add_event(IDLE_TIME)

    @staticmethod
    def draw(minion):

        minion.HPimage0.draw(0 - minion.window_left + minion.x, 50 + minion.y)
        minion.HPimage1.clip_draw(0, 0, (int)(90 * (minion.Health_point / minion.Max_HP)), 20, -(int)(
            90 * (1 - (minion.Health_point / minion.Max_HP))) // 2 - minion.window_left + minion.x, 50 + minion.y)
        minion.image.clip_draw(int(minion.frame) * minion.w, 0, minion.w, minion.h, 0 - minion.window_left + minion.x,
                               0 + minion.y)
        if minion.type == GOBLIN_SPEAR and int(minion.frame) == 15:
            minion.attack_sound.play()
        elif minion.type == DWARF_WORRIR and int(minion.frame) == 20:
            minion.attack_sound.play()
        elif minion.type == DWARF_BABARIAN and int(minion.frame) == 20:
            minion.attack_sound.play()


next_state_table = {
    IdleState: {ATTACK_TIME: AttackState},
    AttackState: {IDLE_TIME: IdleState}
}


class Goblin_Knight:
    image = None

    def __init__(self):
        self.HPimage0 = load_image('resources/images/UI/HP_0.png')
        self.HPimage1 = load_image('resources/images/UI/HP_1.png')

        self.type = GOBLIN_KNGIHT
        self.DF = 80
        self.AP = 80
        self.Max_HP = 1000
        self.Health_point = self.Max_HP
        self.x, self.y = - 20, 90
        self.window_left = 0
        self.window_bottom = 0
        if Goblin_Knight.image == None:
            Goblin_Knight.image = load_image('resources/images/Goblins/GK_walk.png')
        self.font = load_font('resources/font/ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.state = 0
        self.event_que = []
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.w
        self.h
        self.enemy = None
        self.attack_sound = load_wav('resources/sound/spear_gob.wav')
        self.attack_sound.set_volume(32)



    def get_bb(self):
        # return self.x - 15, self.y - 35, self.x + 40, self.y + 50
        return -15 - self.window_left + self.x, -35 - self.window_bottom + self.y, 40 - self.window_left + self.x, 50 - self.window_bottom + self.y

    def oppose(self, enemy):
        self.enemy = enemy
        return self.enemy

    def set_center_object(self, caturpult):
        self.center_object = caturpult

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.window_left = clamp(0, int(self.center_object.x) - self.canvas_width // 2, 1839 - self.canvas_width)
        self.window_bottom = clamp(0, int(self.center_object.y) - self.canvas_height // 2, 1103 - self.canvas_height)


        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def attack(self):
        self.state = 1
        self.dir = 0

    def dead(self):
        self.x = 0

    def kill(self):
        self.dir = 1
        self.state = 0
        self.y = 90

    def walk(self):
        self.state = 0
        self.dir = 1

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


class Goblin_Spear:
    image = None

    def __init__(self):
        self.HPimage0 = load_image('resources/images/UI/HP_0.png')
        self.HPimage1 = load_image('resources/images/UI/HP_1.png')
        self.type = GOBLIN_SPEAR
        self.DF = 15
        self.AP = 5
        self.Max_HP = 90
        self.Health_point = self.Max_HP
        self.x, self.y = - 20, 90
        self.window_left = 0
        self.window_bottom = 0
        # Boy is only once created, so instance image loading is fine
        if Goblin_Spear.image == None:
            Goblin_Spear.image = load_image('resources/images/Goblins/GS_walk.png')
        self.font = load_font('resources/font/ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.state = 0
        self.event_que = []
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.w
        self.h
        self.enemy = None
        self.attack_sound = load_wav('resources/sound/spear_gob.wav')
        self.attack_sound.set_volume(32)

    def get_bb(self):
        # return self.x - 15, self.y - 35, self.x + 40, self.y + 50
        return -15 - self.window_left + self.x, -35 - self.window_bottom + self.y, 40 - self.window_left + self.x, 50 - self.window_bottom + self.y

    def oppose(self, enemy):
        self.enemy = enemy
        return self.enemy

    def set_center_object(self, caturpult):
        self.center_object = caturpult

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.window_left = clamp(0, int(self.center_object.x) - self.canvas_width // 2, 1839 - self.canvas_width)
        self.window_bottom = clamp(0, int(self.center_object.y) - self.canvas_height // 2, 1103 - self.canvas_height)

        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def attack(self):
        self.state = 1
        self.dir = 0
        self.y = 95

    def dead(self):
        self.x = 0

    def kill(self):
        self.dir = 1
        self.state = 0

    def walk(self):
        self.state = 0
        self.dir = 1
        self.y = 90

    def draw(self):
        self.cur_state.draw(self)
        # debug
        #draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


class Goblin_Babarian:
    image = None

    def __init__(self):
        self.HPimage0 = load_image('resources/images/UI/HP_0.png')
        self.HPimage1 = load_image('resources/images/UI/HP_1.png')

        self.type = GOBLIN_BABARIAN
        self.DF = 30
        self.AP = 150
        self.Max_HP = 1300
        self.Health_point = self.Max_HP
        self.x, self.y = - 20, 90
        self.window_left = 0
        self.window_bottom = 0
        # Boy is only once created, so instance image loading is fine
        if Goblin_Babarian.image == None:
            Goblin_Babarian.image = load_image('resources/images/Goblins/GB_walk.png')
        self.font = load_font('resources/font/ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.state = 0
        self.event_que = []
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.w
        self.h
        self.enemy = None
        self.attack_sound = load_wav('resources/sound/spear_gob.wav')
        self.attack_sound.set_volume(32)


    def get_bb(self):
        # return self.x - 15, self.y - 35, self.x + 40, self.y + 50
        return -15 - self.window_left + self.x, -35 - self.window_bottom + self.y, 40 - self.window_left + self.x, 50 - self.window_bottom + self.y

    def oppose(self, enemy):
        self.enemy = enemy
        return self.enemy

    def set_center_object(self, caturpult):
        self.center_object = caturpult

    def add_event(self, event):
        self.event_que.insert(0, event)

    def dead(self):
        self.x = 0

    def kill(self):
        self.dir = 1
        self.state = 0


    def update(self):
        self.window_left = clamp(0, int(self.center_object.x) - self.canvas_width // 2, 1839 - self.canvas_width)
        self.window_bottom = clamp(0, int(self.center_object.y) - self.canvas_height // 2, 1103 - self.canvas_height)

        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def attack(self):
        self.state = 1
        self.dir = 0
        self.y = 95

    def walk(self):
        self.state = 0
        self.dir = 1
        self.y = 90

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


class Dwarf_worrior:
    image = None

    def __init__(self):
        self.HPimage0 = load_image('resources/images/UI/HP_0.png')
        self.HPimage1 = load_image('resources/images/UI/HP_1.png')

        self.type = DWARF_BABARIAN
        self.DF = 50
        self.AP = 100
        self.Max_HP = 1500
        self.Health_point = self.Max_HP
        self.x, self.y = 1500, 90
        self.window_left = 0
        self.window_bottom = 0
        # Boy is only once created, so instance image loading is fine
        # self.image = load_image('resources/images/Gk_walk/GK_walk.png')
        if Dwarf_worrior == None:
            Dwarf_worrior.image = load_image('resources/images/Dwarfs/DW_walk.png')
        self.font = load_font('resources/font/ENCR10B.TTF', 16)
        self.dir = -1
        self.velocity = 0
        self.frame = 0
        self.state = 0
        self.event_que = []
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.w
        self.h
        self.enemy = None
        self.attack_sound = load_wav('resources/sound/axe_worrior.wav')
        self.attack_sound.set_volume(32)


    def get_bb(self):
        # return self.x - 15, self.y - 35, self.x + 40, self.y + 50
        return -15 - self.window_left + self.x, -35 - self.window_bottom + self.y, 40 - self.window_left + self.x, 50 - self.window_bottom + self.y

    def oppose(self, enemy):
        self.enemy = enemy
        return self.enemy

    def set_center_object(self, caturpult):
        self.center_object = caturpult

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.window_left = clamp(0, int(self.center_object.x) - self.canvas_width // 2, 1839 - self.canvas_width)
        self.window_bottom = clamp(0, int(self.center_object.y) - self.canvas_height // 2, 1103 - self.canvas_height)

        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def dead(self):
        self.x = 1600

    def kill(self):
        self.dir = -1
        self.state = 0

    def attack(self):
        self.state = 1
        self.dir = 0
        self.y = 90

    def walk(self):
        self.state = 0
        self.dir = -1

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

class Dwarf_babarian:
    image = None

    def __init__(self):
        self.HPimage0 = load_image('resources/images/UI/HP_0.png')
        self.HPimage1 = load_image('resources/images/UI/HP_1.png')

        self.type = DWARF_WORRIR
        self.DF = 10
        self.AP = 150
        self.Max_HP = 1600
        self.Health_point = self.Max_HP
        self.x, self.y = 1500, 90
        self.window_left = 0
        self.window_bottom = 0
        # Boy is only once created, so instance image loading is fine
        # self.image = load_image('resources/images/Gk_walk/GK_walk.png')
        if Dwarf_babarian.image == None:
            Dwarf_babarian.image = load_image('resources/images/Dwarfs/DB_walk.png')
        self.font = load_font('resources/font/ENCR10B.TTF', 16)
        self.dir = -1
        self.velocity = 0
        self.frame = 0
        self.state = 0
        self.event_que = []
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.w
        self.h
        self.enemy = None
        self.attack_sound = load_wav('resources/sound/axe_babarian.wav')
        self.attack_sound.set_volume(32)


    def get_bb(self):
        # return self.x - 15, self.y - 35, self.x + 40, self.y + 50
        return -15 - self.window_left + self.x, -35 - self.window_bottom + self.y, 40 - self.window_left + self.x, 50 - self.window_bottom + self.y

    def oppose(self, enemy):
        self.enemy = enemy
        return self.enemy

    def set_center_object(self, caturpult):
        self.center_object = caturpult

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.window_left = clamp(0, int(self.center_object.x) - self.canvas_width // 2, 1839 - self.canvas_width)
        self.window_bottom = clamp(0, int(self.center_object.y) - self.canvas_height // 2, 1103 - self.canvas_height)

        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def dead(self):
        self.x = 1600

    def kill(self):
        self.dir = -1
        self.state = 0

    def attack(self):
        self.state = 1
        self.dir = 0
        self.y = 90

    def walk(self):
        self.state = 0
        self.dir = -1

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
