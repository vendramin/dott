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

"""
cafe: 16, 64, 40, 40
48, 64, 32, 40
tenedor: 176,96, 32, 16
"""
class Coffee(Item):
    def __init__(self):
        super(Coffee, self).__init__('coffee')
        self.rect = Rect(42, 139, 80, 80)
        self.poly = Rect2Polygon(Rect(47, 140, 53, 56))
        self.description = 'coffee'
        self.add_state(ROOM, 'rooms/kitchen/coffee.png')
        self.state = ROOM
        self.room = 'kitchen'
        self.set_image('items/coffee.png')
        self.z = 1

class DecafCoffee(Item):
    def __init__(self):
        super(DecafCoffee, self).__init__('decaf-coffee')
        self.rect = Rect(96, 138, 64, 80)
        self.poly = Rect2Polygon(Rect(98, 142, 46, 44))
        self.description = 'decaf-coffee'
        self.room = 'kitchen'
        self.set_image('items/decaf-coffee.png')
        self.add_state(ROOM, 'rooms/kitchen/decaf-coffee.png')
        self.state = ROOM
        self.z = 0
 
class Fork(Item):
    def __init__(self):
        super(Fork, self).__init__('fork')
        self.rect = Rect(352, 192, 64, 32)
        self.poly = Rect2Polygon(self.rect)
        self.description = 'fork'
        self.add_state(ROOM, 'rooms/kitchen/fork.png')
        self.state = ROOM
        self.room = 'kitchen'
        self.set_image('items/fork.png')

class KitchenToLaundry(Door):
    def __init__(self):
        super(KitchenToLaundry, self).__init__('kitchen2laundry',
                'kitchen', 'laundry2kitchen')
        self.rect = Rect(464, 32, 64, 172)
        self.poly = Rect2Polygon(self.rect)
        self.add_state(OPEN, 'rooms/kitchen/kitchen2laundry.png')
        self.add_state(CLOSED)
        self.state=CLOSED

class KitchenToPlayroom(Door):
    def __init__(self):
        super(KitchenToPlayroom, self).__init__('kitchen2playroom',  'kitchen', 'playroom2kitchen')
        self.poly = Rect2Polygon(Rect(368,  64,  80,  128))
        self.add_state(OPEN)
        self.state=OPEN
        self.is_open = True

class Kitchen(Room):
    def __init__(self):
        super(Kitchen, self).__init__('kitchen')
        self.set_image('rooms/kitchen/kitchen.png')
#        self.add_door(KitchenToPlayroom())
#        self.add_door(KitchenToLaundry())
