import sys, random
import pygame as pg
import pymunk as pmu
import pymunk.pygame_util as pmuutil
from setting import *
from ball import Ball


# !  make the simulation the same each time, easier to debug
random.seed(1)


def show_fps(screen, clock, font):
    screen.blit(font.render(f"fps: {clock.get_fps()}", 1, WHITE), (10, 10))


# ? main function
def main():
    pg.init()

    screen = pg.display.set_mode((SCREEN_SIZE))
    pg.display.set_caption(SCREEN_TITLE)
    clock = pg.time.Clock()

    # ? font setting
    font = pg.font.SysFont("Arial", 16)

    # ? Spaces are the basic simulation unit in Chipmunk.
    # ? You add bodies, shapes and joints to a space, and then
    # ? update the space as a whole.
    space = pmu.Space()
    # setting for brick

    # pmuutil.positive_y_is_up = True
    # space.gravity = GRAVYTY

    ball = Ball(30, 10, space)

    # body
    segment_body = pmu.Body(body_type=pmu.Body.STATIC)
    # shape
    segment_shape = pmu.Segment(segment_body, (0, 300), (600, 450), 15)
    segment_shape.elasticity = 1
    space.add(segment_body, segment_shape)

    # ? debug option in pymunk
    if DEBUG:
        draw_option = pmuutil.DrawOptions(screen)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit(0)
            # Brick-out input

        screen.fill(BLACK)
        if DEBUG:
            space.debug_draw(draw_option)
            # show fps
            show_fps(screen, clock, font)

        ball.draw(screen)
        pg.draw.line(screen, BLUE, (0, 300), (600, 450), 15)
        # draw
        # Brick-out draw

        space.step(STEP)

        pg.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    sys.exit(main())
