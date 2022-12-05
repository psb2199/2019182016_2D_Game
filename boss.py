from pico2d import *
import game_framework
import game_world
import math
import random


class Boss:
    image = None
    image_hit = None
    image_die = None
    imageEF = None


    def __init__(self,x = 200,y=-100,damage = 1):
        if Boss.image == None:
            Boss.image = load_image('resources\\mid_Boss.png')
        if Boss.image_hit == None:
            Boss.image_hit = load_image('resources\\mid_Boss_hit.png')
        if Boss.image_die == None:
            Boss.image_die = load_image('resources\\mid_Boss_destroied.png')
        if Boss.imageEF == None:
            Boss.imageEF = load_image('resources\\Effect.png')
        self.x, self.y, self.damage = x,y,damage
        self.heath = 600
        self.spawntime = 6000
        self.lifetime = 0

        self.frame = 0
        self.die_img= 0

        self.start_y = 0
        self.hit = False
        self.hit_count = 0

        self.effect_x = 0
        self.effect_y = 0




    def draw(self):
        if self.heath > 0:
            if self.hit == True:
                self.image_hit.clip_composite_draw(0, 0, 240, 120, 0, '', self.x, self.y, 240, 120)
            else:
                self.image.clip_composite_draw((int(self.frame / 10) % 2) * 240, 0, 240, 120, 0, '', self.x, self.y,
                                               240, 120)
        else:
            self.image_die.clip_composite_draw((int(self.frame / 10) % 1) * 240, 0, (self.frame%2)*240, 120, 0, '', self.x, self.y, 240 - self.die_img/5,
                                           120 - self.die_img/ 10)
            self.imageEF.clip_composite_draw((int(self.frame / 10) % 13) * 30, 0, 30, 27, 0, '',
                                             self.effect_x, self.effect_y, 40, 40)
        #draw_rectangle(*self.get_bb())

    def update(self):
        if self.hit == True:
            self.hit_count += 1
            if self.hit_count > 10:
                self.hit_count = 0
                self.hit = False

        self.frame += 1
        self.lifetime += 1
        if self.lifetime > self.spawntime:
            self.start_y += 0.1
            if self.heath > 0:
                self.y = math.sin(self.frame / 200 ) * 20 + 700 - min(self.start_y,200)
                self.x = math.cos(self.frame / 400 ) * 100 + 200

            else :
                game_world.remove_collision_object(self)
                self.y -= 0.2
                self.die_img += 1
                if self.die_img % 100 == 0:
                    self.effect_x = self.x + random.randint(-40,40)
                    self.effect_y = self.y + random.randint(-20, 20)
                if self.die_img > 600:
                    game_world.remove_object(self)
                    self.die_img = 0


    def get_bb(self):
        size_weath = 100
        size_heigt = 10
        return self.x - size_weath, self.y - size_heigt, self.x + size_weath, self.y + size_heigt

    def handle_collision(self, other, group):
        if group == 'bullets:boss':
            self.heath -= self.damage
            self.hit = True

            #print(self.heath)





def test_self():
    import play_state

    pico2d.open_canvas(400, 600)
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
