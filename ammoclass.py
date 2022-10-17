from pico2d import *

class ammo:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = load_image('ammo.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def logic(self,player_x, player_y):
        self.y += 15
        if (self.y > player_y + 700):  # 300 = 화면 끝이나 적 피격시 사라질 값
            self.y = player_y + 20
            self.x = player_x