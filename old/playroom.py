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

class PlayroomToRoof(Door):
    def __init__(self):
        super(PlayroomToRoof, self).__init__('playroom2roof', 'playroom', 'roof2playroom')
        self.poly = Polygon((433, 129), (593, 111), (487, 214), (457, 211))
        self.add_state(OPEN)
        self.state=OPEN
        self.is_open = True
        self.description = 'chimney'

    def on_open(self, game):
        pass
    def on_close(self, game):
        pass 
 
class PlayroomToKitchen(Door):
    def __init__(self):
        super(PlayroomToKitchen, self).__init__('playroom2kitchen', 'playroom', 'kitchen2playroom')
        self.rect = Rect(288, 80, 80, 112)
        self.poly = Polygon((360,192), (374, 98), (327, 97), (330, 189))
        self.add_state(OPEN)
        self.state=OPEN
        self.is_open = True
        self.description = 'swinging door'

    def on_open(self, game):
        pass
    def on_close(self, game):
        pass 
    
class Grating(StaticItem):
    def __init__(self):
        super(Grating, self).__init__('grating')
        self.rect = Rect(336, 144, 80, 64)
        self.poly = Polygon((356, 205), (369, 197), (415, 204), (397, 218))
        self.add_state(OPEN, 'rooms/playroom/grating.png')
        self.add_state(CLOSED)
        self.state = CLOSED
        self.description = 'grating'
    def on_push(self, game):
        self.on_close(game)
    def on_pull(self, game):
        self.on_open(game)
    def on_open(self, game):
        self.state = OPEN
    def on_close(self, game):
        self.state = CLOSED

class PlayroomToLobby(Door):
    def __init__(self):
        super(PlayroomToLobby, self).__init__('playroom2lobby',  'playroom',  'lobby2playroom')
        self.rect = Rect(48, 80, 112, 176)
        self.poly = Rect2Polygon(self.rect)
        self.add_state(OPEN, 'rooms/playroom/playroom2lobby.png')
        self.add_state(CLOSED)
        self.state = CLOSED
        
class Playroom(Room):    
    def __init__(self):
        super(Playroom, self).__init__('playroom')
        self.set_image('rooms/playroom/playroom.png')
        self.add_item(Grating())

