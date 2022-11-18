from pico2d import *
import game_framework
import game_world

from background import Background
from background import Background_cloud
from background import Background_cloud2

from player import Player
from powerup import Powerup
from bullet import Bullet

from small_enemy import Small_Enemy
from small_enemy2 import Small_Enemy2

from mid_boss import Mid_Boss
from enemy_bullet import Enemy_Bullet


background = None
cloud = None
cloud2 = None

player = None
powerups = []
bullets = []

small_enemys = []
small_enemy2 = None

mid_boss = None
enemy_bullet = []

gametime = 0
ii = 0
ee = 0
ss = 0
ss2 = 0
pp = 0

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            # game_world.add_object(powerup, 1)
            # game_world.add_collision_group(player, powerup, 'player:powerup')
            pass

        else:
            player.handle_event(event)


# 초기화
def enter():
    # global gametime
    global background, cloud, cloud2

    global player, powerups
    global bullets, bullet_count,bullet_gap

    global small_enemys, small_em_cnt1, small_em_gap1
    global small_enemy2

    global mid_boss
    global enemy_bullets, em_bulcnt, em_bulgap

    background = Background()
    cloud = Background_cloud()
    cloud2 = Background_cloud2()
    game_world.add_object(background, 0)
    game_world.add_object(cloud, 0)
    game_world.add_object(cloud2, 0)


    mid_boss = Mid_Boss()
    game_world.add_object(mid_boss, 1)

    em_bulcnt = 20
    em_bulgap = 50
    enemy_bullets = [Enemy_Bullet() for i in range(em_bulcnt)]
    for i in range(em_bulcnt):
        enemy_bullets[i].lifetime = -i * em_bulgap
        game_world.add_object(enemy_bullets[i], 0)


    small_em_cnt1 = 10
    small_em_gap1 = 50
    small_enemys = [Small_Enemy() for i in range(small_em_cnt1)]
    for i in range(small_em_cnt1):
        if i % 2 == 0:
            small_enemys[i].lifetime = -i * small_em_gap1
            small_enemys[i].x = 200
        elif i % 2 == 1:
            small_enemys[i].lifetime = -1 * (i-1) * small_em_gap1
            small_enemys[i].x = 200
        game_world.add_object(small_enemys[i], 1)


    small_enemy2 = Small_Enemy2()
    game_world.add_object(small_enemy2, 1)

    player = Player()
    game_world.add_object(player, 1)
    powerups = [Powerup() for i in range(3)]
    for i in range(3):
        game_world.add_object(powerups[i], 1)

    bullet_count = 10  # 10개 권장
    bullet_gap = 20  # 20 권장
    bullets = [Bullet() for i in range(bullet_count)]
    for i in range(bullet_count):
        bullets[i].lifetime = -i * bullet_gap
        game_world.add_object(bullets[i], 1)


    game_world.add_collision_group(bullets, small_enemys, 'bullets:small_enemys')
    game_world.add_collision_group(bullets, small_enemy2, 'bullets:small_enemy2')
    game_world.add_collision_group(bullets, mid_boss, 'bullets:mid_boss')
    game_world.add_collision_group(enemy_bullets, player, 'enemy_bullets:player')
    game_world.add_collision_group(player, powerups, 'player:powerups')



# 종료
def exit():
    game_world.clear()

def update():
    global ii,ee,ss,pp, gametime
    for game_object in game_world.all_objects():
        game_object.update()

    if bullets[ii].lifetime == 0:
        bullets[ii].x = player.x
        bullets[ii].y = player.y
        bullets[ii].bullet_level = player.bullet_level
        ii += 1
    if ii + 1 > bullet_count:
        ii = 0


    small_enemys[ss].damage = player.attack_power
    if ss % 2 == 0:
        small_enemys[ss].dir_x = 0.3
        if small_enemys[ss].lifetime > 1500:
            small_enemys[ss].x = -50
    elif ss % 2 == 1:
        small_enemys[ss].dir_x = -0.3
        if small_enemys[ss].lifetime > 1500:
            small_enemys[ss].x = 450

    ss += 1
    if ss + 1 > small_em_cnt1:
        ss = 0


    small_enemy2.damage = player.attack_power
    if small_enemy2.died == True:
        powerups[pp].x = small_enemy2.die_x
        powerups[pp].y = small_enemy2.die_y
    pp += 1
    if pp + 1> 3:
        pp = 0

    if mid_boss.heath > 0 and mid_boss.lifetime > mid_boss.spawntime + 1000:
        if enemy_bullets[ee].lifetime == 0:
            if ee % 2 ==0:
                enemy_bullets[ee].x = mid_boss.x - 30
            elif ee % 2 == 1:
                enemy_bullets[ee].x = mid_boss.x + 30
            enemy_bullets[ee].y = mid_boss.y - 10
            ee += 1
        if ee + 1 > em_bulcnt:
            ee = 0


    mid_boss.damage = player.attack_power


    for a,b, group in game_world.all_collision_pairs():
        if collide(a, b):
            # print('COLLID by ', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)

    gametime += 1




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
