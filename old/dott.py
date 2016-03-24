__version__ = "$Revision: 5 $"
# $Source$

import pygame
import sys

import scupy

from scupy.game import Game
from scupy.actor import Actor
from scupy.item import Item

from pygame.locals import *

__metaclass__ = type

class Bernard(Actor):
     def __init__(self):
        super(Bernard, self).__init__("Bernard")
        self.take_item('textbook')

if __name__ == '__main__':

    print sys.argv
    if len(sys.argv) == 1:
        start = 'lobby'
    else:
        start = sys.argv[1]

    game = Game((640, 400))
    game.init(start)
    game.player = Bernard()
    game.run()
