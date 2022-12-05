import game_framework
import play_state
from pico2d import *

import title_state

image = None
logo_time = 0

def enter():
    global image

    image = load_image('resources\\gameover.png')


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

            # elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            #     game_framework.change_state(play_state)
            #     pass


def update():
    # global logo_time
    # if (logo_time > 6.0):
    #     logo_time = 0
    #     # game_framework.quit()
    #     game_framework.change_state(title_state)
    #     delay(0.01)
    # logo_time += 0.01
    pass

def draw():
    clear_canvas()
    #image.draw(200,300)
    image.clip_composite_draw(0, 0, 509, 535, 0, '', 200, 300, 400, 600)
    update_canvas()