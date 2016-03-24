import pygame
import sys

import scupy

from scupy.room import Room 
from scupy.item import Item, Door, StaticItem
from scupy.actor import Actor
from scupy.geometry import Point2D, Point3D, Polygon, Rect2Polygon

from pygame.locals import *
from scupy.config import *

__metaclass__ = type

class Statue(StaticItem):
     def __init__(self):
        super(Statue, self).__init__('statue')
        self.rect = Rect(448, 16, 96, 176)
        self.poly = Rect2Polygon(self.rect) 
        self.add_state(LEFT, 'rooms/edna/statue1.png')
        self.add_state(RIGHT, 'rooms/edna/statue2.png')
        self.state = LEFT
        self.description = 'statue'
        self.z = 1

class EdnaToHallway(Door):
    def __init__(self):
        super(EdnaToHallway, self).__init__('edna2hallway', 'edna', 'hallway2edna')
        self.rect = Rect(528, 48, 80, 160)
        self.poly = Rect2Polygon(self.rect) 
        self.add_state(OPEN, 'rooms/edna/open.png')
        self.add_state(CLOSED, 'rooms/edna/closed.png')
        self.state=OPEN
  
class Edna(Room):    
    def __init__(self):
        super(Edna, self).__init__('edna')
        self.set_image('rooms/edna/edna.png')
#        self.add_door(EdnaToHallway())
        self.add_item(Statue())


