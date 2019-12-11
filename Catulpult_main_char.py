import game_framework
from pico2d import *
import game_world

PIXEL_PER_METER = (5.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 60

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP = range(4)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP
}



class IdleState:

    @staticmethod
    def enter(Goblin_Doom_catulpult, event):
        if event == RIGHT_DOWN:
            Goblin_Doom_catulpult.x_velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            Goblin_Doom_catulpult.x_velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            Goblin_Doom_catulpult.x_velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            Goblin_Doom_catulpult.x_velocity += RUN_SPEED_PPS

    @staticmethod
    def exit(Goblin_Doom_catulpult, event):
        pass

    @staticmethod
    def do(Goblin_Doom_catulpult):
        pass

    @staticmethod
    def draw(Goblin_Doom_catulpult):
        cx = Goblin_Doom_catulpult.x - Goblin_Doom_catulpult.bg.window_left
        Goblin_Doom_catulpult.image.clip_draw(int(Goblin_Doom_catulpult.frame) * Goblin_Doom_catulpult.w, 0, Goblin_Doom_catulpult.w, Goblin_Doom_catulpult.h, cx,Goblin_Doom_catulpult.y)


class MoveState:

    @staticmethod
    def enter(Goblin_Doom_catulpult, event):
        if event == RIGHT_DOWN:
            Goblin_Doom_catulpult.x_velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            Goblin_Doom_catulpult.x_velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            Goblin_Doom_catulpult.x_velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            Goblin_Doom_catulpult.x_velocity += RUN_SPEED_PPS
        Goblin_Doom_catulpult.dir = clamp(-1, Goblin_Doom_catulpult.x_velocity, 1)

    @staticmethod
    def exit(Goblin_Doom_catulpult, event):
        pass

    @staticmethod
    def do(Goblin_Doom_catulpult):
        Goblin_Doom_catulpult.frame = (Goblin_Doom_catulpult.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        Goblin_Doom_catulpult.x += Goblin_Doom_catulpult.x_velocity * game_framework.frame_time
        Goblin_Doom_catulpult.x = clamp(0, Goblin_Doom_catulpult.x, Goblin_Doom_catulpult.bg.w)

    @staticmethod
    def draw(Goblin_Doom_catulpult):
        cx = Goblin_Doom_catulpult.x - Goblin_Doom_catulpult.bg.window_left
        if Goblin_Doom_catulpult.dir == 1:
            Goblin_Doom_catulpult.image.clip_draw(int(Goblin_Doom_catulpult.frame) * Goblin_Doom_catulpult.w, Goblin_Doom_catulpult.h * 1, Goblin_Doom_catulpult.w, Goblin_Doom_catulpult.h ,  cx, Goblin_Doom_catulpult.y)
        else:
            Goblin_Doom_catulpult.image.clip_draw(int(Goblin_Doom_catulpult.frame) * Goblin_Doom_catulpult.w, Goblin_Doom_catulpult.h * 0, Goblin_Doom_catulpult.w, Goblin_Doom_catulpult.h , cx, Goblin_Doom_catulpult.y)

next_state_table = {
    IdleState: {RIGHT_UP: MoveState, LEFT_UP: MoveState, RIGHT_DOWN: MoveState, LEFT_DOWN: MoveState},
    MoveState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState}

}


class Goblin_Doom_catulpult:

    def __init__(self):
        self.HPimage0 = load_image('resources/images/UI/GDC_HP_0.png')
        self.HPimage1 = load_image('resources/images/UI/GDC_HP_1.png')
        self.Max_HP = 3000
        self.Health_point = self.Max_HP
        self.x, self.y = 100, 100
        self.AP = 400
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.image = load_image("resources/images/Goblins/Goblin_Doom_wheel.png")
        self.font = load_font('ENCR10B.TTF', 16)
        self.w = self.image.w // 60
        self.h = self.image.h // 2
        self.dir = 1
        self.x_velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def get_bb(self):
        return self.x - self.bg.window_left - self.w//2, self.y - self.h//2, self.x - self.bg.window_left + self.w//2, self.y + self.h//2

    def set_background(self, bg):
        self.bg = bg
        self.x = self.bg.w / 2


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

        self.HPimage0.draw(self.canvas_width//2,  140 + self.y - self.h // 2)
        self.HPimage1.clip_draw(0, 0, (int)(257 *(self.Health_point/self.Max_HP)), 20, -(int)(257 *(1-(self.Health_point/self.Max_HP)))//2 + self.canvas_width//2,  140 + self.y - self.h // 2)

        self.font.draw(self.canvas_width//2 - 100, 160 + self.y - self.h // 2,
                   'HP: %d' % self.Health_point,
                   (255, 255, 0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)



