import random
import json
import os
import math

from pico2d import *
import game_framework
import game_world
import pause_state
import title_state
import menu_state
import game_over_state
import game_clear_state

from Backgorund_objacts import Ground
from Backgorund_objacts import Background
from Backgorund_objacts import Frontground
from Backgorund_objacts import Castle

from UI_s import Goblin_knight_UI
from UI_s import Goblin_spear_UI
from UI_s import Goblin_babarian_UI
from UI_s import UI_Case
from UI_s import pause_UI
from UI_s import question_UI
from UI_s import Mouse_UI

from Minions import Goblin_Knight
from Minions import Goblin_Spear
from Minions import Goblin_Babarian
from Minions import Dwarf_worrior
from Minions import Dwarf_babarian

from Catulpult_main_char import Goblin_WAR_machine

current_path = os.getcwd()

name = "MainState"

#background
frontground = None
background = None
ground = None

#UI
GOBLIN_KNGIHT, GOBLIN_SPEAR, GOBLIN_BABARIAN, NOTMIN1, NOTMIN2 = range(5)

UIs = []
temp = 0
UIm = []
UIC = None
mouse = None
mouse_coll = False
UI_count = 0
game_run_time = 0
count = 0
font = None
tempUI = None
temp_time = 0

# army
spawn_count = 0
goblins = []
GoblinWarMachine_GWM = None

# enemy
E_spawn_count = 0
enemys = []
castle = None



# ====================================================

scr_w = 800
scr_h = 600

mouse_pressed = False



# ====================================================

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def enter():
    global font
    font = load_font('resources/font/MoriaCitadel.TTF', 16)

    global background
    background = Background()
    game_world.add_object(background, 0)

    global ground
    ground = Ground()
    game_world.add_object(ground, 0)

    global GoblinWarMachine_GWM
    GoblinWarMachine_GWM = Goblin_WAR_machine()
    game_world.add_object(GoblinWarMachine_GWM, 1)

    ground.set_center_object(GoblinWarMachine_GWM)
    background.set_center_object(GoblinWarMachine_GWM)
    ground.set_center_object(GoblinWarMachine_GWM)
    GoblinWarMachine_GWM.set_background(background)

    global castle
    castle = Castle()
    game_world.add_object(castle, 2)
    castle.set_center_object(GoblinWarMachine_GWM)

    global frontground
    frontground = Frontground()
    game_world.add_object(frontground, 2)
    frontground.set_center_object(GoblinWarMachine_GWM)

    global UIC
    UIC = UI_Case()
    game_world.add_object(UIC, 2)

    global UIm
    UIm = [question_UI(), pause_UI()]
    for UI in UIm:
        game_world.add_object(UI, 2)

    global mouse
    mouse = Mouse_UI()

def exit():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    global mouse_pressed, mouse_distance

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_q:
            game_framework.push_state(menu_state)

        elif event.type == SDL_MOUSEBUTTONDOWN:
            mouse_pressed = True

        elif event.type == SDL_MOUSEBUTTONUP:
            mouse_pressed = False


        elif event.type == SDL_MOUSEMOTION:
            mouse.x = event.x
            mouse.y = 600 - event.y +1
        else:
            GoblinWarMachine_GWM.handle_event(event)


def update():
    global game_run_time, E_spawn_count, spawn_count, UI_count, mouse_coll, mouse_pressed, goblins, tempUI, temp_time
    game_run_time += 1

    if game_run_time % 600 == 0:
        if random.randint(0, 100) <= 50:
            enemys.append(Dwarf_worrior())
        else:
            enemys.append(Dwarf_babarian())
        game_world.add_object(enemys[E_spawn_count], 1)
        enemys[E_spawn_count].set_center_object(GoblinWarMachine_GWM)
        E_spawn_count += 1

    if game_run_time % 300 == 0:
        if UI_count < 6:
            if random.randint(0, 100) <= 50:
                UIs.append(Goblin_spear_UI())
            elif 50 < random.randint(0, 100) <= 75:
                UIs.append(Goblin_knight_UI())
            else:
                UIs.append(Goblin_babarian_UI())
            game_world.add_object(UIs[UI_count], 2)
            UI_count += 1

    for game_object in game_world.all_objects():
        game_object.update()

    for goblin in goblins:
        for enemy in enemys:
            if collide(goblin, enemy):
                enemy.attack()
                goblin.attack()
                if 12< enemy.frame <=12.5:
                    goblin.Health_point -= clamp(1,enemy.AP - goblin.DF,enemy.AP)
                if 15< goblin.frame <= 15.5:
                    enemy.Health_point -= clamp(1,goblin.AP - enemy.DF,goblin.AP)
                if enemy.Health_point <= 0:
                    for goblin_q in goblins:
                        enemy.dead()
                        goblin_q.kill()
                        game_world.remove_object(enemy)
                if goblin.Health_point <= 0:
                    for enemy_q in enemys:
                        goblin.dead()
                        enemy_q.kill()
                        game_world.remove_object(goblin)

        if collide(goblin, castle):
            goblin.attack()
            if 15 < goblin.frame <= 15.5:
                castle.Health_Point -= goblin.AP
            if castle.Health_Point <= 0:
                game_framework.push_state(game_clear_state)


    if collide(GoblinWarMachine_GWM, castle):
        GoblinWarMachine_GWM.x -= 5

    for enemy in enemys:
        if collide(GoblinWarMachine_GWM, enemy):

            if game_run_time % 20 == 0:
                GoblinWarMachine_GWM.Health_point -= enemy.AP
                if GoblinWarMachine_GWM.x_velocity != 0:
                    enemy.Health_point -= GoblinWarMachine_GWM.AP
            enemy.x += 2

            if enemy.Health_point <= 0:
                game_world.remove_object(enemy)
            if GoblinWarMachine_GWM.Health_point <= 0:
                game_framework.push_state(game_over_state)


    for UIi in UIm:
        if collide(UIi, mouse):
            if mouse_pressed == True:
                if UIi.type == NOTMIN1:
                    game_framework.push_state(pause_state)
                elif UIi.type == NOTMIN2:
                    game_framework.push_state(menu_state)
                mouse_pressed = False

    for UIa in UIs:
        for UIb in UIs:
            if UIa != UIb and collide(UIa, UIb):
                UIb.dir = 0
                UIb.x -=2
        if collide(UIa, mouse):
            if mouse_pressed==True:
                if UIa.type == GOBLIN_KNGIHT:
                    goblins.append(Goblin_Knight())
                    game_world.add_object(goblins[spawn_count], 1)
                    goblins[spawn_count].set_center_object(GoblinWarMachine_GWM)
                elif UIa.type == GOBLIN_SPEAR:
                    goblins.append(Goblin_Spear())
                    game_world.add_object(goblins[spawn_count], 1)
                    goblins[spawn_count].set_center_object(GoblinWarMachine_GWM)
                elif UIa.type == GOBLIN_BABARIAN:
                    goblins.append(Goblin_Babarian())
                    game_world.add_object(goblins[spawn_count], 1)
                    goblins[spawn_count].set_center_object(GoblinWarMachine_GWM)
                spawn_count += 1
                tempUI = UIa
                temp_time = 2000
                UIs.remove(UIa)
                game_world.remove_object(UIa)
                for UIb in UIs:
                    UIb.dir = 1
                UI_count -= 1

    if tempUI != None and temp_time >= 2000:
        tempUI.sound()
        temp_time -= 1


    for UIa in UIs:
        if collide(UIa, UIC):
            UIa.dir = 0

    delay(0.01)

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    font.draw(get_canvas_width() - 90 , 540,'%0d : %0d' % ((game_run_time/100)/60, (game_run_time/100)%60), (255, 255, 255))
    mouse.draw()

    update_canvas()
