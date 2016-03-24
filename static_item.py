import os
import pygame
import item
import room
import door
import actor

from scumm import StaticItem

path = os.path.join('data', 'static_items')

general = os.path.join('data', 'static_items')
#paths = {'computer': os.path,join(general, 'computer')}

"""
lavarropas viejo: 280, 0, 55, 130
"""


def load_image(filename):
    return pygame.image.load(os.path.join(path, filename)).convert_alpha()

def load_images(*filenames, **kwargs):
    if 'name' in kwargs:
        name = kwargs['name']
        return [pygame.image.load(os.path.join(path, name, f)).convert_alpha() for f in filenames]
    else:
        return [pygame.image.load(f).convert_alpha() for f in filenames]

def init():
    bed.init()
    bell.init()
    bird_bath.init()
    cabinet.init()
    candy_machine.init()
    chuck.init()
    computer.init()
    drawer.init()
    fickle_fingers.init()
    grating.init()
    mailbox.init()
    mummy.init()
    pay_phone.init()
    rack.init()
    speaker.init()
    statue.init()
    tv.init()

__metaclass__ = type

class Bed(StaticItem):
    """ The bed inside the attic. """
    def __init__(self):
        super(Bed, self).__init__()
    def init(self):
        self.rect = pygame.Rect(240, 128, 192, 112)
        self.x = 240
        self.y = 128
        self.description = 'bed'
        self.dirty = 0
        self.images = load_images('01.png','02.png', '03.png', name='bed')

    def update(self):
        if door.attic2warehouse.is_open:
            self.image = self.images[2]
            self.dirty = 1
        else:
            self.image = self.images[0]
            self.dirty = 1

class Bell(StaticItem):
    """ The bell in the lobby. """
    def __init__(self):
        super(Bell, self).__init__()
    def init(self):
        self.rect = pygame.Rect(412, 160, 20, 20)
        self.x = 412
        self.y = 160
        self.description = 'service bell'
        self.visible = False

class BirdBath(StaticItem):
    def __init__(self):
        super(BirdBath, self).__init__()
        self.x = 440
        self.y = 164
    def init(self):
        self.rect = pygame.Rect(440, 164, 100, 20)
        self.description = 'bird bath'
        self.visible = False

class Cabinet(StaticItem):
    """ Cabinet. """
    def __init__(self):
        super(Cabinet, self).__init__()
    def init(self):
        self.rect = pygame.Rect(224, 144, 96, 64)
        self.description = 'cabinet'
        self.image = load_image('cabinet.png')
        self.has_funnel = True
        self.is_open = False
        self.visible = False
    def on_open(self):
        if not self.is_open:
            self.is_open = True
            self.visible = True
            if self.has_funnel:
                item.funnel.visible = True
                for g in item.funnel.groups():
                    g.switch_layer(1, 2)
    def on_close(self):
        if self.is_open:
            self.is_open = False
            self.visible = False
            if self.has_funnel:
                item.funnel.visible = False
                for g in item.funnel.groups():
                    g.switch_layer(1, 2)
 
class CandyMachine(StaticItem):
    """ Candy machine. """
    def __init__(self):
        super(CandyMachine, self).__init__()
    def init(self):
        self.rect = pygame.Rect(364, 26, 116, 192)
        self.description = 'candy machine'
        self.has_quarters = True
        self.visible = False
    def use_with(self, obj):
        if obj == item.crowbar and self.has_quarters:
            room.secondfloor.sprites.add(item.quarters)
            self.game.sprites.add(item.quarters)
            self.has_quarters = False

class Computer(StaticItem):
    """ The computer inside the Weird Ed's room. """
    def __init__(self):
        super(Computer, self).__init__()
    def init(self):
        self.rect = pygame.Rect(215, 60, 70, 45) 
        self.description = 'computer'
        self.images = load_images('01.png', '02.png', name='computer')
        self.frame = 0
        self.image = self.images[self.frame]
        self.dirty = 2 
        self.delay = 20
        self.pause = self.delay
        self.visible = True
    def update(self):
        self.pause = self.pause - 1
        if self.pause <= 0:
            self.pause = self.delay
            self.frame = (self.frame + 1) % 2
            self.image = self.images[self.frame]

class Chuck(StaticItem):
    def __init__(self):
        super(Chuck, self).__init__()
    def init(self):
        self.rect = pygame.Rect(203, 115, 50, 75)
        self.x = 203
        self.y = 115
        self.description = 'Chuck the Plant'
        self.visible = False

class Drawer(StaticItem):
    def __init__(self):
        super(Drawer, self).__init__()
    def init(self):
        self.rect = pygame.Rect(342, 200, 65, 50)
        self.has_booboo_b_gone = True
        self.is_open = False
        self.visible = False
        self.image = load_image('drawer.png')
        self.description = 'desk drawer'
    def on_open(self):
        if not self.is_open:
            self.is_open = True
            self.visible = True
            if self.has_booboo_b_gone:
                item.booboo_b_gone.visible = True
                for g in item.booboo_b_gone.groups():
                    g.switch_layer(1, 2)
            
    def on_close(self):
        if self.is_open:
            self.is_open = False
            self.visible = False
            if self.has_booboo_b_gone:
                item.booboo_b_gone.visible = False
                for g in item.booboo_b_gone.groups():
                    g.switch_layer(1, 2)

class FickleFingers(StaticItem):
    def __init__(self):
        super(FickleFingers, self).__init__()
    def init(self):
        self.rect = pygame.Rect(368, 62, 25, 39)
        self.x = 368
        self.y = 62
        self.description = 'Fickle Fingers coin slot'
        self.visible = False
        self.state = 1
    def use_with(self, obj):
        if isinstance(obj, item.Dime):
            if self.state == 1:
                self.game.player.drop_item(obj)
                self.state = 2
                actor.conventioner.x = 335
                actor.conventioner.y = 104
            elif self.state == 2:
                self.game.player.drop_item(obj)
                self.state = 3
                actor.conventioner.sleeping_on_the_floor()
                item.sweater.is_blocked = False

class Grating(StaticItem):
    def __init__(self):
        super(Grating, self).__init__()
    def init(self):
        self.rect = pygame.Rect(336, 144, 80, 64)
#        self.poly = Polygon((356, 205), (369, 197), (415, 204), (397, 218))
        self.image = load_image('grating.png')
        self.description = 'grating'
        self.visible = False
        self.is_open = False
    def on_push(self):
        self.on_close()
    def on_pull(self):
        self.on_open()
    def on_open(self):
        if not self.is_open:
            self.is_open = True
            self.visible = True
    def on_close(self):
        if self.is_open:
            self.is_open = False
            self.visible = False

class Mailbox(StaticItem):
    def __init__(self):
        super(Mailbox, self).__init__()
    def init(self):
        self.rect = pygame.Rect(800, 96, 64, 48)
        self.x = 800
        self.y = 96
        self.image = load_image('mailbox.png')
        self.is_open = False
        self.visible = False
    def on_open(self):
        if not self.is_open:
            self.visible = True
            self.is_open = True
    def on_close(self):
        if self.is_open:
            self.visible = False
            self.is_open = False

class Mummy(StaticItem):
    def __init__(self):
        super(Mummy, self).__init__()
        self.x = 432
        self.y = 92
    def init(self):
        self.rect = pygame.Rect(432, 92, 112, 160)
        self.image = load_image('mummy.png')
        self.description = 'Dead Cousin Ted' 

class PayPhone(StaticItem):
    def __init__(self):
        super(PayPhone, self).__init__()
    def init(self):
        self.rect = pygame.Rect(528, 96, 64, 96)
        self.x = 528
        self.y = 96
        self.description = 'pay phone'
        self.visible = False

class Rack(StaticItem):
    def __init__(self):
        super(Rack, self).__init__()
    def init(self):
        self.rect = pygame.Rect(17, 225, 230, 60)
        self.rect.x = 17
        self.rect.y = 225
        #self.poly = Polygon((85, 301), (269, 301), (180, 271), (51, 241), (37, 246))
        self.description = 'rack for fliers'
        self.visible = False

class Speaker(StaticItem):
    def __init__(self):
        super(Speaker, self).__init__()
    def init(self):
        #self.rect = pygame.Rect(304, 160, 144, 96)
        self.description = 'speaker'
        self.image = load_image('speaker.png')
        self.rect = self.image.get_rect()
        self.rect.x = 304
        self.rect.y = 160
        self.is_up = True
        self.visible = False
    def on_push(self):
        """ Push the speaker. """
        if self.is_up:
            self.is_up = False
            self.visible = True

class Statue(StaticItem):
    def __init__(self):
        super(Statue, self).__init__()
    def init(self):
        self.rect = pygame.Rect(448, 16, 96, 176)
        self.images = load_images('01.png', '02.png', name='statue')
        self.image = self.images[0]
        self.description = 'statue'

class TV(StaticItem):
    """ The TV inside the suite room. """
    def __init__(self):
        super(TV, self).__init__()
    def init(self):
        self.description = 'tv'
        self.images = load_images('01.png', '02.png', '03.png',
                '04.png', name='tv')
        self.frame = 0
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = 155
        self.rect.y = 48
        self.delay = 30
        self.pause = self.delay
        self.is_on = False
        self.visible = False
    def update(self):
        self.pause = self.pause - 1
        if self.pause <= 0:
            self.pause = self.delay
            self.frame = (self.frame + 1) % len(self.images)
            self.image = self.images[self.frame]
    def on_use(self):
        if self.is_on:
            self.is_on = False
            self.visible = False
        else:
            self.is_on = True
            self.visible = True
            self.dirty = 2 

# global variables
bed = Bed()
bell = Bell()
bird_bath = BirdBath()
cabinet = Cabinet()
candy_machine = CandyMachine()
chuck = Chuck()
computer = Computer()
drawer = Drawer()
fickle_fingers = FickleFingers()
grating = Grating()
mailbox = Mailbox()
mummy = Mummy()
pay_phone = PayPhone()
rack = Rack()
speaker = Speaker()
statue = Statue()
tv = TV()
