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

class Keys(Item):
    def __init__(self):
        super(Keys, self).__init__('keys')
        self.rect = Rect(118, 122, 20, 25)
        self.poly = Rect2Polygon(Rect(103, 112, 17, 24))
        self.add_state(ROOM)
        self.state = ROOM
        self.room = 'suite'
        self.description = 'keys'
        self.z = 1 
        self.set_image('items/keys.png')

    def on_pickup(self, game):
        super(Keys, self).on_pickup(game)
        game.doors['suite2secondfloor'].modify_state(CLOSED, 'rooms/suite/closed_nokey.png')
        game.doors['suite2secondfloor'].modify_state(OPEN, 'rooms/suite/open_nokey.png')

class SuiteToSecondfloor(Door):
    def __init__(self):
        super(SuiteToSecondfloor, self).__init__('suite2secondfloor',
                'suite',  'secondfloor2suite')
        self.rect = Rect(0, 0, 128, 192)
        self.poly = Rect2Polygon(self.rect) 
        self.add_state(OPEN, 'rooms/suite/open.png')
        self.add_state(CLOSED)
        self.state = CLOSED
        self.is_open = False
        self.z = 2 

    def on_open(self, game):
        super(SuiteToSecondfloor, self).on_open(game)
        self.z = 2
        game.rooms['suite'].areas.sort(key=lambda x:x.z, reverse=True)
 
    def on_close(self, game):
        super(SuiteToSecondfloor, self).on_close(game)
        self.z = 0
        game.rooms['suite'].areas.sort(key=lambda x:x.z, reverse=True)
 
class Suite(Room):    
    def __init__(self):
        super(Suite, self).__init__('suite')
        self.set_image('rooms/suite/suite.png')


