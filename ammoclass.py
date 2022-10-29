from pico2d import *
import random

class ammo:
    def __init__(self):
        self.x = 200
        self.y = random.randint(0, 300)
        self.image = load_image('resources\\ammo.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def logic(self,player_x, player_y):
        self.y += 0.1
        # if (self.y > player_y + 700):  # 700 = 화면 끝이나 적 피격시 사라질 값
        #     self.y = player_y + 20
        #     self.x = player_x

# 0qj