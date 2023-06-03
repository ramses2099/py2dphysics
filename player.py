import random
import pygame as pg
import pymunk as pmu
import pymunk.pygame_util as pmuutil
from setting import *
from utils import *


class Player:
    def __init__(self, x, y, space) -> None:
        self.mass = 1.0
        self.space = space

        self.image = pg.image.load(PLAYER_IMG)
        self.orig_image = self.image

        self.moment = pmu.moment_for_box(self.mass, (PLYAER_SIZE[0], PLYAER_SIZE[1]))
        self.body = pmu.Body(self.mass, self.moment)
        self.body.position = pmu.Vec2d(x, y)

        self.shape = pmu.Poly.create_box(self.body, (PLYAER_SIZE[0], PLYAER_SIZE[1]))
        self.shape.elasticity = 0.2
        self.shape.friction = 0.9
        self.space.add(self.body, self.shape)

    def draw(self, surface):
        x, y = to_pygame(self.shape.body.position)
        surface.blit(self.image, (x - 50, y - 10))

    def update(self):
        pass
