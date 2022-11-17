from pico2d import *
import game_framework


RD, LD, RU, LU, UD, DD, UU, DU, SPACE = range(9)
event_name = ['RD', 'LD', 'RU', 'LU', 'UD', 'DD', 'UU', 'DU', 'SPACE']

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYDOWN, SDLK_UP): UD,
    (SDL_KEYDOWN, SDLK_DOWN): DD,

    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYUP, SDLK_UP): UU,
    (SDL_KEYUP, SDLK_DOWN): DU,

    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}



#2 : 상태의 정의
class IDLE:
    @staticmethod
    def enter(self,event):
       # print('ENTER IDLE')
        self.dir_x = 0
        self.dir_y = 0
        self.timer = 0


    @staticmethod
    def exit(self, event):
        #print('EXIT IDLE')
        self.face_dir = self.dir_y

    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 1


    @staticmethod
    def draw(self):
        self.image.clip_composite_draw(96, 0, 32, 32, 0, '', self.x, self.y, 50, 50)

class RUN:
    def enter(self, event):
        #print('ENTER RUN')

        if event == RD:
            self.dir_x += 1
        elif event == LD:
            self.dir_x -= 1
        elif event == UD:
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
        #print('EXIT RUN')
        pass


    def do(self):
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 1
        self.x += self.dir_x * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.dir_y * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 400)
        self.y = clamp(0, self.y, 600)


    def draw(self):
        if self.dir_x == -1:
            self.image.clip_composite_draw(0, 0, 32, 32, 0, '', self.x, self.y, 50, 50)
        elif self.dir_x == 1:
            self.image.clip_composite_draw(192, 0, 32, 32, 0, '', self.x, self.y, 50, 50)
        else:
            self.image.clip_composite_draw(64, 0, 32, 32, 0, '', self.x, self.y, 50, 50)

class RUNcross:
    def enter(self, event):
        #print('ENTER RUNcross')

        if event == RD:
            self.dir_x += 1
        elif event == LD:
            self.dir_x -= 1
        elif event == UD:
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
        # print('EXIT RUNcross')
        pass


    def do(self):
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.x += self.dir_x * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.dir_y * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 400)
        self.y = clamp(0, self.y, 600)


    def draw(self):
        if self.dir_x == -1:
            self.image.clip_composite_draw(0, 0, 32, 32, 0, '', self.x, self.y, 50, 50)
        elif self.dir_x == 1:
            self.image.clip_composite_draw(192, 0, 32, 32, 0, '', self.x, self.y, 50, 50)
        else:
            self.image.clip_composite_draw(64, 0, 32, 32, 0, '', self.x, self.y, 50, 50)



next_state = {
    IDLE:      {RU: RUN,  LU: RUN,  RD: RUN,  LD: RUN,  UD: RUN,  DD: RUN,  UU: RUN,  DU: RUN, SPACE:IDLE},
    RUN:       {RU: IDLE, LU: IDLE, RD: RUNcross, LD: RUNcross, UD: RUNcross, DD: RUNcross, UU: IDLE, DU: IDLE, SPACE:RUN},
    RUNcross:  {RU: RUN, LU: RUN, RD: RUN, LD: RUN, UD: RUN, DD: RUN, UU: RUN, DU: RUN,SPACE:RUNcross}
}

PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 30.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_ACTION = 8



class Player:

    def __init__(self):
        self.x, self.y = 200, 50
        self.frame = 0
        self.dir_x = 0
        self.dir_y = 0
        self.image = load_image('resources\\Player.png')

        self.bullet_level = 1
        self.attack_power = 1

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
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def get_bb(self):
        size_weath = 7
        size_heigt = 7
        return self.x - size_weath, self.y - size_heigt, self.x + size_weath, self.y + size_heigt


    def handle_collision(self, other, group):

        if group == 'player:powerup':
            self.bullet_level += 1
            self.attack_power += 1
        if group == 'enemy_bullets:player':
            print("gameover")
        pass


def test_self():
    import play_state

    pico2d.open_canvas(400, 600)
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()

