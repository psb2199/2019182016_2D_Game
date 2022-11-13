from pico2d import *
import game_framework


class Bullet:
    image1 = None
    image2 = None
    image3 = None
    image4 = None

    def __init__(self, x = 200, y = 50, velocity = 3, bullet_level = 1):
        self.x, self.y, self.velocity, self.bullet_level = x, y, velocity, bullet_level
        self.lifetime = 0

        if Bullet.image1 == None:
            Bullet.image1 = load_image('resources\\Bullet_1.png')
        if Bullet.image2 == None:
            Bullet.image2 = load_image('resources\\Bullet_2.png')
        if Bullet.image3 == None:
            Bullet.image3 = load_image('resources\\Bullet_3.png')
        if Bullet.image4 == None:
            Bullet.image4 = load_image('resources\\Bullet_4.png')


    def draw(self):
        if self.lifetime > 0:
            if self.bullet_level == 1:
                self.image1.draw(self.x, self.y)
            elif self.bullet_level == 2:
                self.image2.draw(self.x, self.y)
            elif self.bullet_level == 3:
                self.image3.draw(self.x, self.y)
            elif self.bullet_level == 4:
                self.image4.draw(self.x, self.y)
            elif self.bullet_level >= 5:
                self.image4.draw(self.x, self.y)
                self.image2.draw(self.x-15, self.y-10)
                self.image2.draw(self.x+15, self.y-10)

        draw_rectangle(*self.get_bb())

    def update(self):
        #print(self.attack_power)

        self.lifetime += 1
        if self.lifetime > 0:
            self.y += self.velocity

        if self.lifetime > 200:
            self.y = self.y
            self.lifetime = 0


    def get_bb(self):
        size_weath = 4
        size_heigt = 8
        if self.bullet_level == 1:
            size_weath = 4
            size_heigt = 8
        elif self.bullet_level == 2:
            size_weath = 7
            size_heigt = 9
        elif self.bullet_level == 3:
            size_weath = 9
            size_heigt = 10
        elif self.bullet_level == 4:
            size_weath = 12
            size_heigt = 16
        elif self.bullet_level >= 5:
            size_weath = 18
            size_heigt = 16

        return self.x - size_weath, self.y - size_heigt, self.x + size_weath, self.y + size_heigt


    def handle_collision(self, other, group):
        # print('bullet disappears')
        if group == 'bullets:enemy':
            self.x = 500
            self.y = 0
            pass






def test_self():
    import play_state

    pico2d.open_canvas(400, 600)
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()


