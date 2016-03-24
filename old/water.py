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

""" 
"""

class WaterToCar(Door):
    def __init__(self):
        super(WaterToCar, self).__init__('water2car',
                'water',  'car2water')
        self.rect = Rect(0, 0, 150, 300)
        self.poly = Rect2Polygon(self.rect) 
        self.add_state(OPEN)
        self.state = OPEN
        self.is_open = True
        self.description = 'path'

    def on_open(self):
        pass
    def on_close(self):
        pass
  
class Water(Room):    
    
    def __init__(self):
        super(Water, self).__init__('water')
        self.set_image('rooms/water/water.png')


