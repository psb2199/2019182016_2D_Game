from pico2d import *
import playerclass
import ammoclass
import enemyclass

open_canvas(400,600)
back = load_image('background.png')

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
frame = 0

ammo0 = ammoclass.ammo(x,y)
ammo1 = ammoclass.ammo(x,y)
ammo2 = ammoclass.ammo(x,y)
ammo3 = ammoclass.ammo(x,y)
ammo4 = ammoclass.ammo(x,y)

ammoarray = [ammo0,ammo1,ammo2,ammo3,ammo4]


Player = playerclass.character(x,y)
Enemy1 = enemyclass.enemy(100)
Enemy2 = enemyclass.enemy(300)
Enemy3 = enemyclass.enemy(200)

ammo0 = ammoclass.ammo(x,y)
ammo1 = ammoclass.ammo(x,y+100)
ammo2 = ammoclass.ammo(x,y+200)
ammo3 = ammoclass.ammo(x,y+300)
ammo4 = ammoclass.ammo(x,y+400)

while (running == True):
    clear_canvas()

    back.clip_draw(0,0 + frame%1800,400,600,200,300)
    frame += 1


    Player.draw()

    Enemy1.draw()
    Enemy2.draw()
    Enemy3.draw()

    ammo0.draw()
    ammo1.draw()
    ammo2.draw()
    ammo3.draw()
    ammo4.draw()

    update_canvas()
    handle_events()

    Player.logic(dir_x,dir_y)
    Enemy1.logic()
    Enemy2.logic()
    Enemy3.logic()

    ammo0.logic(Player.x, Player.y)
    ammo1.logic(Player.x, Player.y)
    ammo2.logic(Player.x, Player.y)
    ammo3.logic(Player.x, Player.y)
    ammo4.logic(Player.x, Player.y)

    delay(0.01)


close_canvas()