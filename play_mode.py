from pico2d import *

import game_framework
import game_world
from boy import Boy
from grass import Grass

boy = None


def init():
    global boy
    game_world.clear()
    game_world.add_oject(Grass(), 0)
    boy = Boy()
    game_world.add_oject(boy)


def finish():
    global boy
    game_world.clear()
    boy = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            import pause_mode

            game_framework.push_mode(pause_mode)
            return
        if event.type == SDL_KEYDOWN and event.key == SDLK_i:
            import item_mode

            game_framework.push_mode(item_mode)
            return
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            import title_mode

            game_framework.change_mode(title_mode)
            return
        boy.handle_event(event)


def pause():
    pass


def resume():
    pass


def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()
