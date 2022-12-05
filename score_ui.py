from pico2d import *
import game_framework

class Score_Ui:

    def __init__(self):
        self.font = load_font('DS-DIGIT.TTF', 25)

        self.x = 0
        self.y = 580

        self.total_score = 0

    def draw(self):

        self.font.draw(self.x, self.y, 'score = %d' % (self.total_score), (200, 200, 200))
    def update(self):
        pass



def test_self():
    import play_state

    pico2d.open_canvas(400, 600)
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
