from pico2d import *

open_canvas(400,600)

player = load_image('player(50x50).png')
enemy = load_image('enemy(50x50).png')
ammo = load_image('ammo.png')

def handle_events():
    global running
    global dir_x
    global dir_y

    events = get_events()
    for event in events:

        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1

            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1


running = True

x = 200
y = 50
dir_x = 0
dir_y = 0

a_x = 0
a_y = 0

while (running == True):
    clear_canvas()
    player.draw(x,y)
    ammo.draw(a_x,a_y)
    update_canvas()
    handle_events()

#player logic
    x = x + (dir_x * 4)
    y = y + (dir_y * 4)

    if(x<15):
        x = 15
    elif(385<x):
        x = 385
    elif (y < 15):
        y = 15
    elif (585 < y):
        y = 585



#ammo logic
    a_x = x
    a_y = y
    while (a_y < 100):
        a_y += 1

    delay(0.01)


close_canvas()