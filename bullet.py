
from pico2d import *
import game_world

class Bullet:
    image = None


    def __init__(self, x = 800, y = 300, velocity = 1):
        if Bullet.image == None:
            Bullet.image = load_image('resources\\ammo.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y += self.velocity
        if self.y < 20 or self.y > 800 - 20:
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    # def handle_collision(self, other, group):
    #     print('ball disappears')
    #     if group == 'boy:ball':
    #         game_world.remove_object(self)



