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

class EddToHallway(Door):
    def __init__(self):
        super(EddToHallway, self).__init__('edd2hallway',
                'edd',  'hallway2edd')
        self.rect = Rect(112, 32, 64, 176)
        self.poly = Rect2Polygon(self.rect) 
        self.add_state(OPEN, 'rooms/edd/edd2hallway.png')
        self.add_state(CLOSED)
        self.state=OPEN
  
class Edd(Room):    
    
    def __init__(self):
        super(Edd, self).__init__('edd')
        self.set_image('rooms/edd/edd.png')
#        self.add_door(EddToHallway())


