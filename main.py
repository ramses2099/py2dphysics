import sys
import pygame as pg
import pymunk as pmu
from setting import *


# ? main function
def main():
    pg.init()

    screen = pg.display.set_mode((SCREEN_SIZE))
    pg.display.set_caption(SCREEN_TITLE)
    clock = pg.time.Clock()

    # ? Spaces are the basic simulation unit in Chipmunk.
    # ? You add bodies, shapes and joints to a space, and then update the space as a whole.
    space = pmu.Space()
    space.gravity = GRAVYTY

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit(0)

        screen.fill(BLACK)

        space.step(STEP)

        pg.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    sys.exit(main())
