import os
import sys
import math
import time
import pygame
from Minions import Goblin
from Minions import Enemy
from object import Enemy_castle
from object import Doom_diver
from object import Goblin_Doom_Catulpult

current_path = os.getcwd()
import pymunk as pm



pygame.init()
win = pygame.display.set_mode((1028, 600))
pygame.display.set_caption("Fist Game")

game_run_time = 0

#army
spawn_count = 0
goblins = []
divers = []
catulpult = Goblin_Doom_Catulpult()


#enemy
E_spawn_count = 0
enemys = []
castle = Enemy_castle()



fly_path=[]



bold_font = pygame.font.SysFont("arial", 30, bold=True)
bold_font2 = pygame.font.SysFont("arial", 40, bold=True)
bold_font3 = pygame.font.SysFont("arial", 50, bold=True)

x_mouse = 0
y_mouse = 0
mouse_distance = 0
rope_lenght = 90
angle = 0
money = 0

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
Flying = False

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

    v = vector((catulpult.x + 50, catulpult.y+40), (x_mouse, y_mouse))
    uv = unit_vector(v)
    uv1 = uv[0]
    uv2 = uv[1]
    mouse_distance = distance(catulpult.x + 50, catulpult.y + 40, x_mouse, y_mouse)
    pu = (uv1*rope_lenght+catulpult.x+50, uv2*rope_lenght+catulpult.y+40)
    bigger_rope = 102
    x_diver = x_mouse - 20
    y_diver = y_mouse - 20
    if mouse_distance > rope_lenght:
        pux, puy = pu
        pux -= 20
        puy -= 20
        pul = pux, puy
        #loaded shell
        pygame.draw.rect(win, (0, 0, 255), (pux, puy, 60, 60))
        #
        pu2 = (uv1*bigger_rope + catulpult.x + 60, uv2*bigger_rope + catulpult.y+40)
        pygame.draw.line(win, (0, 0, 0), (catulpult.x+70, catulpult.y + 20), pu2, 5)
        pygame.draw.rect(win, (0, 0, 255), (pux, puy, 30, 30))
        #pygame.draw.circle(win, BLUE, (pux, puy), 12, 2)
        pygame.draw.line(win, (0, 0, 0), (catulpult.x+ 60, catulpult.y+20), pu2, 5)
    else:
        mouse_distance += 10
        pu3 = (uv1*mouse_distance + catulpult.x + 50, uv2*mouse_distance + catulpult.y +40)
        pygame.draw.line(win, (0, 0, 0), (catulpult.x+70, catulpult.y+20), pu3, 5)
        #screen.blit(redbird, (x_redbird, y_redbird))
        pygame.draw.rect(win, (0, 0, 255), (x_diver, y_diver, 30, 30))
        #pygame.draw.circle(win, BLUE, (x_diver, y_diver), 12, 2)
        pygame.draw.line(win, (0, 0, 0), (catulpult.x+60, catulpult.y+20), pu3, 5)

    # Angle of impulse
    dy = y_mouse - catulpult.y - 40
    dx = x_mouse - catulpult.x - 50
    if dx == 0:
        dx = 0.00000000000001
    angle = math.atan((float(dy))/dx)


while running:
    pygame.time.delay(50)
    money += 1
    game_run_time += 1

    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if (pygame.mouse.get_pressed()[0]):
            mouse_pressed = True
        if (event.type == pygame.MOUSEBUTTONUP and event.button == 1 and mouse_pressed):
            mouse_pressed = False

            #cat_x = 50
            #cat_y = 480

            xo = catulpult.x + 105
            yo = 100
            if mouse_distance > rope_lenght:
                mouse_distance = rope_lenght

            if x_mouse < catulpult.x + 5:
                diver = Doom_diver(mouse_distance, angle, xo, yo, space)
                divers.append(diver)
            else:
                diver = Doom_diver(-mouse_distance, angle, xo, yo, space)
                divers.append(diver)

    keys = pygame.key.get_pressed()

    x_mouse, y_mouse = pygame.mouse.get_pos()

    if keys[pygame.K_LEFT]:
        catulpult.x -= catulpult.dir
    if keys[pygame.K_RIGHT]:
        catulpult.x += catulpult.dir

    win.fill((230,230,255))

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
    pygame.draw.rect(win, (255, 0, 0), (catulpult.x, catulpult.y, catulpult.width, catulpult.height))


    for point in fly_path:
        pygame.draw.circle(win, WHITE, point, 5, 0)

    #sling
    if mouse_pressed and y_mouse > 100:
        sling_action()
        fly_path = []

    diver_to_removed=[]
    #fly_diver
    for diver in divers:
        if diver.shape.body.position.y < 0:
              diver_to_removed.append(diver)
        p = to_pygame(diver.shape.body.position)
        x, y = p
        x -= 22
        y -= 20
        #win.blit(redbird, (x, y))
        pygame.draw.circle(win, BLUE,p, int(diver.shape.radius), 2)
        fly_path.append(p)

    dt = 1.0 / 50.0 / 2.
    for x in range(2):
        space.step(dt)

    #spawn army
    if mouse_pressed and x_mouse > 10 and x_mouse < 90 and y_mouse > 10 and y_mouse < 90:
        if money > 10:
            goblins.append(Goblin(spawn_count))
            spawn_count += 1
            money -= 50

    #spawn enemy
    if game_run_time % 50 == 0:
        enemys.append(Enemy(E_spawn_count))
        E_spawn_count += 1

    # enemy_castle
    pygame.draw.rect(win, (125, 125, 125), (castle.x, castle.y , 50, 120))
    pygame.draw.rect(win, (255, 125, 125), (950, 480, 80, 60))

    # Draw money
    money_font = bold_font.render("MONEY", 1, BLACK)
    number_font = bold_font.render(str(money), 1, BLACK)
    win.blit(money_font, (920, 110))



    if money == 0:
        win.blit(number_font, (930, 150))
    else:
        win.blit(number_font, (930, 150))

    for goblin in goblins:
        #pygame.draw.rect(win, (255, 255, 0), (goblin.x, goblin.y , 20, 40))
        win.blit(goblin.image, (goblin.x, goblin.y))
        goblin.update()

    for enemy in enemys:
        pygame.draw.rect(win, (255, 0, 0), (enemy.x, enemy.y , 20, 40))
        enemy.update()

    pygame.display.update()

pygame.quit()