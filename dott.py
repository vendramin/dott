__version__ = "$Revision: 5 $"
# $Source$

import pygame
import sys
import actor
import item
import room
import static_item
import door

from game import Game
from pygame.locals import *

__metaclass__ = type

if __name__ == '__main__':

    print sys.argv
    if len(sys.argv) == 1:
        start = room.lobby
    else:
        start = eval(sys.argv[1])

    game = Game((640, 400))
    game.init(actor.bernard, room=start)
    actor.bernard.take_item(item.crowbar)
    game.run()
