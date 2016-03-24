import pygame
import sys

from room import Room
from item import Door, Item, StaticItem
from mouse import Mouse

from pygame.locals import *
from config import *

from lobby import *
from outside import *
from basement import *
from study import *
from playroom import *
from secondfloor import *
from roof import *
from kitchen import *
from attic import *
from suite import *
from sad import *
from green import *
from hallway import *
from warehouse import *
from laundry import *
from edd import *
from edna import *
from car import *
from water import *
from items import *

class Game(object):
    def __init__(self,  size=None):
        pygame.init()
        if not size:
            size = SCREEN_SIZE
            
        self.screen = pygame.display.set_mode(size, HWSURFACE|DOUBLEBUF)
        pygame.display.set_caption("DoTT")
   
        self.font = pygame.font.Font('gui/font.ttf', 14) 
        
        self.room = None
        self.actors = {}
        self.player = None
        self.rooms = {}
        self.verb = WALK
        self.mouse = Mouse('gui/cursor.png')
        self.fullscreen = False
        self.message = ''
        self.gui = pygame.image.load('gui/gui.png').convert_alpha()

        # para la gui
        self.j = 0
    
    def add_room(self, room):
        """ Add a room to the list of rooms of the game. All rooms must belong to this dictionary! """
        self.rooms[room.name] = room
        
    def change_room(self, name):
        self.room = self.rooms[name]

    def run(self, screen=None):
        self.quit = 0
        if screen != None: self.screen = screen
        while not self.quit:
            self.loop()

    def loop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                self.on_mouse_motion()
            elif event.type == MOUSEBUTTONDOWN:
                self.on_mouse_button_down()
            elif event.type == MOUSEBUTTONUP:
                pass
            elif event.type == KEYUP:
                pass
            elif event.type == KEYDOWN:
                if event.key == K_i:
                    print "Inventory:"
                    print self.player.inventory
                if event.key == K_f:
                    pass
                #self.toggle_fullscreen()
                if event.key == K_c:
                    self.verb = CLOSE
                if event.key == K_o:
                    self.verb = OPEN
                if event.key == K_w:
                    self.verb = WALK
                if event.key == K_l:
                    self.verb = LOOK
                if event.key == K_p:
                    self.verb = PICK_UP
                if event.key == K_s:
                    self.verb = PUSH
                if event.key == K_j:
                    if self.j<len(self.player.inventory)-6:
                        self.j = self.j+3
                if event.key == K_k:
                    if self.j>0:
                        self.j = self.j-3
                if event.key == K_d:
                    x, y = self.mouse.get_pos()
                    print "mouse:",  x,  y
                    print "Active room information:"
                    print self.room.rectangles
                    self.room.info()
                    print "Main actor information:"
                    self.player.info()
                else:
                    self.room.on_event(event)

        # FIXME: hay que usar update de la lista de rects que se modificaron: mouse, texto, sprites.
        self.draw()
        x, y = self.mouse.get_pos()
        self.screen.blit(self.mouse.image,
                (x-self.mouse.image.get_width()/2,
                    y-self.mouse.image.get_height()/2))
        pygame.display.update()

    def on_mouse_motion(self):
        x, y = self.mouse.get_pos()
        x -= self.room.camera.x
        y -= self.room.camera.y
        print x, y
        for i in self.room.areas:
            if i.poly.collidepoint(x,y):
                self.message = self.verb + ' ' + i.description
                break
            else:
                self.message = self.verb
               
    def on_mouse_button_down(self):
        x, y = self.mouse.get_pos()
       
        # select the verb
        verbs = {GIVE: Rect(0, 302, 77, 28), PICK_UP: Rect(81, 302, 124, 28), 
                USE: Rect(209, 302, 76, 28), OPEN: Rect(0, 334, 77, 28), 
                LOOK_AT: Rect(81, 334, 124, 28), PUSH: Rect(209, 334, 76, 28),
                CLOSE: Rect(0, 366, 77, 28), TALK_TO: Rect(81, 366, 124, 28), 
                PULL: Rect(209, 366, 76, 28)} 

        for v, r in verbs.items():
            if r.collidepoint(x, y):
                self.verb = v
                return 

        # select an item of the inventory
        rects = [Rect(320, 299, 80, 48), Rect(400, 299, 80, 48), Rect(480, 299, 80, 48), 
                Rect(320, 348, 80, 48), Rect(400, 348, 80, 48), Rect(480, 348, 80, 48)] 

        for r in rects:
            if r.collidepoint(x, y):
                if self.j + rects.index(r) < len(self.player.inventory):
                    print rects.index(r) 
                    print self.player.inventory[self.j + rects.index(r)]

        x -= self.room.camera.x
        y -= self.room.camera.y
     
        for i in self.room.areas:
            if i.poly.collidepoint(x, y):
                if self.verb == WALK:
                    i.on_walk(self)
                    break
                elif self.verb == OPEN:
                    i.on_open(self)
                    break
                elif self.verb == CLOSE:
                    i.on_close(self)
                    break
                elif self.verb == PICK_UP:
                    i.on_pickup(self)
                    break
                elif self.verb == PUSH:
                    i.on_push(self)
                    
        self.verb = WALK
                
    def draw(self):
        """ Draw the entire scene. """
        self.screen.blit(self.room.image, (self.room.camera.x, self.room.camera.y))
        self.screen.fill((0, 0, 0), Rect(0, 283, 640, 112))
        self.screen.blit(self.gui, (0, 300))
        self.screen.blit(self.font.render(self.message,  True, (255, 255, 255)), ((640-len(self.message))/2, 280))
        
        self.draw_gui()
        self.room.draw(self)
   
    def draw_gui(self):
        j = 0
        p = [(320, 299), (400, 299), (480, 299), (320, 348), (400, 348), (480, 348)] 
        for name in self.player.inventory[self.j:]:
            self.screen.blit(self.items[name].image, p[j])
            if j == 5:
                break
            else:
                j = j+1

    def load_items(self):
        self.items = {
                'textbook': Textbook(),
                'help-wanted': HelpWanted(),
                'dime': Dime(),
                'flier': Flier(),
                'funnel': Funnel(),
                'keys': Keys(),
                'booboo-b-gone': BoobooBGone(),
                'bankbook': Bankbook(),
                'coffee': Coffee(),
                'decaf-coffee': DecafCoffee(),
                'fork': Fork(),
                'ink': Ink() }

    def load_doors(self):
        self.doors = {
                'lobby2study': LobbyToStudy(),
                'lobby2basement': LobbyToBasement(),
                'lobby2outside': LobbyToOutside(),
                'lobby2playroom': LobbyToPlayroom(),
                'lobby2secondfloor': LobbyToSecondfloor(),
                'study2lobby': StudyToLobby(),
                'basement2lobby': BasementToLobby(),
                'outside2lobby': OutsideToLobby(),
                'outside2car': OutsideToCar(),
                'car2outside': CarToOutside(),
                'car2water': CarToWater(),
                'water2car': WaterToCar(),
                'playroom2lobby': PlayroomToLobby(),
                'playroom2kitchen': PlayroomToKitchen(),
                'playroom2roof': PlayroomToRoof(),
                'kitchen2laundry': KitchenToLaundry(),
                'kitchen2playroom': KitchenToPlayroom(),
                'laundry2kitchen': LaundryToKitchen(),
                'secondfloor2suite': SecondfloorToSuite(),
                'secondfloor2sad': SecondfloorToSad(),
                'secondfloor2green': SecondfloorToGreen(),
                'secondfloor2lobby': SecondfloorToLobby(),
                'secondfloor2hallway': SecondfloorToHallway(),
                'suite2secondfloor': SuiteToSecondfloor(),
                'sad2secondfloor': SadToSecondfloor(),
                'green2secondfloor': GreenToSecondfloor(),
                'hallway2secondfloor': HallwayToSecondfloor(),
                'hallway2edd': HallwayToEdd(),
                'hallway2edna': HallwayToEdna(),
                'hallway2warehouse': HallwayToWarehouse(),
                'edd2hallway': EddToHallway(),
                'edna2hallway': EdnaToHallway(),
                'warehouse2hallway': WarehouseToHallway(),
                'warehouse2attic': WarehouseToAttic(),
                'attic2warehouse': AtticToWarehouse(),
                'attic2roof': AtticToRoof(),
                'roof2attic': RoofToAttic(),
                'roof2playroom': RoofToPlayroom() }

    def load_rooms(self):
        self.rooms = {
                'lobby': Lobby(),
                'outside': Outside(),
                'basement': Basement(),
                'study': Study(),
                'playroom': Playroom(),
                'secondfloor': Secondfloor(),
                'roof': Roof(),
                'kitchen': Kitchen(),
                'attic': Attic(),
                'suite': Suite(),
                'sad': Sad(),
                'green': Green(),
                'hallway': Hallway(),
                'warehouse': Warehouse(),
                'laundry': Laundry(),
                'edd': Edd(),
                'edna': Edna(),
                'car': Car(),
                'water': Water() }

    def init(self, room_name):
        """ Create the world """ 
        self.load_items()
        self.load_doors()
        self.load_rooms()

        # Add doors in rooms 
        for d in self.doors.values():
            self.rooms[d.room].add_door(d)

        # Add items in rooms
        for i in self.items.values():
            if not i.room == None:
                self.rooms[i.room].add_item(i)

        # Set the room where to start
        self.room = self.rooms[room_name]

    def toggle_fullscreen(self):
        if self.fullscreen:
            self.screen = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE|DOUBLEBUF)
        else:
            self.screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN|HWSURFACE|DOUBLEBUF)
        self.fullscreen = not self.fullscreen

