from pico2d import *
import game_framework
import game_world
import math
import random


class Mid_Boss:
    image = None
    image_die = None
    imageEF = None


    def __init__(self,x = 200,y=700,damage = 1):
        if Mid_Boss.image == None:
            Mid_Boss.image = load_image('resources\\mid_Boss.png')
        if Mid_Boss.image_die == None:
            Mid_Boss.image_die = load_image('resources\\mid_Boss_destroied.png')
        if Mid_Boss.imageEF == None:
            Mid_Boss.imageEF = load_image('resources\\Effect.png')
        self.x, self.y, self.damage = x,y,damage
        self.heath = 200
        self.frame = 0
        self.die_img= 0

        self.effect_x = 0
        self.effect_y = 0




    def draw(self):
        if self.heath > 0:
            self.image.clip_composite_draw((int(self.frame/10) % 2)*240, 0, 240, 120, 0, '', self.x, self.y, 240, 120)
        else:
            self.image_die.clip_composite_draw((int(self.frame / 10) % 1) * 240, 0, (self.frame%2)*240, 120, 0, '', self.x, self.y, 240 - self.die_img/5,
                                           120 - self.die_img/ 10)
            self.imageEF.clip_composite_draw((int(self.frame / 10) % 13) * 30, 0, 30, 27, 0, '',
                                             self.effect_x, self.effect_y, 30, 27)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.frame += 1

        if self.heath > 0:
            self.y = math.sin(self.frame / 200 ) * 20 + 500
            self.x = math.cos(self.frame / 400 ) * 100 + 200

        else :
            self.y -= 0.2
            self.die_img += 1
            if self.die_img % 100 == 0:
                self.effect_x = self.x + random.randint(-40,40)
                self.effect_y = self.y + random.randint(-20, 20)
            if self.die_img > 600:
                game_world.remove_object(self)
                self.die_img = 0


    def get_bb(self):
        if self.heath > 0:
            size_weath = 100
            size_heigt = 10
        else:
            size_weath = 0
            size_heigt = 0
        return self.x - size_weath, self.y - size_heigt, self.x + size_weath, self.y + size_heigt

    def handle_collision(self, other, group):
        if group == 'bullets:mid_boss':
            self.heath -= self.damage
            #print(self.heath)





def test_self():
    import play_state

    pico2d.open_canvas(400, 600)
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
