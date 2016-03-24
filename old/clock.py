import pygame
import os
import sys

from pygame.locals import *

class LobbyToPlayroom(pygame.sprite.DirtySprite):
    def __init__(self):
        super(LobbyToPlayroom, self).__init__()
        #self.source_rect = Rect(240, 80, 160, 128)
        self.image = pygame.image.load('open.png').convert()
        self.rect = self.image.get_rect()  
        self.rect.x = 240
        self.rect.y = 80
        self.name = 'door'
#        self.visible = 1
#        self.dirty = 2
    def on_open(self, group):
        self.visible = 1
        self.dirty = 2
    def on_close(self, group):
        self.visible = 0
        self.dirty = 2
#    def update(self):
#        pass

class Button(pygame.sprite.DirtySprite):
    def __init__(self):
        super(Button, self).__init__()
        self.images = [pygame.image.load('open1.png'),
                pygame.image.load('open2.png')]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 301
        self.frame = 0
        self.dirty = 2
    def change_state(self, frame):
        self.frame = frame 
        self.image = self.images[self.frame]
    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.change_state(1)
        else:
            self.change_state(0)

class OldClock(pygame.sprite.DirtySprite):
    def __init__(self):
        super(OldClock, self).__init__()
        self.delay = 60
        self.pause = self.delay
        self.frame = 0
        self.images = [pygame.image.load('1.png').convert_alpha(),
                pygame.image.load('2.png').convert_alpha(),
                pygame.image.load('3.png').convert_alpha(),
                pygame.image.load('2.png').convert_alpha()]
        self.image = self.images[0]
        self.rect = self.image.get_rect()  
        self.rect.x = 640
        self.rect.y = 112
        self.name = 'old clock'
        self.dirty = 2
 
    def update(self):
        self.pause = self.pause - 1
        if self.pause <= 0:
            self.pause = self.delay
            self.frame = (self.frame + 1) % 4
            self.image = self.images[self.frame]

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

class Mouse(pygame.sprite.DirtySprite):
    def __init__(self, filename):
        super(Mouse, self).__init__()
        pygame.mouse.set_visible(False)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.dirty = 2 

    def get_pos(self):
        return pygame.mouse.get_pos()

    def set_pos(self, position):
        pygame.mouse.set_pos(position)

    def update(self):
        self.rect.center = self.get_pos()

if __name__ == '__main__': 
    quit = False
    x = 0
    y = 0

    pygame.init()
            
    screen = pygame.display.set_mode((640, 400), HWSURFACE|DOUBLEBUF)
    pygame.display.set_caption("Mouse")
   
    mouse = Mouse('mouse.png')
    text = Text('font.ttf')

    background = pygame.image.load('background.png')
    gui = pygame.image.load('gui.png')

    screen.blit(background, (0, 0))
    screen.blit(gui, (0, 300))
    background = screen.copy()
    pygame.display.flip()

    old_clock = OldClock()
    button = Button()
    lobby2playroom = LobbyToPlayroom()

    areas = pygame.sprite.LayeredDirty(lobby2playroom, old_clock)
    sprites = pygame.sprite.LayeredDirty(lobby2playroom, button, old_clock, text, mouse)

    d=0
    clock = pygame.time.Clock()
    while not quit:

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                a = pygame.sprite.spritecollideany(mouse, areas)
                if a:
                    #if pygame.sprite.collide_rect(mouse, old_clock):
                    text.msg = str(mouse.get_pos()) + a.name #' the old clock'
                else:
                    text.msg = str(mouse.get_pos())
            elif event.type == MOUSEBUTTONDOWN:
                pass
            elif event.type == MOUSEBUTTONUP:
                pass
            elif event.type == KEYDOWN:
                if event.key == K_o:
                    a = pygame.sprite.spritecollideany(mouse, areas)
                    if a:
                        print 'open'
                        a.on_open(sprites)
                        lobby2playroom.visible = 0
                        lobby2playroom.dirty = 2
                if event.key == K_c:
                    a = pygame.sprite.spritecollideany(mouse, areas)
                    if a:
                        print 'close'
                #        a.on_close(sprites)
                        lobby2playroom.visible = (lobby2playroom.visible+1)%2
                        lobby2playroom.dirty = 2
                if event.key == K_t:
                    text.visible = (text.visible+1)%2
                    text.dirty = 2
                if event.key == K_d:
                    screen.blit(pygame.image.load('background.png'), (x, 0))
                    screen.blit(gui, (0, 300))
                    if d == 0:
                        pass
                        screen.blit(pygame.image.load('open.png'), (x+240, 80))
                        d = 1
                    else:
                        d = 0
                    background = screen.copy()
#                    pygame.display.update()
                    pygame.display.update(Rect(x+240, 80, 160, 128))

                if event.key == K_RIGHT:
                    x = x - 20
                    old_clock.rect.x = old_clock.rect.x - 20
                    screen.blit(pygame.image.load('background.png'), (x, 0))
                    background = screen.copy()
                    pygame.display.update()
                if event.key == K_LEFT:
                    x = x + 20
                    old_clock.rect.x = old_clock.rect.x + 20
                    screen.blit(pygame.image.load('background.png'), (x, 0))
                    background = screen.copy()
                    pygame.display.update()

       
        text.update()
  
        sprites.clear(screen, background)

        areas.update()
        sprites.update()
  
        pygame.display.update(sprites.draw(screen))


