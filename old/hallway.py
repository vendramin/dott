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

class HallwayToEdd(Door):
    def __init__(self):
        super(HallwayToEdd, self).__init__('hallway2edd',
                'hallway', 'edd2hallway')
        self.rect = Rect(384, 16, 80, 192)
        self.poly = Rect2Polygon(self.rect)
        self.add_state(OPEN, 'rooms/hallway/hallway2edd.png')
        self.add_state(CLOSED)
        self.state=CLOSED

class HallwayToEdna(Door):
    def __init__(self):
        super(HallwayToEdna, self).__init__('hallway2edna',
                'hallway', 'edna2hallway')
        self.rect = Rect(176, 16, 96, 176)
        self.poly = Rect2Polygon(self.rect)
        self.add_state(OPEN, 'rooms/hallway/hallway2edna.png')
        self.add_state(CLOSED)
        self.state=CLOSED

class HallwayToSecondfloor(Door):
    def __init__(self):
        super(HallwayToSecondfloor, self).__init__('hallway2secondfloor',
                'hallway', 'secondfloor2hallway')
        self.poly = Polygon((338, 13), (350, 120), (307, 150), (227, 47), (292, 13))
        self.add_state(OPEN)
        self.state=OPEN
        self.is_open = True
        self.description = 'stairway'
    def on_open(self, game):
        pass
    def on_close(self, game):
        pass

class HallwayToWarehouse(Door):
    def __init__(self):
        super(HallwayToWarehouse, self).__init__('hallway2warehouse',
                'hallway', 'warehouse2hallway')
        self.poly = Polygon((138, 207), (217, 251), (186, 300))
        self.add_state(OPEN)
        self.add_state(CLOSED)
        self.state=OPEN
        self.is_open = True
        self.description = 'stairway'
    def on_open(self, game):
        pass
    def on_close(self, game):
        pass
    def on_walk(self, game):
        if not game.doors[self.to].is_open:
            game.doors[self.to].is_open = True
            game.doors[self.to].state = OPEN
        game.room = game.rooms[game.doors[self.to].room]    
        #if not Door.d[self.to].is_open:
        #    Door.d[self.to].is_open = True
        #    Door.d[self.to].state = OPEN
        #game.room = game.rooms[Door.d[self.to].room]
 
class Hallway(Room):    
    
    def __init__(self):
        super(Hallway, self).__init__('hallway')
        self.set_image('rooms/hallway/hallway.png')
        self.add_patch('rooms/hallway/patch1.png', Rect(320, 144, 64, 48))
        self.add_patch('rooms/hallway/patch2.png', Rect(288, 160, 64, 32))


