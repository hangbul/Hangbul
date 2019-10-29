import random
import json
import os

from pico2d import *
from math import *

import numpy as np
import pygame
import game_framework
import title_state
import pause_state
import characters
import object
import os
import cv2
import sys
import time
current_path = os.getcwd()

#color
b_c = (255, 0, 0)
g_c = (0, 255, 0 )
r_c = (0, 0, 255)
w_c = (255, 255, 255)




name = "MainState"

cater = None
grass = None
font = None
goblin = None


rope_draw = False
mouse_pressed = False
mouse_distance = 0

x_mouse, y_mouse = None, None
rope_lenght = 80
angle = 0



def vector(p0, p1):
    """Return the vector of the points
    p0 = (xo,yo), p1 = (x1,y1)"""
    a = p1[0] - p0[0]
    b = p1[1] - p0[1]
    return (a, b)


def unit_vector(v):
    """Return the unit vector of the points
    v = (a,b)"""
    h = ((v[0]**2)+(v[1]**2))**0.5
    if h == 0:
        h = 0.000000000000001
    ua = v[0] / h
    ub = v[1] / h
    return (ua, ub)

def distance(xo, yo, x, y):
    """distance between points"""
    dx = x - xo
    dy = y - yo
    d = ((dx ** 2) + (dy ** 2)) ** 0.5
    return d

def sling_action():

    global mouse_distance
    global rope_lenght
    global angle
    global x_mouse, y_mouse
    global goblin, cater

    # Fixing bird to the sling rope
    v = vector((cater.sling_x, cater.sling_y), (x_mouse, y_mouse))
    uv = unit_vector(v)
    uv1 = uv[0]
    uv2 = uv[1]
    mouse_distance = distance(cater.sling_x, cater.sling_y, x_mouse, y_mouse)
    pu = (uv1*rope_lenght+cater.sling_x, uv2*rope_lenght+cater.sling_y)
    bigger_rope = 102
    x_goblin = x_mouse - 20
    y_goblin = y_mouse - 20
    if mouse_distance > rope_lenght:
        pux, puy = pu
        pux -= 20
        puy -= 20
        goblin.x, goblin.y= pux, puy
        goblin.draw()
        pu2 = (uv1*bigger_rope+cater.sling_x, uv2*bigger_rope+cater.sling_y)
        goblin.x, goblin.y= pux, puy
    else:
        mouse_distance += 10
        pu3 = (uv1*mouse_distance+cater.sling_x, uv2*mouse_distance+cater.sling_y)
        goblin.x, goblin.y = x_goblin, y_goblin
        goblin.draw()

    # Angle of impulse
    dy = y_mouse - cater.sling_y
    dx = x_mouse - cater.sling_x
    if dx == 0:
        dx = 0.00000000000001
    angle = math.atan((float(dy))/dx)


def enter():
    global  grass, goblin, cater
    goblin = characters.Goblin()
    grass = object.Grass()
    cater = object.catetpult()


def exit():
    global goblin, grass, cater
    del(goblin)
    del(grass)
    del(cater)

def pause():
    pass


def resume():
    pass


def handle_events():
    global gob_draw, mouse_pressed, x_mouse, y_mouse, rope_draw

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            cater.dir = -1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            cater.dir = 1
        elif event.type == SDL_KEYUP and (event.key == SDLK_RIGHT or event.key == SDLK_LEFT):
            cater.dir = 0
        elif event.type == SDL_MOUSEBUTTONDOWN:
            mouse_pressed = True
            rope_draw =True
        elif event.type == SDL_MOUSEBUTTONUP:
            mouse_pressed = False
            rope_draw = False
        elif event.type == SDL_MOUSEMOTION:
            x_mouse, y_mouse = event.x, 600 - event.y + 1


def update():
    #boy.update()
    pass

def draw():
    clear_canvas()

    if mouse_pressed:
        sling_action()

    grass.draw()
    cater.draw()
    update_canvas()





