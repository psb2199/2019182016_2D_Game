from pico2d import *
import game_framework
import game_world

from background import Background
from player import Player
from enemy import Enemy
from bullet import Bullet


player = None
background = None
enemy = None

bullets = []

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            player.handle_event(event)


# 초기화
def enter():
    global player, background, enemy

    player = Player()
    background = Background()
    enemy = Enemy()

    game_world.add_object(background, 0)
    game_world.add_object(player, 1)
    game_world.add_object(enemy, 1)

    # global bullets
    # bullets = [Bullet() for i in range(10)]
    #
    # game_world.add_objects(bullets, 1)
    game_world.add_collision_group(enemy, bullets, 'enemy:bullet')




# 종료
def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()


    for a,b, group in game_world.all_collision_pairs():
        if collide(a, b):
            print('COLLID by ', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)



def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass


def collide(a,b):
    la,ba,ra,ta = a.get_bb()
    lb,bb,rb,tb = b.get_bb()

    if la > rb : return False
    if ra < lb : return False
    if ta < bb : return False
    if ba > tb : return False

    return True



def test_self():
    import play_state

    pico2d.open_canvas(400, 600)
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
