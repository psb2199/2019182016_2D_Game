from pico2d import *
import game_framework
import random


class Enemy_Bullet:
    image = None


    def __init__(self,x = 600,y=700,velocity_y = 0.5,velocity_x = random.randint(-20,20)):
        if Enemy_Bullet.image == None:
            Enemy_Bullet.image = load_image('resources\\Enemy_Bullet.png')
        self.x, self.y, self.velocity_y,self.velocity_x = x,y,velocity_y,velocity_x
        self.lifetime = 0
        self.frame = 0



    def draw(self):

        if self.lifetime > 0:
            self.image.clip_composite_draw((int(self.frame/10) % 8)*8, 0, 8, 10, 0, '', self.x, self.y, 10, 12)
            draw_rectangle(*self.get_bb())

    def update(self):
        self.lifetime += 1

        if self.lifetime > 0:
            self.y -= self.velocity_y
            self.x += self.velocity_x
            self.frame += 1

        if self.lifetime > 1200:
            self.y = self.y
            self.velocity_x = random.randint(-20, 20)/150
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
