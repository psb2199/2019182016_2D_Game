from pico2d import *

class character:
    def __init__(self,x,y):
        self.x = x
        self.y = y

        self.image = load_image('resources\\player(50x50).png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def logic(self,dir_x,dir_y):

        self.x = self.x + (dir_x * 4)
        self.y = self.y + (dir_y * 4)

        if (self.x < 15):
            self.x = 15
        elif (385 < self.x):
            self.x = 385
        elif (self.y < 15):
            self.y = 15
        elif (585 < self.y):
            self.y = 585
