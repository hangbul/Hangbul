import game_framework
import main_state

from pico2d import *


name = "TitleState"
image = None
main_image = None
start_image = None

def enter():
    global  image, main_image, start_image
    image =load_image('title.png')
    main_image =load_image('main_title.png')
    start_image =load_image('game_start.png')

def exit():
    global image, main_image, start_image
    del(image, main_image, start_image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                #game_framework.quit()
                game_framework.change_state(main_state)
def draw():
    clear_canvas()
    image.draw(400,300)
    main_image.clip_draw(0, 0, 456, 135, 400, 350)
    start_image.clip_draw(0, 0, 219, 46, 400, 150)

    update_canvas()






def update():
    pass


def pause():
    pass


def resume():
    pass






