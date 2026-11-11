from pathlib import Path
from time import perf_counter, sleep

from pico2d import (
    SDL_KEYDOWN, SDL_QUIT, SDLK_ESCAPE,
    clear_canvas, close_canvas, get_events, load_image, open_canvas, update_canvas,
)

from flock import Flock


WIDTH, HEIGHT = 800, 480
FRAME_INTERVAL = 1 / 60
SKY_COLOR = (210, 234, 250)


def main():
    open_canvas(WIDTH, HEIGHT)
    try:
        asset_path = Path(__file__).resolve().with_name('bird_animation.png')
        sheet = load_image(str(asset_path))
        flock = Flock(WIDTH, HEIGHT)
        previous_time = perf_counter()

        while True:
            frame_start = perf_counter()
            events = get_events()
            if any(event.type == SDL_QUIT or
                   (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE)
                   for event in events):
                break

            flock.update(frame_start - previous_time)
            previous_time = frame_start
            clear_canvas(*SKY_COLOR)
            flock.draw(sheet)
            update_canvas()

            remaining_time = FRAME_INTERVAL - (perf_counter() - frame_start)
            if remaining_time > 0:
                sleep(remaining_time)
    finally:
        close_canvas()


if __name__ == '__main__':
    main()
