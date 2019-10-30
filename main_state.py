import os
import sys
import math
import time
import pygame
import characters
current_path = os.getcwd()
import pymunk as pm

win = pygame.display.set_mode((1028, 600))

pygame.display.set_caption("Fist Game")

#army

#goblins = characters.goblin_army()



#caterpult
x = 50
y = 480
width = 100
height = 60
vel = 5


x_mouse = 0
y_mouse = 0
mouse_distance = 0
rope_lenght = 90
angle = 0

#color
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#vecter - gravtity
space = pm.Space()
space.gravity = (0.0, -700.0)



mouse_pressed = False
running = True

def to_pygame(p):
    """Convert pymunk to pygame coordinates"""
    return int(p.x), int(-p.y+600)


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
    """Set up sling behavior"""
    global mouse_distance
    global rope_lenght
    global angle
    global x_mouse
    global y_mouse
    # Fixing bird to the sling rope

    v = vector((x + 50, y+40), (x_mouse, y_mouse))
    uv = unit_vector(v)
    uv1 = uv[0]
    uv2 = uv[1]
    mouse_distance = distance(x+ 50, y+40, x_mouse, y_mouse)
    pu = (uv1*rope_lenght+x+50, uv2*rope_lenght+y+40)
    bigger_rope = 102
    x_redbird = x_mouse - 20
    y_redbird = y_mouse - 20
    if mouse_distance > rope_lenght:
        pux, puy = pu
        pux -= 20
        puy -= 20
        pul = pux, puy
        #screen.blit(redbird, pul)
        pygame.draw.rect(win, (0, 0, 255), (pux, puy, 60, 60))
        #pygame.draw.circle(win,(0,0,255), [pux, puy], 20)
        pu2 = (uv1*bigger_rope+x+60, uv2*bigger_rope+y+40)
        pygame.draw.line(win, (0, 0, 0), (x+60, y + 40), pu2, 5)
        #screen.blit(redbird, pul)
        pygame.draw.rect(win, (0, 0, 255), (pux, puy, 60, 60))

        pygame.draw.line(win, (0, 0, 0), (x+ 50, y+40), pu2, 5)
    else:
        mouse_distance += 10
        pu3 = (uv1*mouse_distance+x+50, uv2*mouse_distance+y+40)
        pygame.draw.line(win, (0, 0, 0), (x+60, y+40), pu3, 5)
        #screen.blit(redbird, (x_redbird, y_redbird))
        pygame.draw.rect(win, (0, 0, 255), (x_redbird, y_redbird, 60, 60))

        pygame.draw.line(win, (0, 0, 0), (x+50, y+40), pu3, 5)
    # Angle of impulse
    dy = y_mouse - y - 40
    dx = x_mouse - x - 50
    if dx == 0:
        dx = 0.00000000000001
    angle = math.atan((float(dy))/dx)


while running:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if (pygame.mouse.get_pressed()[0]):
            mouse_pressed = True
        if (event.type == pygame.MOUSEBUTTONUP and event.button == 1 and mouse_pressed):
            mouse_pressed = False
    keys = pygame.key.get_pressed()

    x_mouse, y_mouse = pygame.mouse.get_pos()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel

    win.fill((255,255,255))

    #menu
    pygame.draw.rect(win, (153, 93, 0), (0, 0, 1028, 100)) # UI

    for i in range(7):
        pygame.draw.rect(win, (240, 240, 240), (10 + 90 * i, 10, 80, 80)) #army UI

    for i in range(3):
        pygame.draw.rect(win, (240, 240, 240), (15 + 90 * 7 + 90 * i, 10, 80, 80)) #pause, start, help menu

    pygame.draw.rect(win, (240, 240, 240), (1028 - 110, 30, 100, 40))  # timer

    #ground
    pygame.draw.rect(win, (0, 255, 0), (0, 540, 1028, 60))

    #caterpult
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    #sling
    if mouse_pressed:
        sling_action()

    # enermy_castle
    pygame.draw.rect(win, (125, 125, 125), (850, 420, 50, 120))
    pygame.draw.rect(win, (255, 125, 125), (950, 480, 80, 60))

    pygame.display.update()

pygame.quit()