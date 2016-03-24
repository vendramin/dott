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
class CarToWater(Door):
    def __init__(self):
        super(CarToWater, self).__init__('car2water',
                'car',  'water2car')
        self.rect = Rect(550, 0, 90, 170)
        self.poly = Rect2Polygon(self.rect) 
        self.add_state(OPEN)
        self.state = OPEN
        self.description = 'path'
        self.is_open = True
    def on_open(self, game):
        pass
    def on_close(self, game):
        pass
 
class CarToOutside(Door):
    def __init__(self):
        super(CarToOutside, self).__init__('car2outside',
                'car',  'outside2car')
        self.rect = Rect(175, 0, 150, 150)
        self.poly = Rect2Polygon(self.rect) 
        self.add_state(OPEN)
        self.state = OPEN
        self.is_open = True
        self.description = 'motel'
    def on_open(self, game):
        pass
    def on_close(self, game):
        pass
  
class Car(Room):    
    
    def __init__(self):
        super(Car, self).__init__('car')
        self.set_image('rooms/car/car.png')
#        self.add_door(CarToOutside())
#        self.add_door(CarToWater())


