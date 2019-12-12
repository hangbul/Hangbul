import game_framework
import main_state

from pico2d import *


name = "MenuState"
image = None
page = 1


def enter():
    global image
    image =load_image('resources/images/menu/help1.png')

def exit():
    global image
    del(image)

def handle_events():
    global image, page

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT and page == 1:
            image = load_image('resources/images/menu/help2.png')
            page = 2

        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT and page == 2:
            image = load_image('resources/images/menu/help1.png')
            page = 1

        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
                game_framework.pop_state()
def draw():

    image.draw(400, 250)


    update_canvas()



def update():
    pass


def pause():
    pass


def resume():
    pass






