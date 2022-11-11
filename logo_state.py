import game_framework
from pico2d import *

import title_state

image = None
logo_time = 0

def enter():
    global image

    image = load_image('resources\\logo.png')


def exit():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()

def update():
    global logo_time
    if (logo_time > 6.0):
        logo_time = 0
        # game_framework.quit()
        game_framework.change_state(title_state)
        delay(0.01)
    logo_time += 0.01

def draw():
    clear_canvas()
    image.draw(200,300)
    update_canvas()