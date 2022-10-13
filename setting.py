from pico2d import *

open_canvas(400,400)

player = load_image('player(50x50).png')
enemy = load_image('enemy(50x50).png')

player.draw_now(200,0)
enemy.draw_now(200,400)

close_canvas()