from pico2d import *
import game_framework

class Life_Ui:
    image = None

    def __init__(self):
        if Life_Ui.image == None:
            Life_Ui.image = load_image('resources\\life.png')

        self.x = 200
        self.y = 550

        self.score = 500


    def draw(self):
        self.image.clip_composite_draw(0, 0, 28, 33, 0, '', self.x, self.y, 28, 33)
    def update(self):
        pass



def test_self():
    import play_state

    pico2d.open_canvas(400, 600)
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
