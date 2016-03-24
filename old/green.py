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

"""
"""

class OnOffButton(StaticItem):
    def __init__(self):
        super(OnOffButton, self).__init__('on/off')
        self.description = 'on/off button'

class Speaker(StaticItem):
    def __init__(self):
        super(Speaker, self).__init__('speaker')
        self.rect = Rect(304, 160, 144, 96)
        self.poly = Rect2Polygon(self.rect)
        self.description = 'speaker'
        self.add_state(UP)
        self.add_state(DOWN, 'rooms/green/speaker.png')
        self.state = UP
    
    def on_push(self, game):
        """ Push the speaker """
        if self.state == UP:
            game.rooms['green'].add_patch('rooms/green/speaker.png', Rect(304, 160, 144, 96))

class GreenToSecondfloor(Door):
    def __init__(self):
        super(GreenToSecondfloor, self).__init__('green2secondfloor',
                'green',  'secondfloor2green')
        self.rect = Rect(144, 0, 160, 160)
        self.poly = Rect2Polygon(self.rect) 
        self.add_state(OPEN, 'rooms/green/green2secondfloor.png')
        self.add_state(CLOSED)
        self.state=OPEN
  
class Green(Room):    
    def __init__(self):
        super(Green, self).__init__('green')
        self.set_image('rooms/green/green.png')
        self.add_item(Speaker())


