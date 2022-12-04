from pico2d import *
import game_framework
import game_world
import random
import math

heath = 70

class Mid_Enemy:
    image = None
    image_hit = None
    image_die = None
    imageEF = None

    def __init__(self,y=700,x = 200,damage = 1):
        if Mid_Enemy.image == None:
            Mid_Enemy.image = load_image('resources\\mid_enemy.png')
        if Mid_Enemy.image_hit == None:
            Mid_Enemy.image_hit = load_image('resources\\mid_enemy_hit.png')
        if Mid_Enemy.image_die == None:
            Mid_Enemy.image_die = load_image('resources\\mid_enemy_destroied.png')
        if Mid_Enemy.imageEF == None:
            Mid_Enemy.imageEF = load_image('resources\\Effect.png')
        self.x, self.y, self.damage = x, y, damage
        self.heath = heath

        self.spawntime = 3000

        self.lifetime = -self.spawntime
        self.frame = -self.spawntime


        self.die_img = 0

        self.start_y = 0
        self.hit = False
        self.hit_count = 0

        self.effect_x = 0
        self.effect_y = 0

    def draw(self):
        if self.heath > 0:
            if self.hit == True:
                self.image_hit.clip_composite_draw(0, 0, 310, 335, 0, '', self.x, self.y, 100, 110)
            else:
                self.image.clip_composite_draw((int(self.frame / 10) % 2)*310, 0, 310, 335, 0, '', self.x, self.y, 100, 110)
        else:
            self.image_die.clip_composite_draw((int(self.frame / 10) % 1) * 310, 0, (self.frame%2)*310, 335, 0, '', self.x, self.y, 100 - self.die_img/5,
                                           110 - self.die_img/ 5)
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

        if self.lifetime > 0:

            if self.heath > 0:
                self.x = 10 * math.cos(self.frame / 200) + 200
                if self.lifetime < 2000:
                    self.y = 100000 / self.frame + 300
                else:
                    self.y = 1/500*(self.frame - 2000)**2 + 350

            else :
                #game_world.remove_collision_object(self)
                self.y -= 0.2
                self.die_img += 1
                if self.die_img % 100 == 0:
                    self.effect_x = self.x + random.randint(-40,40)
                    self.effect_y = self.y + random.randint(-20, 20)
                if self.die_img > 600:
                    #game_world.remove_object(self)
                    self.die_img = 0
                    self.x = -100
                    self.y = -100

        if self.lifetime > 3000:
            self.x = 700
            self.y = 200
            self.heath = heath
            self.frame = 0
            self.lifetime = 0



    def get_bb(self):
        size_weath = 40
        size_heigt = 2
        if self.heath > 0:
            return self.x - size_weath, self.y - size_heigt, self.x + size_weath, self.y + size_heigt
        else:
            return 0,0,0,0

    def handle_collision(self, other, group):
        if group == 'bullets:mid_enemy':
            self.heath -= self.damage
            self.hit = True
        if group == 'player:mid_enemy':
            print("gameover")



def test_self():
    import play_state

    pico2d.open_canvas(400, 600)
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
