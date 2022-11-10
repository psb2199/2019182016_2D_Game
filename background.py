from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('resources\\background.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(200, 0)

    # def get_bb(self):
    #     return 0, 0, 1600 - 1, 50



