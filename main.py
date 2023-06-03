import sys, random
import pygame as pg
import pymunk as pmu
import pymunk.pygame_util as pmuutil
from setting import *

# !  make the simulation the same each time, easier to debug
random.seed(1)


# ! draw manually
def draw_ball(screen: pg.Surface, ball: pmu.Shape) -> None:
    p = int(ball.body.position.x), int(ball.body.position.y)
    pg.draw.circle(screen, RED, p, int(ball.radius), 2)


# ! add falling ball to space
def add_ball(space):
    mass = 3
    raidus = 25
    # rigid body
    body = pmu.Body()
    x = random.randint(120, 300)
    body.position = x, 50
    # ?Base class for all the shapes.
    # ? You usually dont want to create instances of this class directly
    # ? but use one of the specialized shapes instead (Circle, Poly or Segment).
    shape = pmu.Circle(body, raidus)
    shape.mass = mass
    shape.friction = 1
    space.add(body, shape)
    return shape


# ! add static body
def add_static_L(space):
    body = pmu.Body(body_type=pmu.Body.STATIC)
    body.position = (300, 300)
    l1 = pmu.Segment(body, (-150, 0), (255, 0), 5)
    l2 = pmu.Segment(body, (-150, 0), (-150, -50), 5)
    l1.friction = 1
    l2.friction = 2
    space.add(body, l1, l2)
    return l1, l2


# ! Small helper to convert pymunk vec2d to pygame integers
def to_pygame(p):
    return round(p.x), round(p.y)


# ! draw lines
def draw_lines(screen, lines):
    for line in lines:
        body = line
        pv1 = body.position + line.a.rotated(body.angle)
        pv2 = body.position + line.b.rotated(body.angle)
        p1 = to_pygame(pv1)
        p2 = to_pygame(pv2)
        pg.draw.line(screen, GREEN, False, [p1, p2])


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

    lines = add_static_L(space)

    # ? debug option in pymunk
    if DEBUG:
        draw_option = pmuutil.DrawOptions(screen)
    balls = []

    # ball = add_ball(space)

    ticks_to_next_ball = 10
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit(0)

        screen.fill(BLACK)
        if DEBUG:
            space.debug_draw(draw_option)

        # update
        ticks_to_next_ball -= 1
        if ticks_to_next_ball <= 0:
            thicks_to_next_ball = 25
            ball_shape = add_ball(space)
            balls.append(ball_shape)

        # draw
        # draw_ball(screen, ball)

        space.step(STEP)

        pg.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    sys.exit(main())
