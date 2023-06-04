import sys, random
import pygame as pg
import pymunk as pmu
import pymunk.pygame_util as pmuutil
from setting import *


class Ball:
    def __init__(self, x, y, space) -> None:
        # body
        self.body = pmu.Body()
        self.body.position = x, y
        # shape
        self.shape = pmu.Circle(self.body, BALL_RADIUS)
        self.shape.density = 1
        self.shape.elasticity = 1
        self.space = space
        self.space.add(self.body, self.shape)

        self.ball_image = pg.image.load(BALL_IMG)

    def draw(self, surface):
        # update
        x, y = self.body.position
        # pg.draw.circle(screen, RED, (int(x), int(y)), BALL_RADIUS)
        surface.blit(self.ball_image, (int(x) - BALL_RADIUS, int(y) - BALL_RADIUS))
