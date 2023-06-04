import sys, random, os.path
import pygame as pg
import pymunk as pmu
import pymunk.pygame_util as pmuutil
from pymunk import Vec2d
from setting import *

# GLOBAL VARIABLE
pg.init()

screen = pg.display.set_mode((SCREEN_SIZE))
pg.display.set_caption(SCREEN_TITLE)
clock = pg.time.Clock()

# font setting
font = pg.font.SysFont("Arial", 16)
space = pmu.Space()
space.gravity = Vec2d(0.0, 900.0)


# GLOBAL VARIABLE
"""element_blue_polygon_glossy.png"""
img = pg.image.load(
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "assets\\element_blue_polygon_glossy.png",
    )
)

mass = 10.0
moment = pmu.moment_for_box(mass, (48, 46))
body = pmu.Body(mass=mass, moment=moment)
body.position = 350, 50
# shape
shape = pmu.Poly.create_box(body, (48, 46))
shape.density = 1
shape.elasticity = 1
space.add(body, shape)


segment = pmu.Segment(space.static_body, (11.0, 280.0), (407.0, 246.0), 0.0)
space.add(segment)


def show_fps():
    screen.blit(font.render(f"fps: {clock.get_fps()}", 1, WHITE), (10, 10))


# main function
def main():
    # debug option in pymunk
    if DEBUG:
        draw_option = pmuutil.DrawOptions(screen)

    while True:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                pass
            if event.type == pg.QUIT:
                sys.exit(0)
            # Brick-out input

        screen.fill(BLACK)
        if DEBUG:
            space.debug_draw(draw_option)
            # show fps
            show_fps()

        p = shape.body.position
        p = Vec2d(p.x, p.y)

        rect = img.get_rect()
        # print(f"w{rect.width},h{rect.height}")
        offset = Vec2d((rect.width / 2), (rect.height / 2))
        p = p - offset

        screen.blit(img, (int(p.x), int(p.y)))

        space.step(STEP)
        pg.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    sys.exit(main())
