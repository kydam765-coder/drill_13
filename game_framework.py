import time
running = False
stack = []


def change_mode(mode):
    if stack:
        stack.pop().finish()
    stack.append(mode)
    mode.init()


def push_mode(mode):
    if stack:
        stack[-1].pause()
    stack.append(mode)
    mode.init()


def pop_mode():
    if stack:
        stack.pop().finish()
    if stack:
        stack[-1].resume()
    else:
        quit()


def quit():
    global running
    running = False


def run(start_mode):
    global running, stack
    running = True
    stack = [start_mode]
    try:
        start_mode.init()
        while running:
            stack[-1].handle_events()
            first_mode = len(stack) - 1
            while (first_mode > 0 and
                   getattr(stack[first_mode], 'update_previous', False)):
                first_mode -= 1
            for mode in stack[first_mode:]:
                mode.update()
            stack[-1].render()
            time.sleep(0.02)
    finally:
        while stack:
            stack.pop().finish()
        running = False
