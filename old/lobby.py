import pygame
import sys

import scupy

from scupy.room import Room
from scupy.item import Item, Door,  StaticItem
from scupy.actor import Actor
from scupy.geometry import Point2D, Point3D, Polygon, Rect2Polygon

from pygame.locals import *
from scupy.config import *

__metaclass__ = type

class Rack(StaticItem):
    def __init__(self):
        super(Rack, self).__init__('rack')
        self.poly = Polygon((85, 301), (269, 301), (180, 271), (51, 241), (37, 246))
        self.description = 'rack for fliers'
        self.z = 0

class Flier(Item):
    def __init__(self):
        super(Flier, self).__init__('flier')
        self.rect = Rect(128, 224, 64, 48)
        self.poly = Rect2Polygon(self.rect)
        self.description = 'flier'
        self.room = 'lobby'
        self.z = 1
        self.set_image('items/flier.png') 

    def on_pickup(self, game):
        """ Pick up this flier """
        super(Flier, self).on_pickup(game)
        game.rooms['lobby'].add_patch('rooms/lobby/noflier.png', self.rect)
 
class Bell(StaticItem):
    def __init__(self):
        super(Bell, self).__init__('bell')
        self.rect = Rect(430, 176, 15, 20)
        self.poly = Rect2Polygon(Rect(413, 160, 27, 23))
        self.description = 'service bell'

class Chuck(StaticItem):
     def __init__(self):
        super(Chuck, self).__init__('chuck')
        self.rect = Rect(203, 115, 50, 75)
        self.poly = Rect2Polygon(self.rect)
        self.description = 'Chuck the Plant'
        self.room = 'lobby'

class HelpWanted(Item):
    def __init__(self):
        super(HelpWanted, self).__init__('help-wanted')
        self.rect = Rect(16, 144, 80, 64)
        self.poly = Rect2Polygon(self.rect)
        self.set_image('items/help-wanted.png')
        self.description = 'help-wanted sign'
        self.room = 'lobby'
    
    def on_pickup(self, game):
        """ Pick up this sign """
        super(HelpWanted, self).on_pickup(game)
        # Modify the rooms from where this sign is visible
        game.rooms['lobby'].add_patch('rooms/lobby/nosign.png', Rect(16, 144, 80, 64))
        game.rooms['outside'].add_patch('rooms/outside/nosign.png', Rect(640, 32, 96, 64))
        game.rooms['car'].add_patch('rooms/car/window.png', Rect(256, 64, 48, 48))
        # FIXME: hay que arreglar lo que se ve cuando se recoge el
        # cartelito
        
class Dime(Item):
    def __init__(self):
        super(Dime, self).__init__('dime')
        self.rect = Rect(560, 155, 15, 15)
        self.poly = Rect2Polygon(self.rect)
        self.z = 1
        self.description = 'dime'
        self.room = 'lobby'
        self.set_image('items/dime.png')

    def on_pickup(self, game):
        """ Pick up this sign """
        super(Dime, self).on_pickup(game)
        # Modify the rooms from where this phone is visible
        game.rooms['lobby'].add_patch('rooms/lobby/phone.png', Rect(528, 96, 64, 96))
    
class PayPhone(StaticItem):
    def __init__(self):
        super(PayPhone, self).__init__('payphone')
        self.rect = Rect(528, 96, 64, 96)
        self.poly = Rect2Polygon(self.rect)
        self.description = 'pay phone'
        self.z = 0

class LobbyToBasement(Door):
    def __init__(self):
        super(LobbyToBasement, self).__init__('lobby2basement',  'lobby', 'basement2lobby')
        self.rect = Rect(592, 112, 144, 80)
        self.poly = Rect2Polygon(self.rect)
        self.add_state(OPEN, 'rooms/lobby/lobby2basement.png')
        self.add_state(CLOSED)
        self.state=CLOSED
        self.description = 'grandfather clock' # dark passage
        
class LobbyToOutside(Door):
    def __init__(self):
        super(LobbyToOutside, self).__init__('lobby2outside',  'lobby', 'outside2lobby')
        self.poly = Rect(95, 87, 157-95, 216-87)
        self.rect = Rect(96, 64, 80, 176)
        self.add_state(OPEN, 'rooms/lobby/lobby2outside.png')
        self.add_state(CLOSED)
        self.state=CLOSED
    def on_open(self, game):
        super(LobbyToOutside, self).on_open(game)
        game.rooms['car'].add_patch('rooms/car/open.png', Rect(160, 64, 48, 48))
    def on_close(self, game):
        super(LobbyToOutside, self).on_close(game)
        game.rooms['car'].add_patch('rooms/car/closed.png', Rect(160, 64, 48, 48))
        
class LobbyToPlayroom(Door):
    def __init__(self):
        super(LobbyToPlayroom, self).__init__('lobby2playroom',  'lobby' ,'playroom2lobby')
        self.poly = Polygon((275, 216), (295, 124), (374, 115), (416, 123), (434, 214))
        self.rect = Rect(240, 80, 160, 128)
        self.add_state(OPEN, 'rooms/lobby/lobby2playroom.png')
        self.add_state(CLOSED)
        self.state=CLOSED
 
class LobbyToStudy(Door):
    def __init__(self):
        super(LobbyToStudy, self).__init__('lobby2study', 'lobby' ,  'study2lobby')
        self.poly = Polygon((480,  113), (531,  81),  (552,  128),  (563,  175),  (560,  207),  (552,  218),  (520,  214))
        self.rect = Rect(448, 64, 80, 144)
        self.add_state(OPEN, 'rooms/lobby/lobby2study.png')
        self.add_state(CLOSED)
        self.state=CLOSED

class LobbyToSecondfloor(Door):
    def __init__(self): 
        super(LobbyToSecondfloor, self).__init__('lobby2secondfloor',  'lobby' ,'secondfloor2lobby')
        self.rect = Rect(770, 0, 170, 300)
        self.poly = Rect2Polygon(self.rect)
        self.add_state(OPEN)
        self.state=OPEN
        self.is_open = True
        self.description = 'stairs'
        
    def on_open(self, game):
        pass

    def on_close(self, game):
        pass

class Lobby(Room):    
    def __init__(self):
        super(Lobby, self).__init__('lobby')
        self.set_image('rooms/lobby/lobby.png')
        self.add_item(PayPhone())
        self.add_item(Chuck())
        self.add_item(Bell())
        self.add_item(Rack())
