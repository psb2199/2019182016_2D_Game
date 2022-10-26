from pico2d import *
import playerclass
import ammoclass
import enemyclass

open_canvas(400,600)
back = load_image('resources\\background.png')

def handle_events():
    global running
    global dir_x,dir_y
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
frame = 0

ammos = ammoclass.ammo(x,y)
Ammoarray = (ammos for i in range(5))

Player = playerclass.character(x,y)


Enemy1 = enemyclass.enemy(100)
Enemy2 = enemyclass.enemy(300)
Enemy3 = enemyclass.enemy(200)



while (running == True):
    clear_canvas()

    back.clip_draw(0,0 + frame%1800,400,600,200,300)
    frame += 1


    Player.draw()

    for ammos in Ammoarray:
        ammos.draw()


    Enemy1.draw()
    Enemy2.draw()
    Enemy3.draw()


    update_canvas()
    handle_events()

    Player.logic(dir_x,dir_y)
    ammos.logic(Player.x, Player.y)

    Enemy1.logic()
    Enemy2.logic()
    Enemy3.logic()


    delay(0.01)


close_canvas()

 
