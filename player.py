from pico2d import *
import game_framework
import game_world
from bullet import Bullet

RD, LD, RU, LU, UD, DD, UU, DU = range(8)
event_name = ['RD', 'LD', 'RU', 'LU', 'UD', 'DD', 'UU', 'DU']

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYDOWN, SDLK_UP): UD,
    (SDL_KEYDOWN, SDLK_DOWN): DD,

    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYUP, SDLK_UP): UU,
    (SDL_KEYUP, SDLK_DOWN): DU,

}



#2 : 상태의 정의
class IDLE:
    @staticmethod
    def enter(self,event):
        print('ENTER IDLE')
        self.dir_x = 0
        self.dir_y = 0
        self.timer = 0

    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')
        self.face_dir = self.dir_y

        # if event == SPACE:
        #     self.fire_ball()


    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 1

        self.timer += 1
        if self.timer % self.bullet_gap == 1:
            self.fire_ball()



    @staticmethod
    def draw(self):
        self.image.clip_draw(self.frame * 50, 0, 50, 50, self.x, self.y)



class RUN:
    def enter(self, event):
        print('ENTER RUN')

        if event == RD:
            self.dir_x += 1
        elif event == LD:
            self.dir_x -= 1
        if event == UD:
            self.dir_y += 1
        elif event == DD:
            self.dir_y -= 1

        elif event == RU:
            self.dir_x -= 1
        elif event == LU:
            self.dir_x += 1
        elif event == UU:
            self.dir_y -= 1
        elif event == DU:
            self.dir_y += 1

    def exit(self, event):
        print('EXIT RUN')
        self.face_dir = self.dir_y



    def do(self):
        self.frame = (self.frame + 1) % 1
        self.x += self.dir_x
        self.y += self.dir_y
        self.x = clamp(0, self.x, 400)
        self.y = clamp(0, self.y, 600)
        self.timer += 1
        if self.timer % self.bullet_gap == 1:
            self.fire_ball()

    def draw(self):
        self.image.clip_draw(self.frame*50, 0, 50, 50, self.x, self.y)


class RUNcross:
    def enter(self, event):
        print('ENTER RUN')

        if event == RD:
            self.dir_x += 1
        elif event == LD:
            self.dir_x -= 1
        if event == UD:
            self.dir_y += 1
        elif event == DD:
            self.dir_y -= 1

        elif event == RU:
            self.dir_x -= 1
        elif event == LU:
            self.dir_x += 1
        elif event == UU:
            self.dir_y -= 1
        elif event == DU:
            self.dir_y += 1

    def exit(self, event):
        print('EXIT RUN')
        self.face_dir = self.dir_y


    def do(self):
        self.frame = (self.frame + 1) % 1
        self.x += self.dir_x
        self.y += self.dir_y
        self.x = clamp(0, self.x, 400)
        self.y = clamp(0, self.y, 600)
        self.timer += 1
        if self.timer % self.bullet_gap == 1:
            self.fire_ball()

    def draw(self):
        self.image.clip_draw(self.frame * 50, 0, 50, 50, self.x, self.y)





next_state = {
    IDLE:      {RU: RUN,  LU: RUN,  RD: RUN,  LD: RUN,  UD: RUN,  DD: RUN,  UU: RUN,  DU: RUN},
    RUN:       {RU: IDLE, LU: IDLE, RD: RUNcross, LD: RUNcross, UD: RUNcross, DD: RUNcross, UU: IDLE, DU: IDLE},
    RUNcross:  {RU: RUN, LU: RUN, RD: RUN, LD: RUN, UD: RUN, DD: RUN, UU: RUN, DU: RUN}
}





class Player:

    def __init__(self):
        self.x, self.y = 200, 50
        self.frame = 0
        self.dir_x = 0
        self.dir_y = 0
        self.image = load_image('resources\\player(50x50).png')

        self.timer = 0
        self.bullet_gap = 30

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}    Event {event_name[event]}')
            self.cur_state.enter(self, event)



    def draw(self):
        self.image.clip_draw(self.frame * 50, 0, 50, 50, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def fire_ball(self):
        print('FIRE BALL')
        bullet = Bullet(self.x, self.y, 3)
        game_world.add_object(bullet, 0)

    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15

    # def handle_collision(self, other, group):
    #     print('boy meet ball')

def test_self():
    import play_state

    pico2d.open_canvas(400, 600)
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()

