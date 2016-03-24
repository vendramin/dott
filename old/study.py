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


class Bankbook(Item):
    def __init__(self):
        super(Bankbook, self).__init__('bankbook')
        self.rect = Rect(320, 176, 48, 32)
        self.poly = Rect2Polygon(self.rect)
        self.description = 'Swiss bankbook'
        self.room = 'study'
        self.z = 0
        self.set_image('items/bankbook.png')
    def on_pickup(self, game):
        super(Bankbook, self).on_pickup(game)
        game.rooms['study'].add_patch('rooms/study/desk.png', Rect(self.rect))

class BoobooBGone(Item):
    def __init__(self):
        super(BoobooBGone, self).__init__('booboo-b-gone')
        self.rect = Rect(342, 200, 65, 50)
        self.poly = Rect2Polygon(Rect(365, 205, 13, 20))
        self.description = 'Booboo-B-Gone'
        self.room = 'study'
        self.add_state(ROOM, 'rooms/study/open.png')
        self.set_image('items/booboo-b-gone.png')
        self.state = ROOM
        self.z = 1
       
class Drawer(StaticItem):
    def __init__(self):
        super(Drawer, self).__init__('drawer')
        self.rect = Rect(342, 200, 65, 50)
        self.poly = Rect2Polygon(self.rect)
        self.add_state(OPEN, 'rooms/study/empty.png')
        self.add_state(CLOSED, 'rooms/study/closed.png')
        self.state = CLOSED
        self.description = 'desk drawer'
        self.z = 2
    def on_open(self, game):
        self.state = OPEN
        self.z = 0
        game.rooms['study'].areas.sort(key=lambda x:x.z, reverse=True)
    def on_close(self, game):
        self.state = CLOSED
        self.z = 2
        game.rooms['study'].areas.sort(key=lambda x:x.z, reverse=True)
 
class StudyToLobby(Door):
    def __init__(self):
        super(StudyToLobby, self).__init__('study2lobby',  'study',  'lobby2study')
        self.rect = Rect(96, 64, 112, 160)
        self.poly = Rect2Polygon(self.rect) 
        self.add_state(OPEN, 'rooms/study/study2lobby.png')
        self.add_state(CLOSED)
        self.state = CLOSED 
  
class Study(Room):    
    
    def __init__(self):
        super(Study, self).__init__('study')
        self.set_image('rooms/study/study.png')
#        self.add_door(StudyToLobby())
        self.add_item(Drawer())


