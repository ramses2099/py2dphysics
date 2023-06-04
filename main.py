import sys, random
import pygame as pg
import pymunk as pmu
import pymunk.pygame_util as pmuutil
from setting import *

# GLOBAL VARIABLE
pg.init()

screen = pg.display.set_mode((SCREEN_SIZE))
pg.display.set_caption(SCREEN_TITLE)
clock = pg.time.Clock()

# font setting
font = pg.font.SysFont("Arial", 16)
space = pmu.Space()
static_body = space.static_body

# GLOBAL VARIABLE


def show_fps():
    screen.blit(font.render(f"fps: {clock.get_fps()}", 1, WHITE), (10, 10))


# create ball
def create_ball(radius, pos):
    body = pmu.Body()
    body.position = pos
    shape = pmu.Circle(body, radius)
    shape.mass = 5

    # use pivot joint to add friction
    pivot = pmu.PivotJoint(static_body, body, (0, 0), (0, 0))
    pivot.max_bias = 0
    pivot.max_force = 1000

    space.add(body, shape, pivot)
    return shape


# main function
def main():
    ball = create_ball(25, (250, 100))
    # use

    cue_ball = create_ball(25, (450, 100))

    # debug option in pymunk
    if DEBUG:
        draw_option = pmuutil.DrawOptions(screen)

    while True:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                cue_ball.body.apply_impulse_at_local_point((-1500, 0), (0, 0))
            if event.type == pg.QUIT:
                sys.exit(0)
            # Brick-out input

        screen.fill(BLACK)
        if DEBUG:
            space.debug_draw(draw_option)
            # show fps
            show_fps()

        space.step(STEP)
        pg.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    sys.exit(main())
