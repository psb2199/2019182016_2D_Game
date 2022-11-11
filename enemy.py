from pico2d import *
import game_framework
import game_world

class Enemy:
    image = None


    def __init__(self, x = 200, y = 500):
        if Enemy.image == None:
            Enemy.image = load_image('resources\\enemy(50x50).png')
        self.x, self.y = x,y

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.y < 0 or self.y > 700 :
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, other, group):
        print('boy meet ball')



def test_self():
    import play_state

    pico2d.open_canvas(400, 600)
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
