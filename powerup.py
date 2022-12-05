
from pico2d import *

import game_framework
import random


class Powerup:
    image = None
    textimage = None


    def __init__(self, x = -100, y = -100):
        self.x, self.y= x, y
        self.frame = 0
        self.txtframe = 0

        self.dir_x = random.randint(-5, 5)
        self.dir_y = random.randint(-5, 5)

        self.died = True
        self.died_x = -100
        self.died_y = -100

        if Powerup.image == None:
            Powerup.image = load_image('resources\\Item_Power.png')
        if Powerup.textimage == None:
            Powerup.textimage = load_image('resources\\powerup.png')


    def draw(self):
        self.image.clip_composite_draw((int(self.frame/20) % 6)*25, 0, 25, 18, 0, '', self.x, self.y, 25, 18)
        #draw_rectangle(*self.get_bb())
        if self.died:
            self.txtframe += 1
            self.textimage.clip_composite_draw((int(self.txtframe / 15) % 2) * 30, 0, 30, 16, 0, '', self.died_x, self.died_y, 30, 16)
            if self.txtframe > 300:
                self.died_x = -100
                self.died_y = -100
                self.txtframe = 0

    def update(self):
        if self.died == True:
            self.x = -100
            self.y = -100
        else:
            self.x += self.dir_x / 5
            self.y += self.dir_y / 5
            self.frame += 1
            if self.y < 0 :
                self.dir_y = random.randint(1, 5)
            if self.y > 600 :
                self.dir_y = random.randint(-5, -1)
            if self.x < 0 :
                self.dir_x = random.randint(1, 5)
            if self.x > 400  :
                self.dir_x = random.randint(-5, -1)



    def get_bb(self):
        size_weath = 15
        size_heigt = 12
        return self.x - size_weath, self.y - size_heigt, self.x + size_weath, self.y + size_heigt


    def handle_collision(self, other, group):

        if group == 'player:powerups':
            self.died_x = self.x
            self.died_y = self.y
            self.x = -100
            self.y = -100
            self.died = True




def test_self():
    import play_state

    pico2d.open_canvas(400, 600)
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()


