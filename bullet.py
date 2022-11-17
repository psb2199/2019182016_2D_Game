from pico2d import *
import game_framework
import random


PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 0.45
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_ACTION = 8

class Bullet:
    image1 = None
    image2 = None
    image3 = None
    image4 = None

    imageEF = None

    def __init__(self, x = 200, y = 700, velocity = RUN_SPEED_PPS, bullet_level = 1):
        self.x, self.y, self.velocity, self.bullet_level = x, y, velocity, bullet_level
        self.lifetime = 0
        self.frame = 0

        self.effect_x = 500
        self.effect_y = 0
        self.effect_lifetime = 0
        self.eff_swt = False

        if Bullet.image1 == None:
            Bullet.image1 = load_image('resources\\Bullet_1.png')
        if Bullet.image2 == None:
            Bullet.image2 = load_image('resources\\Bullet_2.png')
        if Bullet.image3 == None:
            Bullet.image3 = load_image('resources\\Bullet_3.png')
        if Bullet.image4 == None:
            Bullet.image4 = load_image('resources\\Bullet_4.png')

        if Bullet.imageEF == None:
            Bullet.imageEF = load_image('resources\\Effect.png')

    def draw(self):

        if self.lifetime > 0:

            if self.bullet_level == 1:
                self.image1.draw(self.x, self.y)
            elif self.bullet_level == 2:
                self.image2.draw(self.x, self.y)
            elif self.bullet_level == 3:
                self.image3.draw(self.x, self.y)
            elif self.bullet_level == 4:
                self.image4.draw(self.x, self.y)
            elif self.bullet_level >= 5:
                self.image4.draw(self.x, self.y)
                self.image2.draw(self.x-15, self.y-10)
                self.image2.draw(self.x+15, self.y-10)

            if self.eff_swt == True:
                self.imageEF.clip_composite_draw((int(self.effect_lifetime) % 13) * 30, 0, 30, 27, 0, '',
                                                 self.effect_x, self.effect_y, 30, 27)

        #draw_rectangle(*self.get_bb())


    def update(self):
        #print(self.attack_power)

        self.lifetime += 1

        if self.eff_swt == True:
            self.effect_lifetime += 0.15
            if self.effect_lifetime > 13:
                self.eff_swt = False
                self.effect_lifetime = 0

        if self.lifetime > 0:
            self.y += self.velocity

        if self.lifetime > 200:
            self.y = self.y
            self.lifetime = 0


    def get_bb(self):
        size_weath = 4
        size_heigt = 8
        if self.bullet_level == 1:
            size_weath = 4
            size_heigt = 8
        elif self.bullet_level == 2:
            size_weath = 7
            size_heigt = 9
        elif self.bullet_level == 3:
            size_weath = 9
            size_heigt = 10
        elif self.bullet_level == 4:
            size_weath = 12
            size_heigt = 16
        elif self.bullet_level >= 5:
            size_weath = 18
            size_heigt = 16

        return self.x - size_weath, self.y - size_heigt, self.x + size_weath, self.y + size_heigt


    def handle_collision(self, other, group):
        # print('bullet disappears')
        if group == 'bullets:mid_boss':
            self.effect_x = self.x + random.randint(-10,10)
            self.effect_y = self.y + random.randint(-10,10)
            self.eff_swt = True

            self.x = 500
            self.y = 0

        elif group == 'bullets:small_enemys':
            self.effect_x = self.x
            self.effect_y = self.y
            self.eff_swt = True

            self.x = 500
            self.y = 0
        else:
            self.eff_swt = False


        pass







def test_self():
    import play_state

    pico2d.open_canvas(400, 600)
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()


