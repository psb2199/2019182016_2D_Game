from pico2d import *
import game_framework
import game_world
import math


pi = 3.141592

class Enemy:
    image = None


    def __init__(self,x = 200,y=700,damage = 1):
        if Enemy.image == None:
            Enemy.image = load_image('resources\\Monster_4.png')
        self.x, self.y, self.damage = x,y,damage
        self.heath = 1000
        self.frame = 0



    def draw(self):
        self.image.clip_composite_draw((int(self.frame/10) % 2)*240, 0, 240, 120, 0, '', self.x, self.y, 240, 120)
        draw_rectangle(*self.get_bb())

    def update(self):


        self.y = math.sin(self.frame / 200 ) * 20 + 500
        self.x = math.cos(self.frame / 200 ) * 100 + 200

        self.frame += 1
        if self.y < 0 or self.y > 900 :
            game_world.remove_object(self)
            print('dd')
        if self.heath <= 0:
            game_world.remove_object(self)


    def get_bb(self):
        size_weath = 100
        size_heigt = 20
        return self.x - size_weath, self.y - size_heigt, self.x + size_weath, self.y + size_heigt

    def handle_collision(self, other, group):

        if group == 'bullets:enemy':
            self.heath -= self.damage
            #print(self.heath)
            pass




def test_self():
    import play_state

    pico2d.open_canvas(400, 600)
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
