import os
import pygame
import room
import item
import door
import gui

from scumm import Actor, Player

path = os.path.join('data', 'actors')

def load_image(filename, name=None):
    if not name == None:
        return pygame.image.load(os.path.join(path, name, filename)).convert_alpha()
    else:
        return pygame.image.load(os.path.join(path, filename)).convert_alpha()

def load_images(*filenames, **kwargs):
    if 'name' in kwargs:
        name = kwargs['name']
        return [pygame.image.load(os.path.join(path, name, f)).convert_alpha() for f in filenames]
    else:
        return [pygame.image.load(f).convert_alpha() for f in filenames]

def init():
    bernard.init()
    conventioner.init()
    thief.init()

__metaclass__ = type

class Bernard(Player):
    def __init__(self):
        super(Bernard, self).__init__()
    def init(self):
        self.gui = gui.GUI(self.items)
        self.take_item(item.textbook)
    def take_item(self, item):
        super(Bernard, self).take_item(item)
        self.gui.items.add(item)
        self.gui.update()

class Conventioner(Actor):
    def __init__(self):
        super(Conventioner, self).__init__()
    def init(self):
        self.description = 'sleeping conventioner'
        self.sleeping_in_bed()
    def update(self):
        self.pause = self.pause - 1
        if self.pause <= 0:
            self.pause = self.delay
            self.frame = (self.frame + 1) % len(self.images)
            self.image = self.images[self.frame]
            self.rect = self.image.get_rect()
            self.rect.topleft = self.x, self.y
    def sleeping_in_bed(self):
        self.images = load_images('01.png', '02.png', '03.png',
                '04.png', '05.png', '06.png', '07.png', '08.png',
                '09.png', '10.png', '11.png', name='conventioner')
        self.x = 320
        self.y = 85
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.frame = 0
        self.dirty = 2
        self.delay = 10
        self.pause = self.delay
    def sleeping_on_the_floor(self):
        self.images = load_images('12.png', '13.png', name='conventioner')
        self.x = 311
        self.y = 188
        self.delay = 50
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
    
class Thief(Actor):

    files = ['%02d.png' % k for k in range(1, 40)] 
    frames = {1: (21, 22)}#, 0, 11)}

    pos = {19: (216, 89), 21: (214, 93), 22: (216, 89)} 

    def __init__(self):
        super(Thief, self).__init__()

    def init(self):
        #self.images = [load_image(f, name='thief') for f in Thief().files]
        self.images = [pygame.image.load(os.path.join(path, 'thief', f)).convert() for f in Thief().files]
        for image in self.images: 
            image.set_colorkey((148, 149, 148))
        self.frames = Thief().frames[1]
        self.frame = 0
        self.dirty = 2
        self.delay = 10
        self.pause = self.delay
        self.description = 'man in sky mask'
        self.frame = 0
        self.image = self.images[19]
        self.rect = self.image.get_rect()
        self.rect.x = 217
        self.rect.y = 90
 
    def update(self):
        self.pause = self.pause - 1
        if self.pause <= 0:
            self.pause = self.delay
            self.frame = (self.frame + 1) % len(self.frames)
            self.image = self.images[self.frames[self.frame]]
            self.rect.topleft = Thief().pos[self.frames[self.frame]]

    def use_with(self, obj=None):
        if obj == item.keys:
            obj.kill()
            self.game.player.drop_item(obj)
            self.game.player.take_item(item.crowbar)
            self.game.player.gui.move_to_bottom()
            self.game.update_inventory()

    def on_give(self, obj=None):
        self.on_use(obj)
 
bernard = Bernard()
conventioner = Conventioner()
thief = Thief()
