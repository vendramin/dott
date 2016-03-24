import pygame
import sys

import scupy

from scupy.room import Room 
from scupy.item import Item, Door, StaticItem
from scupy.actor import Actor
from scupy.geometry import Point2D, Point3D, Polygon,  Rect2Polygon

from pygame.locals import *
from scupy.config import *

__metaclass__ = type

"""
bed: 120, 64, 96, 56
"""

class Bed(StaticItem):
    def __init__(self):
        super(Bed, self).__init__('bed')
        self.rect = Rect(240, 128, 192, 112)
        self.poly = Rect2Polygon(self.rect)
        self.description = ''
        self.add_state(OPEN, 'rooms/attic/bed.png')
        self.add_state(CLOSED)
        self.state = CLOSED

class AtticToRoof(Door):
    def __init__(self):
        super(AtticToRoof, self).__init__('attic2roof',  'attic', 'roof2attic')
        self.poly = Polygon((127, 92), (152, 100), (152, 157), (118, 175))
        self.add_state(OPEN)
        self.state=OPEN
        self.is_open = True
        self.description = 'window'
    def on_open(self, game):
        pass
    def on_close(self, game):
        pass

class AtticToWarehouse(Door):
    def __init__(self):
        super(AtticToWarehouse, self).__init__('attic2warehouse',  'attic',
                'warehouse2attic')
        self.rect = Rect(432, 32, 96, 160) 
        self.poly = Rect2Polygon(self.rect)
        self.add_state(OPEN, 'rooms/attic/attic2file.png')
        self.add_state(CLOSED)
        self.state = CLOSED

    def on_open(self, game):
        super(AtticToWarehouse, self).on_open(game)
        #game.rooms['attic'].items['bed'].state = OPEN

    def on_close(self, game):
        super(AtticToWarehouse, self).on_close(game)
        #game.rooms['attic'].items['bed'].state = CLOSED

class Attic(Room):
    def __init__(self):
        super(Attic, self).__init__('attic')
        self.set_image('rooms/attic/attic.png')
        self.add_item(Bed())
