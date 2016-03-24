import pygame
import sys
import scumm
import gui
import actor
import item
import room as r
import door 
import static_item 

from pygame.locals import *
from config import *

# layers
VERBS = 11
ITEMS = 12

class Mouse(pygame.sprite.DirtySprite):
    def __init__(self, filename):
        super(Mouse, self).__init__()
        pygame.mouse.set_visible(False)
        self.set_image(filename)
        self.default = self.image
        self.rect = self.image.get_rect()
        self.dirty = 2 

    def set_image(self, filename=None):
        if filename == None:
            self.image = self.default
        else:
            self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()

    def get_pos(self):
        return pygame.mouse.get_pos()

    def set_pos(self, position):
        pygame.mouse.set_pos(position)

    def update(self):
        self.rect.center = self.get_pos()

class Text(pygame.sprite.DirtySprite):

    def __init__(self, filename=None, size=20):
        super(Text, self).__init__()
        self.font = pygame.font.Font(filename, size)
        self.msg = None
        self.color = Color('white')
        self.antialias = True
        self.update()
        self.rect = self.image.get_rect()
        self.dirty = 2

    def set_color(self, color):
        self.color = color

    def update(self):
        if not self.msg == None: 
            self.rect = self.image.get_rect(centerx=320)
        self.image = self.font.render(self.msg, self.antialias, self.color)

class Game(object):
    def __init__(self, size=None):
        pygame.init()
        if not size:
            size = SCREEN_SIZE
            
        self.screen = pygame.display.set_mode(size, HWSURFACE|DOUBLEBUF)
        pygame.display.set_caption("DoTT")
   
        self.font = pygame.font.Font('data/gui/font.ttf', 14) 
        self.text = Text('data/gui/font.ttf')
        
        self.room = None

        self.actors = {}
        self.player = None
        self.verb = WALK
        self.object = None

        self.mouse = Mouse('data/gui/cursor.png')
        self.fullscreen = False
        self.message = ''
        self.gui = pygame.image.load('data/gui/gui.png').convert_alpha()

        # para la gui
        self.j = 0
    
    def run(self, screen=None):
        self.quit = 0
        clock = pygame.time.Clock()
        while not self.quit:
            clock.tick(60)
            self.loop()

    def loop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                pass
            #self.on_mouse_motion()
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
                if event.key == K_s:
                    print self.sprites
                if event.key == K_DOWN:
                    self.room.x = self.room.x
                    self.room.y = self.room.y-20
                if event.key == K_UP:
                    self.room.x = self.room.x
                    self.room.y = self.room.y+20
                if event.key == K_RIGHT:
                    # FIXME: hacer un update de la GUI
                    self.room.x = self.room.x-20
                    self.room.update_sprites()
                    self.screen.blit(self.room.image, (self.room.x, 0))
                    self.background = self.screen.copy()
                    pygame.display.flip()
                if event.key == K_LEFT:
                    # FIXME: hacer un update de la GUI
                    self.room.x = self.room.x+20
                    self.room.update_sprites()
                    self.screen.blit(self.room.image, (self.room.x, 0))
                    self.background = self.screen.copy()
                    pygame.display.flip()
                if event.key == K_t:
                    self.text.visible = (self.text.visible+1)%2
                if event.key == K_g:
                    self.verb = GIVE
                if event.key == K_c:
                    self.verb = CLOSE
                if event.key == K_o:
                    self.verb = OPEN
                if event.key == K_w:
                    self.verb = WALK
                if event.key == K_l:
                    self.verb = LOOK_AT
                if event.key == K_p:
                    self.verb = PICK_UP
                if event.key == K_u:
                    self.verb = USE
                if event.key == K_s:
                    self.verb = PUSH
                if event.key == K_j:
                    self.player.gui.move_down()
                    self.update_inventory()
                if event.key == K_k:
                    self.player.gui.move_up()
                    self.update_inventory()
                if event.key == K_0:
                    self.player.gui.move_to_top()
                    self.update_inventory()

        self.on_mouse_motion()
        self.text.update()

        self.sprites.clear(self.screen, self.background)
        self.sprites.update()
        pygame.display.update(self.sprites.draw(self.screen))

    def on_mouse_motion(self):

        x, y = self.mouse.get_pos()

        # mouse inside the room
        if pygame.Rect(0, 0, 640, 295).collidepoint(x, y):
            lst = self.room.sprites.get_sprites_at((x, y))
            if not lst == []:
                self.text.msg = str(self.verb) + ' ' + lst[-1].description + ' at ' + str((x, y))
                self.object = lst[-1]
            else:
                self.object = None
                if self.verb == None:
                    self.text.msg = str(self.mouse.get_pos())
                else:
                    self.text.msg = str(self.verb)+ ' at ' + str((x, y))

        # mouse inside the inventory
        elif pygame.Rect(322, 300, 278, 100).collidepoint(x, y):
            lst = self.player.gui.items.get_sprites_at((x, y))
            if not lst == []:
                self.text.msg = 'use ' + lst[-1].description
     
    def on_mouse_button_down(self):
        """ Acts when the mouse button was pressed. """
        x, y = self.mouse.get_pos()

        # clicked inside the room
        if pygame.Rect(0, 0, 640, 295).collidepoint(x, y):
            if not self.object == None:
                if self.verb == GIVE:
                    self.object.on_give()
                if self.verb == WALK:
                    self.object.on_walk()
                elif self.verb == OPEN:
                    self.object.on_open()
                elif self.verb == CLOSE:
                    self.object.on_close()
                elif self.verb == PICK_UP:
                    self.object.on_pickup()
                elif self.verb == PULL:
                    self.object.on_pull()
                elif self.verb == PUSH:
                    self.object.on_push()
                elif self.verb == USE:
                    self.object.on_use()
                else:
                    self.object.use_with(self.verb)

            # walk to is the default verb 
            # self.mouse.image = self.mouse.default
            self.verb = WALK

        # clicked on some verb
        elif pygame.Rect(0, 300, 295, 100).collidepoint(x, y):
            lst_verbs = self.player.gui.verbs.get_sprites_at((x, y))
            if not lst_verbs == []:
                self.verb = lst_verbs[0].verb
                self.text.msg = self.verb + ' at ' + str((x, y))

        # clicked on the inventory
        elif pygame.Rect(212, 300, 388, 100).collidepoint(x, y):
            self.old = self.verb
            lst_items = self.player.gui.items.get_sprites_at((x, y))
            if not lst_items == []:
                if isinstance(lst_items[0], gui.Up):
                    self.player.gui.move_up()
                    self.update_inventory()
                elif isinstance(lst_items[0], gui.Down):
                    self.player.gui.move_down()
                    self.update_inventory()
                else:
                    self.verb = lst_items[0].use_with()
                    if not self.verb == None:
                        if self.verb == self.old:
                            #self.mouse.image = self.mouse.default
                            self.verb = WALK
                        else:
                            if not isinstance(self.old, scumm.Item):
                                pass
                                #self.mouse.image = self.verb.image
                            else:
                                self.old.use_with(self.verb)
                                self.verb = WALK



    def update_inventory(self):
        """ Update the inventory GUI. """
        self.sprites.remove_sprites_of_layer(ITEMS)
        self.sprites.add(self.player.gui.items.sprites(), layer=ITEMS)

    def init(self, player, room=None):
        """ Initialize the game and its components. """

        self.player = player

        # create the empty list of sprites
        self.sprites = pygame.sprite.LayeredDirty()
        self.sprites.empty()

        scumm.init(self)

        item.init()
        actor.init()
        r.init()
        door.init()
        static_item.init()

        if room == None:
            self.change_room(room.lobby)
        else:
            self.change_room(room)

    def change_room(self, room):

        self.room = room
        self.screen.blit(room.image, (room.x, room.y))
        self.screen.blit(self.gui, (2, 303))
        
        # backup for the background
        self.background = self.screen.copy() 
        pygame.display.flip()

        # make a copy of the ordered list of the sprites
        self.sprites.empty()
        # remove all sprites from the active window
        self.sprites = self.room.sprites.copy()

        # add sprites for verbs and items
        self.sprites.add(self.player.gui.verbs.sprites(), layer=VERBS)
        self.sprites.add(self.player.gui.items.sprites(), layer=ITEMS)

        # add text and mouse to the copy
        self.sprites.add(self.text, layer=self.sprites.get_top_layer()+1)
        self.sprites.add(self.mouse, layer=self.sprites.get_top_layer()+1)

