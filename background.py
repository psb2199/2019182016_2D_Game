from pico2d import *
import game_world
import game_framework
import random

class Background:
    bgm = None
    def __init__(self):
        self.image = load_image('resources\\Map.png')
        self.frame = 0

        if Background.bgm is None:
            Background.bgm = load_music('resources\\sound\\playmusic.mp3')
            Background.bgm.set_volume(32)
            Background.bgm.play()

    def update(self):
        self.frame += 0.1

    def draw(self):
        self.image.clip_draw(0, min(int(self.frame),1800), 400, 600, 200, 300)


class Background_cloud:

    def __init__(self,x = random.randint(0,400),y = 900):
        self.image = load_image('resources\\cloud.png')
        self.x = x
        self.y = y

    def update(self):
        self.y -= random.randint(1,10)/5
        if self.y < -300 or self.y > 900 :
            self.y = 900
            self.x = random.randint(-200,600)

    def draw(self):
        self.image.clip_composite_draw(0, 0, 400, 400, 0, '', self.x, self.y, 600, 600)


class Background_cloud2:

    def __init__(self,x = random.randint(0,400),y = 900):
        self.image = load_image('resources\\cloud2.png')
        self.x = x
        self.y = y

    def update(self):
        self.y -= random.randint(1,10)/10
        if self.y < -300 or self.y > 900 :
            self.y = 900.
            self.x = random.randint(-200,600)

    def draw(self):
        self.image.clip_composite_draw(0, 0, 400, 400, 0, '', self.x, self.y, 500, 500)




def test_self():
    import play_state

    pico2d.open_canvas(400, 600)
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
