from pico2d import *
import playerclass
import ammoclass

open_canvas(400,600)


#Player = load_image('player(50x50).png')
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

            if event.key == SDLK_ESCAPE:
                running = False

            elif event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1

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

ammo0 = ammoclass.ammo(x,y)
ammo1 = ammoclass.ammo(x,y)
ammo2 = ammoclass.ammo(x,y)
ammo3 = ammoclass.ammo(x,y)
ammo4 = ammoclass.ammo(x,y)

ammoarray = [ammo0,ammo1,ammo2,ammo3,ammo4]


player = playerclass.character(x,y)

ammo0 = ammoclass.ammo(x,y)
ammo1 = ammoclass.ammo(x,y+100)
ammo2 = ammoclass.ammo(x,y+200)
ammo3 = ammoclass.ammo(x,y+300)
ammo4 = ammoclass.ammo(x,y+400)

while (running == True):
    clear_canvas()
    player.draw()

    ammo0.draw()
    ammo1.draw()
    ammo2.draw()
    ammo3.draw()
    ammo4.draw()

    update_canvas()
    handle_events()

    player.logic(dir_x,dir_y)

    ammo0.logic(player.x, player.y)
    ammo1.logic(player.x, player.y)
    ammo2.logic(player.x, player.y)
    ammo3.logic(player.x, player.y)
    ammo4.logic(player.x, player.y)

    delay(0.01)


close_canvas()