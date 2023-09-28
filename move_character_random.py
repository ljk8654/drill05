import turtle
import random
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')





x, y = 0, 0 #이동하는 위치
x1, y1 = 0, 0 #원래 위치
frame = 0
while True:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    arrow_x,arrow_y = random.randint(40,900),random.randint(150,900)
    arrow.clip_draw(0, 0, 50, 52, arrow_x, arrow_y)
    x2,y2 = arrow_x,arrow_y
    x1, y1 = x, y
    while (x != x2):
        for i in range(0, 100 + 1, 5):
            t = i / 100
            x = (1 - t) * x1 + t * x2
            y = (1 - t) * y1 + t * y2
            clear_canvas()
            TUK_ground.draw(1024 // 2, 1280 // 2)
            arrow.clip_draw(0, 0, 50, 52, arrow_x, arrow_y)
            if x2 > x:
                character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
            elif x2 < x:
                character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', x, y, 100,100)
            update_canvas()
            frame = (frame + 1) % 8
            delay(0.1)
