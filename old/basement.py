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

class BasementToLobby(Door):
    def __init__(self):
        super(BasementToLobby, self).__init__('basement2lobby',  'basement', 'lobby2basement')
        self.poly = Rect2Polygon(Rect(716, 10, 80, 115))
        self.add_state(OPEN)
        self.state=OPEN
        self.is_open = True
    def on_open(self, game):
        pass
    def on_close(self, game):
        pass

class Basement(Room):
    def __init__(self):
        super(Basement, self).__init__('basement')
        self.set_image('rooms/basement/basement.png')
#        self.add_door(BasementToLobby())
