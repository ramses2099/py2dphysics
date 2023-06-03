"""

class brickout represt game brick out
pygame and pymunk
03-06-2023

"""

import random
import pygame as pg
import pymunk as pmu
import pymunk.pygame_util as pmuutil
from setting import *
from player import Player


class BrickOut:
    def __init__(self, space, screen) -> None:
        self.space = space
        self.screen = screen
        self.player = Player(250, 50, self.space)

    def input(self, event):
        pass

    def draw(self, surface):
        self.player.draw(surface)

    def update(self):
        pass
