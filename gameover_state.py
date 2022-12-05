import game_framework

from pico2d import *

import play_state
image = None


def enter():
    global image
    global font

    image = load_image('resources\\gameover.png')
    font = load_font('DS-DIGIT.TTF', 25)

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

    pass

def draw():
    clear_canvas()
    #image.draw(200,300)
    image.clip_composite_draw(0, 0, 509, 535, 0, '', 200, 300, 400, 600)

    font.draw(110, 230, '==== Score ====' % ( ), (200, 200, 200))
    font.draw(170, 200, '%d' % (play_state.total_score), (200, 200, 200))
    update_canvas()

def test_self():
    import play_state

    pico2d.open_canvas(400, 600)
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
