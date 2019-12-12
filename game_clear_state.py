import game_framework
import main_state
import title_state

from pico2d import *


name = "Game_clear_State"
image = None
point_image = None
image_h = -100
run_time = 0
point = 3

def enter():
    global  image, point_image, point
    image =load_image('resources/images/UI/Game_clear.png')

    if main_state.GoblinWarMachine_GWM.Health_point < main_state.GoblinWarMachine_GWM.Max_HP//2:
        point -= 1
    if main_state.game_run_time > 360000:
        point -= 1

    if point == 2:
        point_image = load_image('resources/images/UI/point2.png')
    elif point == 3:
        point_image = load_image('resources/images/UI/point3.png')
    else:
        point_image = load_image('resources/images/UI/point1.png')


def exit():
    global image, point_image
    del(image)
    del(point_image)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.pop_state()
                game_framework.change_state(title_state)
def draw():

    if run_time < 81:
        clear_canvas()
        main_state.draw()
        point_image.draw(400, image_h + 100)
        image.draw(400, image_h)
        update_canvas()


def update():
    global image_h, run_time
    run_time += 1
    if image_h < 300:
        image_h += 5
    delay(0.01)

def pause():
    pass


def resume():
    pass






