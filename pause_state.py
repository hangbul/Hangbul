import game_framework
import main_state

from pico2d import *


name = "PuaseState"
image = None
time_n = 0

def enter():
    global  image
    image =load_image('resources/images/UI/pause.png')

def exit():
    global image
    del(image)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()
def draw():
    global time_n

    if time_n > 0.5 and time_n < 1:
        clear_canvas()
        main_state.draw()

    else :
        image.draw(400, 300)


    delay(0.01)
    time_n += 0.01

    if time_n >= 1:
        time_n = 0

    update_canvas()






def update():
    pass


def pause():
    pass


def resume():
    pass






