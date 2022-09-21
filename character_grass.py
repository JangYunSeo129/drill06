from pico2d import *
# 임포트의 방식 변환 pico2d가 갖고이ㅛ는걸 몽땅다 임포트해라~ pico2d.을 쓸필요가 없어짐

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
while (x < 800):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,90)
    x = x+ 2
    delay(0.008)

close_canvas()
