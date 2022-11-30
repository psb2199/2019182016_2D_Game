from pico2d import *
import game_framework

import random
import math

health = 10

class Mid_Enemy:
    image = None

    def __init__(self,y=300,x = 200,damage = 1):
        if Mid_Enemy.image == None:
            Mid_Enemy.image = load_image('resources\\mid_enemy.png')

        self.y, self.x ,self.damage = y, x, damage
        self.heath = health
        self.died = False
        self.die_x = 0
        self.die_y = 0
        self.liftime = 0

        self.frame = 0


    def draw(self):
        if self.heath > 0:
            self.image.clip_composite_draw(0*32, 0, 310, 335, 0, '', self.x, self.y, 100, 110)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.frame += 1
        self.liftime += 1

        if self.heath > 0:
            self.died = False
            self.x = 100 * math.cos(self.frame / 200) + 200
            self.y = 100 * math.sin(self.frame / 200) + 300
        else:
            self.died = True
            self.die_x = self.x
            self.die_y = self.y

            self.x = -100
            self.y = -100



        if self.liftime > 5000:
            self.y = 700
            self.heath = health
            self.liftime = 0

            self.frame = 0



    def get_bb(self):
        size_weath = 20
        size_heigt = 4
        return self.x - size_weath, self.y - size_heigt, self.x + size_weath, self.y + size_heigt

    def handle_collision(self, other, group):
        if group == 'bullets:mid_enemy':
            self.heath -= self.damage
        if group == 'player:mid_enemy':
            print("gameover")



def test_self():
    import play_state

    pico2d.open_canvas(400, 600)
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
