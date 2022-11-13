
from pico2d import *

import game_framework
import game_world

import random


class Powerup:
    image = None


    def __init__(self, x = 200, y = 300):
        self.x, self.y= x, y
        self.frame = 0

        self.dir_x = random.randint(-5, 5)
        self.dir_y = random.randint(-5, 5)

        if Powerup.image == None:
            Powerup.image = load_image('resources\\Item_Power.png')


    def draw(self):
        self.image.clip_composite_draw((int(self.frame/20) % 6)*25, 0, 25, 18, 0, '', self.x, self.y, 25, 18)
        draw_rectangle(*self.get_bb())


    def update(self):
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
        size_weath = 13
        size_heigt = 9
        return self.x - size_weath, self.y - size_heigt, self.x + size_weath, self.y + size_heigt


    def handle_collision(self, other, group):
        print('powerup disappears')
        if group == 'player:powerup':
            self.x, self.y = 200, 300
            self.dir_x = random.randint(-5, 5)
            self.dir_y = random.randint(-5, 5)

            game_world.remove_object(self)




def test_self():
    import play_state

    pico2d.open_canvas(400, 600)
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()


