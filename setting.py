from pico2d import *

open_canvas(500,700)

player = load_image('player(50x50).png')
enemy = load_image('enemy(50x50).png')

player.draw_now(250,50)
enemy.draw_now(250,650)

y = 0
while (y<650):
    clear_canvas_now()
    player.draw_now(250,50)
    enemy.draw_now(250,650-y)
    y += 2
    delay(0.01)

close_canvas()