from pico2d import *
import game_framework
import game_world
import math
import random


class Small_Enemy:
    image = None
    imageEF = None


    def __init__(self,x = 100,y=700,damage = 1):
        if Small_Enemy.image == None:
            Small_Enemy.image = load_image('resources\\enemy1.png')
        if Small_Enemy.imageEF == None:
            Small_Enemy.imageEF = load_image('resources\\Effect.png')
        self.x, self.y, self.damage = x,y,damage
        self.heath = 1
        self.frame = 0
        self.die_img= 0

        self.effect_x = 0
        self.effect_y = 0




    def draw(self):
        if self.heath > 0:
            self.image.clip_composite_draw((int(self.frame/10) % 11)*32, 0, 32, 36, 0, '', self.x, self.y, 32, 36)
        else:
            self.imageEF.clip_composite_draw((int(self.frame / 10) % 13) * 30, 0, 30, 27, 0, '',
                                             self.effect_x, self.effect_y, 30, 27)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.frame += 0.8

        if self.heath > 0:
            self.y -= 1
            self.x = math.cos(self.frame / 400 ) * 100 + 200

        else :
            self.y -= 0.2
            self.die_img += 1

            self.effect_x = self.x + random.randint(-1,1)
            self.effect_y = self.y + random.randint(-1, 1)

            if self.die_img > 60:
                game_world.remove_object(self)
                self.die_img = 0


    def get_bb(self):
        if self.heath > 0:
            size_weath = 13
            size_heigt = 15
        else:
            size_weath = 0
            size_heigt = 0
        return self.x - size_weath, self.y - size_heigt, self.x + size_weath, self.y + size_heigt

    def handle_collision(self, other, group):
        if group == 'bullets:small_enemy':
            self.heath -= self.damage
            #print(self.heath)





def test_self():
    import play_state

    pico2d.open_canvas(400, 600)
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
