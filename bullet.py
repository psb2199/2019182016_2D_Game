
from pico2d import *
import game_world


class Bullet:
    image = None


    def __init__(self, x = 200, y = 300, velocity = 1):
        if Bullet.image == None:
            Bullet.image = load_image('resources\\Bullet_Eg_b.png')
        self.x, self.y, self.velocity = x, y, velocity


    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y += self.velocity
        if self.y < 0 or self.y > 700 :
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10


    def handle_collision(self, other, group):
        print('ball disappears')
        if group == 'enemy:bullet':
            game_world.remove_object(self)






