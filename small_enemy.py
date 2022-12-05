from pico2d import *
import game_framework
import game_world
import math
import random

health = 2

class Small_Enemy:
    image = None
    explo_sound = None

    def __init__(self,y=0,damage = 1):
        if Small_Enemy.image == None:
            Small_Enemy.image = load_image('resources\\enemy1.png')

        self.y, self.damage= y,damage
        self.heath = health
        self.lifetime = 0

        self.x = 0
        self.dir_x = 0

        self.frame = 0

        self.score = 0

        if Small_Enemy.explo_sound is None:
            Small_Enemy.explo_sound = load_wav('resources\\sound\\explo.wav')
            Small_Enemy.explo_sound.set_volume(32)



    def draw(self):
        if self.heath > 0:
            self.image.clip_composite_draw((int(self.frame/10) % 11)*32, 0, 32, 36, 0
                                           , '', self.x, self.y, 32, 36)
        #draw_rectangle(*self.get_bb())

    def update(self):
        self.frame += 1
        self.lifetime += 1

        if self.heath > 0:
            self.y -= 0.6
            self.x += self.dir_x
        else:
            Small_Enemy.explo_sound.play()
            self.score += 10

            self.y = -100
            self.heath = health


        if self.lifetime > 2000:
            # self.x = 0
            self.y = 700 - random.randint(-20,0)
            self.heath = health
            self.lifetime = 0

            self.frame = 0






    def get_bb(self):
        size_weath = 13
        size_heigt = 15
        return self.x - size_weath, self.y - size_heigt, self.x + size_weath, self.y + size_heigt

    def handle_collision(self, other, group):
        if group == 'bullets:small_enemys':
            self.heath -= self.damage



            #print(self.heath)





def test_self():
    import play_state

    pico2d.open_canvas(400, 600)
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
