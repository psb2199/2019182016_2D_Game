from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('resources\\Map_2.png')
        self.frame = 0

    def update(self):
        self.frame += 0.1

    def draw(self):
        self.image.clip_draw(0, int(self.frame), 400, 600, 200, 300)

    # def get_bb(self):
    #     return 0, 0, 1600 - 1, 50



