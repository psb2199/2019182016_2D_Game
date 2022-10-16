from pico2d import *

open_canvas(500,700)

player = load_image('player(50x50).png')
enemy = load_image('enemy(50x50).png')

player.draw_now(250,50)
enemy.draw_now(250,650)

delay(10)

close_canvas()