from pico2d import *
import game_framework
import game_world
import math
import random

health = 1

class Small_Enemy2:
    image = None


    def __init__(self,x = 0,y=0,damage = 1):
        if Small_Enemy2.image == None:
            Small_Enemy2.image = load_image('resources\\enemy2.png')

        self.x, self.y, self.damage = x,y,damage
        self.heath = health
        self.liftime = 0

        self.frame = 0





    def draw(self):
        if self.heath > 0:
            self.image.clip_composite_draw((int(self.frame/10) % 11)*32, 0, 32, 36, -0.6, '', self.x, self.y, 32, 36)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.frame += 1
        self.liftime += 1

        if self.heath > 0:
            self.y -= 0.6
            self.x -= 0.3
        else:
            self.x = -50
            self.y = -100

        if self.liftime > 2000:
            self.x = 450
            self.y = 700 - random.randint(-20,0)
            self.heath = health
            self.liftime = 0

            self.frame = 0






    def get_bb(self):
        size_weath = 13
        size_heigt = 15
        return self.x - size_weath, self.y - size_heigt, self.x + size_weath, self.y + size_heigt

    def handle_collision(self, other, group):
        if group == 'bullets:small_enemys2':
            self.heath -= self.damage





            #print(self.heath)





def test_self():
    import play_state

    pico2d.open_canvas(400, 600)
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
