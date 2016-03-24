import pygame

from room import Room
from geometry import Point2D, Point3D, Polygon
from config import *

__metaclass__ = type

class Item(object):
    #     d = {}
    def __init__(self, name):
        self.name = name 
        self.description = 'unkown object'
        self.is_visible = True
        self.is_hidden = False
        self.position = None
        self.image = None
        self.room = None
        self.rect = None
        self.z = 0
        self.states = {}
        self.state = None
        
    def modify_state(self, state, filename=None):
        if filename : 
            self.states[state] = pygame.image.load(filename).convert_alpha()
        else:
            self.states[state] = None

    def add_state(self, state, filename=None):
        if not state in self.states.keys():
            if filename : 
                self.states[state] = pygame.image.load(filename).convert_alpha()
            else:
                self.states[state] = None

    def set_state(selfs,  state):
        self.state = state

    def set_rectangle(self, rectangle):
        self.rectangle = rectangle

    def set_image(self, filename):
        self.image = pygame.image.load(filename).convert_alpha()

#    def draw(self, screen, position=None):
#        if position is not None:
#            position = (self.rect.x, self.rect.y)
#        if self.states[self.state] is not None:
#            screen.blit(self.states[self.state], position)

    def draw(self, game):
        ### guardar el rectangulo que se dibuja!
        if self.state is not None:
            if self.states[self.state] is not None:
                game.screen.blit(self.states[self.state], (self.rect.x+game.room.camera.x,  self.rect.y+game.room.camera.y))

    def scale(self, value):
        self.image = pygame.transform.rotozoom(self.image, 0, value)

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)

    def on_walk(self,  game):
        pass

    def on_open(self,  game):
        pass

    def on_close(self,  game):
        pass

    def on_event(self, event):
        pass

    def on_pickup(self, game):
        if not game.player.has_item(self.name):
            game.player.take_item(self.name)
            game.room.areas.remove(self)
            self.room = None

            # show only the last items
            game.j = 0
            while game.j <  len(game.player.inventory)-6:
                game.j = game.j + 3

class StaticItem(Item):
    def on_pickup(self,  game):
        pass

class Door(StaticItem):
    """ Class for doors. """
    def __init__(self, name, room, to):
        """ 
        Creates the door <name> connected to the door named <to>. 
        
        Parameters:
            name - this is the name of the door
            room - the room where this room is located
            to - name of the other side of this same door

        """
        
        super(Door, self).__init__(name)
#        self.is_open = False
        self.room = room
        self.to = to
        self.is_locked = False
        self.description = 'door'
#        self.add_state(OPEN)
#        self.add_state(CLOSED)
#        self.state = CLOSED

    def on_open(self, game):
        """ Open the door. The door connected to this one is also open. """
        # FIXME: estados? no existen...
#        if not self.is_open:
        if self.state == CLOSED: 
#            self.is_open = True
            self.state = OPEN
            game.doors[self.to].state = self.state
#            game.doors[self.to].iss_open = self.is_open
        
    def on_close(self, game):
        """ Close the door. The door connected to this one is also closed. """
        if self.state == OPEN:
#        if self.is_open:
#            self.is_open = False
            self.state = CLOSED
            game.doors[self.to].state = self.state
#            game.doors[self.to].is_open = self.is_open
        
    def on_walk(self, game):
        if self.state == OPEN:
            game.room = game.rooms[game.doors[self.to].room]
            

