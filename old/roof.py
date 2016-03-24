import pygame
import sys

import scupy

from scupy.room import Room
from scupy.item import Item, Door
from scupy.actor import Actor
from scupy.geometry import Point2D, Point3D, Polygon,  Rect2Polygon

from pygame.locals import *
from scupy.config import *

__metaclass__ = type

class Crank(Item):
    pass

class RoofToAttic(Door):
    def __init__(self):
        super(RoofToAttic, self).__init__('roof2attic',  'roof', 'attic2roof')
        self.poly = Polygon((440, 185), (496, 185), (504, 236), (466, 238))
        self.add_state(OPEN)
        self.state=OPEN
        self.is_open = True
        self.description = 'window'
    def on_open(self, game):
        pass
    def on_close(self, game):
        pass

class RoofToPlayroom(Door):
    def __init__(self):
        super(RoofToPlayroom, self).__init__('roof2playroom',  'roof', 'playroom2kitchen')
        self.poly = Polygon((140, 141), (169, 115), (227, 123), (233, 194), (196, 206))
        self.add_state(OPEN)
        self.state=OPEN
        self.is_open = True
        self.description = 'chimney'
    def on_open(self, game):
        pass
    def on_close(self, game):
        pass

class Roof(Room):
    def __init__(self):
        super(Roof, self).__init__('roof')
        self.set_image('rooms/roof/roof.png')
