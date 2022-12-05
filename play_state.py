from pico2d import *

import gameover_state

import game_framework
import game_world

from score_ui import Score_Ui
from life_ui import Life_Ui

from background import Background
from background import Background_cloud
from background import Background_cloud2

from player import Player
from powerup import Powerup
from bullet import Bullet

from small_enemy import Small_Enemy
from small_enemy2 import Small_Enemy2

from mid_enemy import Mid_Enemy
from mid_enemy_bullet import Mid_Enemy_Bullet

from boss import Boss
from boss_bullet import Boss_Bullet


life_ui = []
score_ui = None

background = None
cloud = None
cloud2 = None

player = None
powerups = []
bullets = []

small_enemys = []
small_enemy2 = None

mid_enemy = None
mid_enemy_bullets = []

boss = None
boss_bullets = []
boos_bullets2 = []

gametime = 0
ii = 0
ee = 0
ee2 = 0
mm = 0
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

    global life_ui,max_player_life
    global score_ui

    global background, cloud, cloud2

    global player, powerups
    global bullets, bullet_count,bullet_gap

    global small_enemys, small_em_cnt1, small_em_gap1
    global small_enemy2

    global mid_enemy
    global mid_enemy_bullets, mid_em_bulcnt, mid_em_bulgap

    global boss
    global boss_bullets, boss_bulcnt, boss_bulgap
    global boss_bullets2 , boss_bulcnt2, boss_bulgap2

    background = Background()
    cloud = Background_cloud()
    cloud2 = Background_cloud2()
    game_world.add_object(background, 0)
    game_world.add_object(cloud, 0)
    game_world.add_object(cloud2, 0)


    boss = Boss()
    game_world.add_object(boss, 1)

    boss_bulcnt = 20
    boss_bulgap = 50
    boss_bullets = [Boss_Bullet() for i in range(boss_bulcnt)]
    for i in range(boss_bulcnt):
        boss_bullets[i].lifetime = -i * boss_bulgap
        game_world.add_object(boss_bullets[i], 0)

    boss_bulcnt2 = 5
    boss_bulgap2 = 20
    boss_bullets2 = [Mid_Enemy_Bullet() for i in range(boss_bulcnt2)]
    for i in range(boss_bulcnt2):
        boss_bullets2[i].lifetime = -i * boss_bulgap2
        game_world.add_object(boss_bullets2[i], 0)


    mid_enemy = Mid_Enemy()
    game_world.add_object(mid_enemy, 1)

    mid_em_bulcnt = 2
    mid_em_bulgap = 50
    mid_enemy_bullets = [Mid_Enemy_Bullet() for i in range(mid_em_bulcnt)]
    for i in range(mid_em_bulcnt):
        mid_enemy_bullets[i].lifetime = -i * mid_em_bulgap - 200
        game_world.add_object(mid_enemy_bullets[i], 0)


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


    max_player_life = player.life
    life_ui = [Life_Ui() for i in range(max_player_life)]
    for i in range(max_player_life):
        life_ui[i].x = i * 25 + 15
        game_world.add_object(life_ui[i], 1)


    score_ui = Score_Ui()
    game_world.add_object(score_ui, 1)


    game_world.add_collision_group(bullets, small_enemys, 'bullets:small_enemys')
    game_world.add_collision_group(bullets, small_enemy2, 'bullets:small_enemy2')
    game_world.add_collision_group(bullets, mid_enemy, 'bullets:mid_enemy')
    game_world.add_collision_group(bullets, boss, 'bullets:boss')


    game_world.add_collision_group(player, powerups, 'player:powerups')
    game_world.add_collision_group(player, mid_enemy_bullets, 'player:mid_enemy_bullets')
    game_world.add_collision_group(player, boss_bullets, 'player:boss_bullets')
    game_world.add_collision_group(player, boss_bullets2, 'player:mid_enemy_bullets')
    game_world.add_collision_group(player, small_enemys, 'player:small_enemys')
    game_world.add_collision_group(player, small_enemy2, 'player:small_enemy2')
    game_world.add_collision_group(player, small_enemy2, 'player:mid_enemy')




# 종료
def exit():
    global total_score
    for i in range(player.life):
        total_score += life_ui[i].score
    print(total_score)

    game_world.clear()


def update():
    global ii,ee,ee2, ss,pp,mm
    global total_score
    for game_object in game_world.all_objects():
        game_object.update()

    if player.collide:
        bullets[ii].x = -100
        bullets[ii].y = -100
        ii += 1
        if ii + 1 > bullet_count:
            ii = 0
        pass
    else:
        if bullets[ii].lifetime == 0:
            bullets[ii].x = player.x
            bullets[ii].y = player.y
            bullets[ii].bullet_level = player.bullet_level
            bullets[ii].fire_sound.play(1)
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
        powerups[pp].died = False
        powerups[pp].x = small_enemy2.die_x
        powerups[pp].y = small_enemy2.die_y
    pp += 1
    if pp + 1> 3:
        pp = 0


    if boss.heath > 0 and boss.lifetime > boss.spawntime + 1000:
        if boss_bullets[ee].lifetime == 0:
            if ee % 2 ==0:
                boss_bullets[ee].x = boss.x - 30
            elif ee % 2 == 1:
                boss_bullets[ee].x = boss.x + 30
            boss_bullets[ee].y = boss.y - 10
            ee += 1
        if ee + 1 > boss_bulcnt:
            ee = 0

        if boss_bullets2[ee2].lifetime == 0:
            boss_bullets2[ee2].x = boss.x
            boss_bullets2[ee2].y = boss.y - 10
            boss_bullets2[ee2].player_x = player.x
            boss_bullets2[ee2].player_y = player.y
            ee2 += 1
        if ee2 + 1 > boss_bulcnt2:
            ee2 = 0

    boss.damage = player.attack_power


    if mid_enemy.heath > 0 and mid_enemy.lifetime > 0:
        if mid_enemy_bullets[mm].lifetime == 0:
            mid_enemy_bullets[mm].x = mid_enemy.x
            mid_enemy_bullets[mm].y = mid_enemy.y - 10
            mid_enemy_bullets[mm].player_x = player.x
            mid_enemy_bullets[mm].player_y = player.y
            mm += 1
        if mm + 1 > mid_em_bulcnt:
            mm = 0

    mid_enemy.damage = player.attack_power





    for i in range(player.life, max_player_life):
        life_ui[i].x = -100




    total_score = 0

    for i in range(small_em_cnt1):
        total_score += small_enemys[i].score

    total_score += small_enemy2.score
    total_score += mid_enemy.score
    total_score += boss.score

    for i in range(3):
        total_score += powerups[i].score

    score_ui.total_score = total_score




    if player.life < 1:
        background.bgm.stop()
        exit()
        game_framework.change_state(gameover_state)

    for a,b, group in game_world.all_collision_pairs():
        if collide(a, b):
            # print('COLLID by ', group)
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
