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
        if handle_event(event):
            return


def handle_event(event):
    if event.type == SDL_QUIT:
        game_framework.quit()
        return True
    if event.type == SDL_KEYDOWN and event.key == SDLK_p:
        import pause_mode

        game_framework.push_mode(pause_mode)
        return True
    if event.type == SDL_KEYDOWN and event.key == SDLK_i:
        import item_mode

        game_framework.push_mode(item_mode)
        return True
    if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
        import title_mode

        game_framework.change_mode(title_mode)
        return True
    boy.handle_event(event)
    return False


def pause():
    pass


def resume():
    pass


def update():
    game_world.update()


def render_scene():
    clear_canvas()
    game_world.render()


def render():
    render_scene()
    update_canvas()
