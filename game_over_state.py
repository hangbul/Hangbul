import game_framework
import main_state
import title_state

from pico2d import *


name = "Game_over_State"
image = None
image_h = -100

def enter():
    global  image
    image =load_image('resources/images/UI/Game_over.png')

def exit():
    global image
    del(image)

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

    if image_h < 300:
        clear_canvas()
        main_state.draw()
        image.draw(400, image_h)
        update_canvas()

def update():
    global image_h

    if image_h < 300:
        image_h += 5

def pause():
    pass


def resume():
    pass






