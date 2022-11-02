from pico2d import *
import enemyclass

class ammo:
    image = None
    def __init__(self,x,y):
        self.x = x
        self.y = y
        if ammo.image == None:
            ammo.image = load_image('resources\\ammo.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def logic(self,player_x, player_y):
        self.y += 15 #총알 속도
        if (self.y > player_y + 700):  # 700 = 화면 끝이나 적 피격시 사라질 값
            self.y = player_y + 20
            self.x = player_x
        # if (enemyclass.enemy.size - self.y < 20 and enemyclass.enemy.size - self.x < 20):
        #     print("dd")

# 0qj