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

""" 
lavaropas(2): 184,72,56,40
lavarropas lavando: 192, 80, 40, 32
lavarropas listo: 192, 96, 32, 16
"""

class Funnel(Item):
    def __init__(self):
        super(Funnel, self).__init__('funnel')
        self.rect = Rect(256, 160, 48, 16)
        self.poly = Rect2Polygon(Rect(265, 159, 20, 20))
        self.description = 'funnel'
        self.add_state(ROOM, 'rooms/laundry/funnel.png')
        self.state = ROOM
        self.room = 'laundry'
        self.z = 1
        self.set_image('items/funnel.png')

class Cabinet(StaticItem):
    def __init__(self):
        super(Cabinet, self).__init__('cabinet')
        self.rect = Rect(224, 144, 96, 64)
        self.poly = Rect2Polygon(self.rect)
        self.description = 'cabinet'
        self.add_state(CLOSED, 'rooms/laundry/closed.png')
        self.add_state(OPEN, 'rooms/laundry/open.png')
        self.state = CLOSED
        self.z = 2
    def on_open(self, game):
        self.state = OPEN
        self.z = 0
        game.rooms['laundry'].areas.sort(key=lambda x:x.z, reverse=True)
      
    def on_close(self, game):
        self.state = CLOSED
        self.z = 2
        game.rooms['laundry'].areas.sort(key=lambda x:x.z, reverse=True)
    
class LaundryToKitchen(Door):
    def __init__(self):
        super(LaundryToKitchen, self).__init__('laundry2kitchen',
                'laundry',  'kitchen2laundry')
        self.rect = Rect(144, 64, 80, 160)
        self.poly = Rect2Polygon(self.rect) 
        self.add_state(OPEN, 'rooms/laundry/laundry2kitchen.png')
        self.add_state(CLOSED)
        self.state = CLOSED
  
class Laundry(Room):    
    
    def __init__(self):
        super(Laundry, self).__init__('laundry')
        self.set_image('rooms/laundry/laundry.png')
        self.add_item(Cabinet())


