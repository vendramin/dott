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
freezer: 40,88,48,24
monedas: 136,80,192,64
"""

class SecondfloorToSuite(Door):
    def __init__(self):
        super(SecondfloorToSuite, self).__init__('secondfloor2suite',  'secondfloor', 'suite2secondfloor')
        self.rect = Rect(224, 32, 96, 160)
        self.poly = Rect2Polygon(Rect(self.rect))
        self.add_state(OPEN, 'rooms/secondfloor/secondfloor2suite.png')
        self.add_state(CLOSED)
        self.state = CLOSED

class SecondfloorToSad(Door):
    def __init__(self):
        super(SecondfloorToSad, self).__init__('secondfloor2sad',  'secondfloor', 'sad2secondfloor')
        self.rect = Rect(496, 32, 80, 160)
        self.poly = Rect2Polygon(self.rect)
        self.add_state(OPEN, 'rooms/secondfloor/secondfloor2sad.png')
        self.add_state(CLOSED)
        self.state = CLOSED

class SecondfloorToGreen(Door):
    def __init__(self):
        super(SecondfloorToGreen, self).__init__('secondfloor2green',  'secondfloor', 'green2secondfloor')
        self.rect = Rect(656, 64, 64, 96)
        self.poly = Rect2Polygon(self.rect)
        self.add_state(OPEN, 'rooms/secondfloor/secondfloor2green.png')
        self.add_state(CLOSED)
        self.state = CLOSED
        
class SecondfloorToHallway(Door):
    def __init__(self):
        super(SecondfloorToHallway, self).__init__('secondfloor2hallway',
                'secondfloor', 'hallway2secondfloor')
        self.poly = Polygon((794, 90), (844, 90), (823, 160), (773, 153)); 
        self.add_state(OPEN)
        self.state = OPEN
        self.is_open = True
        self.description = 'stairs'

    def on_open(self, game):
        pass
    def on_close(self, game):
        pass

class SecondfloorToLobby(Door):
    def __init__(self):
        super(SecondfloorToLobby, self).__init__('secondfloor2lobby',  'secondfloor', 'lobby2secondfloor')
        self.poly = Rect2Polygon(Rect(151, 102, 50, 70))
        self.add_state(OPEN)
        self.state=OPEN
        self.is_open = True
        self.description = 'stairs'

    def on_open(self, game):
        pass
    def on_close(self, game):
        pass

class Secondfloor(Room):
    def __init__(self):
        super(Secondfloor, self).__init__('secondfloor')
        self.set_image('rooms/secondfloor/secondfloor.png')

