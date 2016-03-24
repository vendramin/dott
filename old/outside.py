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

class Window(StaticItem):
    def __init__(self):
        super(Window, self).__init__('window')
        self.rect = Rect(640, 32, 96, 64)
        self.poly = Rect2Polygon(self.rect)
        self.description = 'window'

class BirdBath(StaticItem):
     def __init__(self):
        super(BirdBath, self).__init__('birdbath')
        self.rect = Rect(440, 164, 100, 20)
        self.poly = Rect2Polygon(self.rect)
        self.description = 'bird bath'
        self.z = 2

class Mummy(StaticItem):
     def __init__(self):
        super(Mummy, self).__init__('mummy')
        self.rect = Rect(432, 92, 112, 160)
        self.poly = Rect2Polygon(self.rect)
        self.add_state('mummy', 'rooms/outside/mummy.png')
        self.state = 'mummy'
        self.description = 'Dead Cousin Ted' 
        self.z = 1

class Mailbox(StaticItem):
    def __init__(self):
        super(Mailbox, self).__init__('mailbox')
        self.rect = Rect(800, 96, 64, 48); 
        self.poly = Rect2Polygon(self.rect)
        self.add_state(OPEN, 'rooms/outside/mailbox.png')
        self.description = 'mailbox'
        self.add_state(CLOSED)
        self.state = CLOSED

    def on_open(self, game):
        self.state = OPEN
            
    def on_close(self, game):
        self.state = CLOSED

class OutsideToCar(Door):
    def __init__(self):
        super(OutsideToCar, self).__init__('outside2car',  'outside',
                'car2outside')
        self.rect = Rect(915, 0, 50, 300)
        self.poly = Rect2Polygon(self.rect)
        self.add_state(OPEN)
        self.state = OPEN
        self.is_open = True
        self.description = 'parking lot'

    def on_close(self, game):
        pass
    def on_open(self, game):
        pass

class OutsideToLobby(Door):
    def __init__(self):
        super(OutsideToLobby, self).__init__('outside2lobby',  'outside', 'lobby2outside')
        self.rect = Rect(384, 0, 96, 128)
        self.poly = Rect2Polygon(self.rect)
        self.add_state(OPEN, 'rooms/outside/outside2lobby.png')
        self.add_state(CLOSED)
        self.state = CLOSED
    def on_open(self, game):
        super(OutsideToLobby, self).on_open(game)
        game.rooms['car'].add_patch('rooms/car/open.png', Rect(160, 64, 48, 48))
    def on_close(self, game):
        super(OutsideToLobby, self).on_close(game)
        game.rooms['car'].add_patch('rooms/car/closed.png', Rect(160, 64, 48, 48))
 
class Outside(Room):
    def __init__(self):
        super(Outside, self).__init__('outside')
        self.set_image('rooms/outside/outside.png')
        self.add_item(Mailbox())
        self.add_item(Window())
        self.add_item(Mummy())
        self.add_item(BirdBath())

