import os
import pygame

import actor
import item
import door
import static_item

from scumm import Room

path = os.path.join('data', 'rooms')

def load_image(filename):
    """ Load and convert an image. """
    return pygame.image.load(os.path.join(path, filename)).convert()

def init():
    """ Initialize all rooms. """
    attic.init()
    basement.init()
    car.init()
    kitchen.init()
    laundry.init()
    lobby.init()
    hallway.init()
    ed.init()
    edna.init()
    green.init()
    outside.init()
    playroom.init()
    roof.init()
    study.init()
    sad.init()
    secondfloor.init()
    suite.init()
    warehouse.init()
    water.init()

__metaclass__ = type

class Attic(Room):
    def __init__(self):
        super(Attic, self).__init__()
    def init(self):
        self.image = load_image('attic.png')
        self.sprites = pygame.sprite.LayeredDirty(door.attic2roof,
                door.attic2warehouse, static_item.bed)

class Basement(Room):
    def __init__(self):
        super(Basement, self).__init__()
    def init(self):
        self.image = load_image('basement.png')
        self.sprites = pygame.sprite.LayeredDirty(door.basement2lobby)

class Car(Room):    
    def __init__(self):
        super(Car, self).__init__()
    def init(self):
        self.image = load_image('car.png')
        self.sprites = pygame.sprite.LayeredDirty(door.car2water,
                door.car2outside, actor.thief)

class Green(Room):    
    def __init__(self): 
        super(Green, self).__init__()
    def init(self):
        self.image = load_image('green.png')
        self.sprites = pygame.sprite.LayeredDirty(door.green2secondfloor,
                static_item.speaker, item.videotape)

class Kitchen(Room):
    def __init__(self):
        super(Kitchen, self).__init__()
    def init(self):
        self.image = load_image('kitchen.png')
        self.sprites = pygame.sprite.LayeredDirty(door.kitchen2playroom,
                door.kitchen2laundry, item.fork)
        self.sprites.add(item.decaf_coffee, layer=0)
        self.sprites.add(item.coffee, layer=1)

class Laundry(Room):    
    def __init__(self):
        super(Laundry, self).__init__()
    def init(self):
        self.image = load_image('laundry.png')
        self.sprites = pygame.sprite.LayeredDirty(door.laundry2kitchen)
        self.sprites.add(item.funnel, layer=1)
        self.sprites.add(static_item.cabinet, layer=2)

class Lobby(Room):    
    def __init__(self):
        super(Lobby, self).__init__()
    def init(self):
        self.image = load_image('lobby.png')
        self.sprites = pygame.sprite.LayeredDirty(door.lobby2playroom,
                door.lobby2outside, door.lobby2secondfloor, door.lobby2study,
                door.lobby2basement, static_item.rack,
                static_item.chuck, static_item.bell, item.fake_barf,
                item.gum)
        self.sprites.add(item.help_wanted, item.flier, static_item.pay_phone, layer=1)
        self.sprites.add(item.dime, layer=2)

class Outside(Room):
    def __init__(self):
        super(Outside, self).__init__()
    def init(self):
        self.image = load_image('outside.png')
        self.sprites = pygame.sprite.LayeredDirty(door.outside2lobby,
                door.outside2car, static_item.mailbox)
        self.sprites.add(static_item.mummy, layer=1)
        self.sprites.add(static_item.bird_bath, layer=2)

class Playroom(Room):    
    def __init__(self):
        super(Playroom, self).__init__()
    def init(self):
        self.image = load_image('playroom.png')
        self.sprites = pygame.sprite.LayeredDirty(door.playroom2lobby,
                door.playroom2kitchen, door.playroom2roof) 
        self.sprites.add(static_item.grating, layer=1)

class Roof(Room):
    def __init__(self):
        super(Roof, self).__init__()
    def init(self):
        self.image = load_image('roof.png')
        self.sprites = pygame.sprite.LayeredDirty(door.roof2attic,
                door.roof2playroom, item.crank)

class Secondfloor(Room):
    def __init__(self):
        super(Secondfloor, self).__init__()
    def init(self):
        self.image = load_image('secondfloor.png')
        self.sprites = pygame.sprite.LayeredDirty(door.secondfloor2hallway,
                door.secondfloor2lobby, door.secondfloor2suite,
                door.secondfloor2green, door.secondfloor2sad,
                static_item.candy_machine)

class Study(Room):    
    def __init__(self):
        super(Study, self).__init__()
    def init(self):
        self.image = load_image('study.png')
        self.sprites = pygame.sprite.LayeredDirty(door.study2lobby, item.bankbook)
        self.sprites.add(item.booboo_b_gone, layer=1)
        self.sprites.add(static_item.drawer, layer=2)

class Suite(Room):    
    def __init__(self):
        super(Suite, self).__init__()
    def init(self):
        self.image = load_image('suite.png')
        self.sprites = pygame.sprite.LayeredDirty(door.suite2secondfloor,
                item.sweater, static_item.tv, static_item.fickle_fingers)
        self.sprites.add(actor.conventioner, item.keys, layer=1)
#        self.sprites.add(item.keys, layer=1)

class Warehouse(Room):    
    def __init__(self):
        super(Warehouse, self).__init__()
    def init(self):
        self.image = load_image('warehouse.png')
        self.sprites = pygame.sprite.LayeredDirty(door.warehouse2attic,
                door.warehouse2hallway)

class Hallway(Room):    
    def __init__(self):
        super(Hallway, self).__init__()
    def init(self):
        self.image = load_image('hallway.png')
#        self.add_patch('rooms/hallway/patch1.png', Rect(320, 144, 64, 48))
#        self.add_patch('rooms/hallway/patch2.png', Rect(288, 160, 64, 32))
        self.sprites = pygame.sprite.LayeredDirty(door.hallway2warehouse,
                door.hallway2secondfloor, door.hallway2ed, door.hallway2edna)

class Ed(Room):    
    def __init__(self):
        super(Ed, self).__init__()
    def init(self):
        self.image = load_image('ed.png')
        self.sprites = pygame.sprite.LayeredDirty(door.ed2hallway,
                static_item.computer, item.stamp_album, item.hamster)

class Edna(Room):    
    def __init__(self):
        super(Edna, self).__init__()
    def init(self):
        self.image = load_image('edna.png')
        self.sprites = pygame.sprite.LayeredDirty(door.edna2hallway,
                static_item.statue)

class Sad(Room):    
    def __init__(self):
        super(Sad, self).__init__()
    def init(self):
        self.image = load_image('sad.png')
        self.sprites = pygame.sprite.LayeredDirty(door.sad2secondfloor)
        self.sprites.add(item.ink, layer=1)

class Water(Room):    
    def __init__(self):
        super(Water, self).__init__()
    def init(self):
        self.image = load_image('water.png')
        self.sprites = pygame.sprite.LayeredDirty(door.water2car)

""" Global variables. """
attic = Attic()
basement = Basement()
car = Car()
ed = Ed()
edna = Edna()
green = Green()
hallway = Hallway()
kitchen = Kitchen()
laundry = Laundry()
lobby = Lobby()
outside = Outside()
playroom = Playroom()
roof = Roof()
sad = Sad()
secondfloor = Secondfloor()
study = Study()
suite = Suite()
warehouse = Warehouse()
water = Water()
