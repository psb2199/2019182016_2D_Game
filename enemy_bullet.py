from pico2d import *
import game_framework
import game_world
import random


class Enemy_Bullet:
    image = None


    def __init__(self,x = 200,y=700,velocity = 0.5):
        if Enemy_Bullet.image == None:
            Enemy_Bullet.image = load_image('resources\\Enemy_Bullet.png')
        self.x, self.y, self.velocity = x,y,velocity
        self.lifetime = 0
        self.frame = 0



    def draw(self):

        if self.lifetime > 0:
            self.image.clip_composite_draw((int(self.frame/25) % 8)*8, 0, 8, 10, 0, '', self.x, self.y, 10, 12)
            draw_rectangle(*self.get_bb())

    def update(self):
        self.lifetime += 1

        if self.lifetime > 0:
            self.y -= self.velocity
            self.frame += 1

        if self.y < 0 or self.y > 900 :
            game_world.remove_object(self)
            print('dd')



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
