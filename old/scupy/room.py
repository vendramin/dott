import pygame

from geometry import Point2D, Point3D, Polygon
from config import *
from pygame.locals import *

__metaclass__ = type

class Room(object):
    
    def __init__(self, name=None): 
        self.name = name
#        self.items = {}
        self.actors = {}
        self.image = None
        self.camera = Point2D(0, 0) 
        self.areas = []
#        self.items = []
        
        # patchs to apply to the room
        self.patchs = []
        
    @property
    def items(self):
        return [i for i in self.areas]

    def add_patch(self, filename, rect):
        self.patchs.append((rect, pygame.image.load(filename).convert_alpha()))

    def set_image(self, filename):
        self.image = pygame.image.load(filename).convert()
        
    def add_door(self, door):
        self.add_item(door)
    
    #def add_item(self, item):
    def add_item(self, item):
        #self.areas.append((item, item.z))
        self.areas.append(item)
        #self.areas.sort(key=lambda x:x[1], reverse=True)
        self.areas.sort(key=lambda x:x.z, reverse=True)

    def remove_item(self, item):
        #self.areas.remove((item, item.z))
        self.areas.remove(item)

    def on_event(self, event):
        if event.key == K_DOWN:
            print "Camera position ", self.camera.x, self.camera.y
            self.camera = Point2D(self.camera.x, self.camera.y-20)
        if event.key == K_UP:
            print "Camera position ", self.camera.x, self.camera.y
            self.camera = Point2D(self.camera.x, self.camera.y+20)
        if event.key == K_RIGHT:
            print "Camera position ", self.camera.x, self.camera.y
            self.camera = Point2D(self.camera.x-20, self.camera.y)
        if event.key == K_LEFT:
            print "Camera position ", self.camera.x, self.camera.y
            self.camera = Point2D(self.camera.x+20, self.camera.y)
             
    def draw(self, game):
        #for i, z in sorted(self.areas, key=lambda x:x[1], reverse=False):
        for i in sorted(self.areas, key=lambda x:x.z, reverse=False):
            if not i.is_hidden:
                i.draw(game)
         
        # Draw patchs
        for rect, img in self.patchs:
            game.screen.blit(img, (rect.x+self.camera.x, rect.y+self.camera.y))

    def info(self):
        print self.name
        print "In this room you may find..."
        print self.items.keys()


