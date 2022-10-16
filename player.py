from pico2d import *

class player:
    def __init__(self,x,y):
        self.x = x
        self.x = y
        self.image = load_image('player(50x50).png')

    def draw(self):
        self.image.draw(self.x,self.y)