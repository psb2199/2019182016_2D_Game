from pico2d import *
import random


class enemy:
    def __init__(self,x):

        self.x = x
        self.y = 650 + random.randrange(50, 200)
        self.speed = 1 + random.randrange(1, 5)/2
        self.image = load_image('enemy(50x50).png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def logic(self):
        self.y -= 1 + self.speed
        if(self.y < -50):
            self.y = 650
            self.x = random.randrange(50, 350)
            self.speed = 1 + random.randrange(1, 5)/2

