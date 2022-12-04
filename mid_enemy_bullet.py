from pico2d import *
import game_framework
import random
import math


class Mid_Enemy_Bullet:
    image = None


    def __init__(self,x = -100,y=-100,player_x = 0,player_y = 0):
        if Mid_Enemy_Bullet.image == None:
            Mid_Enemy_Bullet.image = load_image('resources\\Enemy_Bullet.png')
        self.x, self.y = x,y
        self.player_x, self.player_y = player_x,player_y
        self.lifetime = 0
        self.frame = 0

        self.degree = 0



    def draw(self):

        if self.lifetime > 0:
            self.image.clip_composite_draw((int(self.frame/10) % 8)*8, 0, 8, 10, 0, '', self.x, self.y, 10, 12)
            draw_rectangle(*self.get_bb())

    def update(self):
        self.lifetime += 1

        self.degree = math.atan((self.player_x - self.x)/(self.player_y - self.y)) * 180 / math.pi

        if self.lifetime > 0:
            self.x -= 2 * math.sin(self.degree / 180 * math.pi)
            self.y -= 2 * math.cos(self.degree / 180 * math.pi)

            self.frame += 1


        if self.lifetime > 500:
            self.lifetime = 0



    def get_bb(self):
        size_weath = 5
        size_heigt = 5
        return self.x - size_weath, self.y - size_heigt, self.x + size_weath, self.y + size_heigt

    def handle_collision(self, other, group):

        if group == 'bullets:enemy':

            pass




def test_self():
    import play_state

    pico2d.open_canvas(400, 600)
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
