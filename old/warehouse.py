import pygame
import sys

import scupy

from scupy.room import Room
from scupy.item import Item, Door
from scupy.actor import Actor
from scupy.geometry import Point2D, Point3D, Polygon, Rect2Polygon

from pygame.locals import *
from scupy.config import *

__metaclass__ = type

class WarehouseToHallway(Door):
    def __init__(self):
        super(WarehouseToHallway, self).__init__('warehouse2hallway',
                'warehouse', 'hallway2warehouse')
        self.rect = Rect(16, 128, 192, 160)
        self.poly = Rect2Polygon(self.rect) 
        self.add_state(OPEN, 'rooms/warehouse/warehouse2hallway.png')
        self.add_state(CLOSED)
        self.state=OPEN
        self.is_open = True
  
class WarehouseToAttic(Door):
    def __init__(self):
        super(WarehouseToAttic, self).__init__('warehouse2attic',
                'warehouse', 'attic2warehouse')
        self.rect = Rect(464, 48, 112, 160)
        self.poly = Rect2Polygon(self.rect) 
        self.add_state(OPEN, 'rooms/warehouse/warehouse2attic.png')
        self.add_state(CLOSED)
        self.state=CLOSED
    def on_open(self, game):
        super(WarehouseToAttic, self).on_open(game)
        #game.rooms['attic'].items['bed'].state = OPEN

    def on_close(self, game):
        super(WarehouseToAttic, self).on_close(game)
        #game.rooms['attic'].items['bed'].state = CLOSED

class Warehouse(Room):    
    
    def __init__(self):
        super(Warehouse, self).__init__('warehouse')
        self.set_image('rooms/warehouse/warehouse.png')


