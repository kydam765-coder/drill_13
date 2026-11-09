from pico2d import *

import game_framework

image = None
update_previous = True


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    image = None


def pause():
    pass


def resume():
    pass


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.pop_mode()
                return
            if event.key in (SDLK_0, SDLK_1, SDLK_2):
                import play_mode

                play_mode.boy.ball_type = {
                    SDLK_0: 0,
                    SDLK_1: 1,
                    SDLK_2: 2,
                }[event.key]
                game_framework.pop_mode()
                return
            if event.key == SDLK_i:
                continue

        import play_mode

        if play_mode.handle_event(event):
            return


def update():
    pass


def render():
    import play_mode

    play_mode.render_scene()
    image.draw(400, 300)
    update_canvas()
