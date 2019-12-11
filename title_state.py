import game_framework
import main_state

from pico2d import *


name = "TitleState"
image = None
title_image = None
title_h = -100
start_image = None
start_h = -100


def enter():
    global image, title_image, start_image
    image = load_image('resources/images/background/game_title2.png')
    title_image = load_image('resources/images/title/main_title.png')
    start_image = load_image('resources/images/title/game_start.png')

def exit():
    global image, title_image
    del(image)
    del (title_image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)


def draw():
    clear_canvas()
    image.draw(400, 300)
    title_image.draw(400, title_h)
    start_image.draw(400, start_h)
    update_canvas()


def update():
    global title_h, start_h
    if title_h <= 400:
        title_h += 10
    if title_h >= 400 and start_h <= 150:
        start_h += 10
    delay(0.01)

def pause():
    pass


def resume():
    pass






