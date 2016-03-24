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

class Ink(Item):
    def __init__(self):
        super(Ink, self).__init__('ink')
        self.rect = Rect(512, 160, 32, 48)
        self.poly = Rect2Polygon(self.rect)
        self.z = 1
        self.description = 'ink'
        self.add_state(ROOM, 'rooms/sad/ink.png')
        self.state = ROOM
        self.set_image('items/ink.png')
        self.room = 'sad'

    def on_use(self, game, other=None):
        if not other == None:
            if other.name == 'stamp album':
                pass
        


#   def on_pickup(self, game):
#        game.player.take_item(self)
#        del game.room.items[self.name]
#        game.room.areas.remove((self, self.z))
#        # Modify the rooms from where this phone is visible
#        game.rooms['sad'].add_patch('rooms/lobby/nocoin.png', Rect(528, 96, 64, 96))
  
class SadToSecondfloor(Door):
    def __init__(self):
        super(SadToSecondfloor, self).__init__('sad2secondfloor', 'sad',  'secondfloor2sad')
        self.rect = Rect(448, 48, 96, 192)
        self.poly = Rect2Polygon(self.rect) 
        self.add_state(OPEN, 'rooms/sad/locked.png')
        self.add_state(CLOSED)
        self.state=OPEN

    def on_close(self, game):
        # if the door is locked...
        if self.state == OPEN:
            self.state = CLOSED
            game.doors[self.to].state = CLOSED
#            game.room = game.rooms[Door.d[self.to].room]
#            game.room = game.rooms[game.doors[self.to]].room
  
class Sad(Room):    
    def __init__(self):
        super(Sad, self).__init__('sad')
        self.set_image('rooms/sad/sad.png')

