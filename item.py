import os
import pygame
import room
import door
import static_item

from scumm import Item
from config import *

path = os.path.join('data', 'items')
path_inventory = os.path.join('data', 'inventory')

def init():
    #   another_dime.init()
    bankbook.init()
    booboo_b_gone.init()
    coffee.init()
    crank.init()
    crowbar.init()
    decaf_coffee.init()
    dime.init()
    fake_barf.init()
    flier.init()
    fork.init()
    funnel.init()
    gum.init()
    hamster.init()
    help_wanted.init()
    ink.init()
    keys.init()
    quarters.init()
    stamp_album.init()
    sweater.init()
    textbook.init()
    videotape.init()

__metaclass__ = type

def load_image(filename):
    return pygame.image.load(os.path.join(path, filename)).convert_alpha()

def load_inventory_image(filename):
    return pygame.image.load(os.path.join(path_inventory,
        filename)).convert_alpha()

def load_images(*filenames, **kwargs):
    if 'name' in kwargs:
        name = kwargs['name']
        return [pygame.image.load(os.path.join(path, name, f)).convert_alpha() for f in filenames]
    else:
        return [pygame.image.load(f).convert_alpha() for f in filenames]

class Bankbook(Item):
    def __init__(self):
        super(Bankbook, self).__init__()
    def init(self):
        self.rect = pygame.Rect(320, 176, 48, 32)
        self.description = 'Swiss bankbook'
        self.image = load_image('bankbook.png')
        self.inventory_image = load_inventory_image('bankbook.png')

class BoobooBGone(Item):
    def __init__(self):
        super(BoobooBGone, self).__init__()
    def init(self):
        self.rect = pygame.Rect(365, 205, 10, 20)
        self.description = 'Booboo-B-Gone'
        self.image = load_image('booboo-b-gone.png')
        self.visible = False
        self.inventory_image = load_inventory_image('booboo-b-gone.png')

    def on_pickup(self):
        super(BoobooBGone, self).on_pickup()
        static_item.drawer.has_booboo_b_gone = False
 
class Crank(Item):
    def __init__(self):
        super(Crank, self).__init__()
    def init(self):
        self.description = 'crank'
        self.image = load_image('crank.png')
        self.rect = self.image.get_rect()
        self.rect.x = 156
        self.rect.y = 178
        self.inventory_image = load_inventory_image('crank.png')

class Coffee(Item):
    def __init__(self):
        super(Coffee, self).__init__()
    def init(self):
        self.rect = pygame.Rect(42, 139, 80, 80)
        self.description = 'coffee'
        self.image = load_image('coffee.png')
        self.inventory_image = load_inventory_image('coffee.png')

class Quarters(Item):
    def __init__(self):
        super(Quarters, self).__init__()
    def init(self):
        self.image = load_image('quarters.png')
        self.description = 'quarters'
        self.rect = self.image.get_rect()
        self.inventory_image = load_inventory_image('quarters.png')
        self.rect.x = 271
        self.rect.y = 159

class Crowbar(Item):
    def __init__(self):
        super(Crowbar, self).__init__()
    def init(self):
        self.description = 'crowbar'
        self.inventory_image = load_inventory_image('crowbar.png')

class DecafCoffee(Item):
    def __init__(self):
        super(DecafCoffee, self).__init__()
    def init(self):
        self.rect = pygame.Rect(96, 138, 64, 80)
        #self.poly = Rect2Polygon(Rect(98, 142, 46, 44))
        self.description = 'decaf-coffee'
        self.image = load_image('decaf-coffee.png')
        self.inventory_image = load_inventory_image('decaf-coffee.png')

class Dime(Item):
    def __init__(self):
        super(Dime, self).__init__()
    def init(self):
        self.rect = pygame.Rect(560, 155, 15, 15)
        self.x = 560
        self.y = 155
        self.description = 'dime'
        self.image = load_image('dime.png')
        self.inventory_image = load_inventory_image('dime.png')
    
class FakeBarf(Item):
    def __init__(self):
        super(FakeBarf, self).__init__()
    def init(self):
        self.x = 234
        self.y = 33
        self.description = 'fake barf'
        self.image = load_image('fake_barf.png') 
        self.rect = self.image.get_rect()
        self.rect.x = 234
        self.rect.y = 33
    def on_pickup(self):
        pass

class Flier(Item):
    def __init__(self):
        super(Flier, self).__init__()
    def init(self):
        self.rect = pygame.Rect(128, 224, 64, 48)
        self.x = 128
        self.y = 224
        self.description = 'flier'
        self.image = load_image('flier.png') 
        self.inventory_image = load_inventory_image('flier.png')

class Fork(Item):
    def __init__(self):
        super(Fork, self).__init__()
    def init(self):
        self.rect = pygame.Rect(352, 192, 64, 32)
        self.description = 'fork'
        self.image = load_image('fork.png')
        self.inventory_image = load_inventory_image('fork.png')

class Funnel(Item):
    def __init__(self):
        super(Funnel, self).__init__()
    def init(self):
        self.rect = pygame.Rect(256, 160, 48, 16)
        #self.poly = Rect2Polygon(Rect(265, 159, 20, 20))
        self.description = 'funnel'
        self.image = load_image('funnel.png')
        self.inventory_image = load_inventory_image('funnel.png')
        self.visible = False
    def on_pickup(self):
        super(Funnel, self).on_pickup()
        static_item.cabinet.has_funnel = False

class Gum(Item):
    def __init__(self):
        super(Gum, self).__init__()
    def init(self):
        self.x = 405
        self.y = 230
        self.description = 'gum with a dime stuck in it'
        self.image = load_image('gum.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = 405, 230
        self.state = 'lobby'
    def on_pickup(self):
        pass
    def use_with(self, obj=None):
        if self.state == 'lobby':
            if obj == crowbar:
                self.inventory_image = load_inventory_image('gum/01.png')
                self.kill()
                self.game.player.take_item(self)
                self.state = 'gum with a dime stuck in it'
                self.game.player.gui.move_to_bottom()
                self.game.update_inventory()
        elif self.state == 'gum with a dime stuck in it':
            self.state = 'wad of gum'
            self.description = 'wad of gum'
            self.image = load_inventory_image('gum/02.png')
            
            another_dime = Dime()
            another_dime.init()

            self.game.player.take_item(another_dime)
            self.game.player.gui.move_to_bottom()
            self.game.update_inventory()
        else:
            return self

class Hamster(Item):
    """
    states:
    0 = in room
    1 = taken
    2 = frozen
    3 = cold
    4 = ok
    """
    def __init__(self):
        super(Hamster, self).__init__()
    def init(self):
        self.description = 'hamster'
        self.images = load_images('01.png', '02.png', '03.png', name='hamster')
        self.frame = 0
        self.state = 0
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.x = 477 
        self.y = 144
        self.rect.topleft = 477, 144
        self.delay = 80
        self.pause = self.delay
        self.dirty = 2
        self.inventory_image = load_inventory_image('hamster.png')
    def update(self):
        if self.state == 0:
            self.pause = self.pause - 1
            if self.pause <= 0:
                self.pause = self.delay
                self.frame = (self.frame + 1) % len(self.images)
                self.image = self.images[self.frame]
    def on_pickup(self):
        super(Hamster, self).on_pickup()
        self.state = 1

class HelpWanted(Item):
    def __init__(self):
        super(HelpWanted, self).__init__()
    def init(self):
        self.rect = pygame.Rect(16, 144, 80, 64)
        self.x = 16
        self.y = 144
        self.image = load_image('help-wanted.png')
        self.description = 'help-wanted sign'
        self.inventory_image = load_inventory_image('help-wanted.png')
    
    def on_pickup(self):
        """ Pick up this sign """
        super(HelpWanted, self).on_pickup()
        # Modify the rooms from where this sign is visible
        #game.rooms['lobby'].add_patch('rooms/lobby/nosign.png', Rect(16, 144, 80, 64))
        #game.rooms['outside'].add_patch('rooms/outside/nosign.png', Rect(640, 32, 96, 64))
        #game.rooms['car'].add_patch('rooms/car/window.png', Rect(256, 64, 48, 48))
        # FIXME: hay que arreglar lo que se ve cuando se recoge el

class Ink(Item):
    def __init__(self):
        super(Ink, self).__init__()
    def init(self):
        self.rect = pygame.Rect(512, 160, 32, 48)
        self.description = 'ink'
        self.image = load_image('ink.png')
        self.inventory_image = load_inventory_image('ink.png')
    #def on_use(self, game, other=None):
    #    if not other == None:
    #        if other.name == 'stamp album':
    #            pass

class Keys(Item):
    def __init__(self):
        super(Keys, self).__init__()

    def init(self):
        self.rects = [pygame.Rect(100, 110, 25, 25), pygame.Rect(0, 114, 21, 28)]
        self.rect = self.rects[0]
        self.description = 'keys'
        self.images = load_images('01.png', '02.png', name='keys')
        self.image = self.images[0]
        self.dirty = 0
        self.inventory_image = load_inventory_image('keys.png')

    def on_pickup(self):
        super(Keys, self).on_pickup()
        door.suite2secondfloor.has_key = False

class Stamp(Item):
    def __init__(self):
        super(Stamp, self).__init__()
    def init(self):
        self.rect = pygame.Rect(300, 175, 16, 14)
        self.description = 'stamp'
        self.image = load_image('stamp.png')

class StampAlbum(Item):
    def __init__(self):
        super(StampAlbum, self).__init__()
    def init(self):
        #       self.rect = pygame.Rect(328, 149, 50, 38)
        self.description = 'stamp album'
        self.x = 290
        self.y = 118
        self.images = load_images('01.png', '02.png', name='stamp_album')
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = 290, 118
    def on_pickup(self):
        pass
      
class Sweater(Item):
    def __init__(self):
        super(Sweater, self).__init__()
    def init(self):
        self.x = 386
        self.y = 147
        self.description = 'sweater'
        self.inventory_image = load_inventory_image('sweater.png')
        self.image = load_image('sweater.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = 386, 147
        self.is_blocked = True
    def on_pickup(self):
        if not self.is_blocked:
            super(Sweater, self).on_pickup()

class Videotape(Item):
    def __init__(self):
        super(Videotape, self).__init__()
    def init(self):
        self.description = 'videotape'
        self.image = load_image('videotape.png')
        self.x = 107
        self.y = 51
        self.rect = self.image.get_rect()
        self.rect.topleft = 107, 51
        self.inventory_image = load_inventory_image('videotape.png')
    
class Textbook(Item):
    def __init__(self):
        super(Textbook, self).__init__()
    def init(self):
        #       self.image = load_image('textbook.png')
        self.description = 'textbook'
        self.inventory_image = load_inventory_image('textbook.png')
        self.rect = self.inventory_image.get_rect()
        

# global variables
#another_dime = Dime()
bankbook = Bankbook()
booboo_b_gone = BoobooBGone()
coffee = Coffee()
crank = Crank()
crowbar = Crowbar()
decaf_coffee = DecafCoffee()
dime = Dime()
fake_barf = FakeBarf()
flier = Flier()
fork = Fork()
funnel = Funnel()
gum = Gum()
hamster = Hamster()
help_wanted = HelpWanted()
ink = Ink()
keys = Keys()
quarters = Quarters()
stamp_album = StampAlbum()
sweater = Sweater()
textbook = Textbook()
videotape = Videotape()
