import game_framework
from pico2d import *

import play_state

image = None
title = None

def enter():
    global image,title,framedown,onoff
    image = load_image('resources\\title.png')
    title = load_image('resources\\PRESSkey.png')

    global frame,framedown
    frame = 0
    framedown = 0
    onoff = False

def exit():
    global image, title, frame,framedown
    del image, title, frame,framedown

def handle_events():
    global onoff
    global frame, framedown
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                onoff = True


def update():
    global frame,framedown,onoff
    frame += 1
    if onoff == True:
        framedown += 0.2
        if framedown > 140:
            game_framework.change_state(play_state)
    pass

def draw():
    clear_canvas()
    global frame,framedown
    image.clip_composite_draw(0, 0, 558, 738, 0, '', 200, 300, 400, 600)
    title.clip_composite_draw(0, 0, 1000, (int(frame/(150 - framedown)) % 2) * 200, 0, '', 200, 150, 375, 75)
    update_canvas()