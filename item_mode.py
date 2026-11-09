from pico2d import *

import game_framework

image = None


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    image = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.pop_mode()
                return

            ball_types = {
                SDLK_0: 0,
                SDLK_1: 1,
                SDLK_2: 2,
            }
            if event.key in ball_types:
                import play_mode

                play_mode.boy.ball_type = ball_types[event.key]
                game_framework.pop_mode()
                return


def update():
    pass


def render():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
