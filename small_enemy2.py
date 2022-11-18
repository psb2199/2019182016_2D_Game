from pico2d import *
import game_framework

import random


health = 20

class Small_Enemy2:
    image = None


    def __init__(self,y=700,damage = 1):
        if Small_Enemy2.image == None:
            Small_Enemy2.image = load_image('resources\\enemy2.png')

        self.y, self.damage = y,damage
        self.heath = health
        self.died = False
        self.die_x = 0
        self.die_y = 0
        self.liftime = 0

        self.x = random.randint(50,350)

        self.frame = 0





    def draw(self):
        if self.heath > 0:
            self.image.clip_composite_draw(0*32, 0, 32, 36, 0, '', self.x, self.y, 48, 54)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.frame += 1
        self.liftime += 1

        if self.heath > 0:
            self.died = False
            self.y = -1/100000*(self.liftime - 3900)*(self.liftime - 4000)*(self.liftime - 4100) + 400
        else:
            self.died = True
            self.die_x = self.x
            self.die_y = self.y

            self.x = -100
            self.y = -100
            self.heath = health



        if self.liftime > 5000:
            self.x = random.randint(50,350)
            self.y = 700
            self.heath = health
            self.liftime = 0

            self.frame = 0






    def get_bb(self):
        size_weath = 20
        size_heigt = 4
        return self.x - size_weath, self.y - size_heigt, self.x + size_weath, self.y + size_heigt

    def handle_collision(self, other, group):
        if group == 'bullets:small_enemy2':
            self.heath -= self.damage
        if group == 'player:small_enemy2':
            print("gameover")





            #print(self.heath)





def test_self():
    import play_state

    pico2d.open_canvas(400, 600)
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
