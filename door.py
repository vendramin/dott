import os
import pygame
import room
import item

from scumm import Door

__metaclass__ = type

path = os.path.join('data', 'doors')

def load_image(filename):
    return pygame.image.load(os.path.join(path, filename)).convert_alpha()

def load_images(*filenames, **kwargs):
    if 'name' in kwargs:
        name = kwargs['name']
        return [pygame.image.load(os.path.join(path, name, f)).convert_alpha() for f in filenames]
    else:
        return [pygame.image.load(f).convert_alpha() for f in filenames]

def init():
    attic2roof.init()
    attic2warehouse.init()
    basement2lobby.init()
    car2outside.init()
    car2water.init()
    lobby2basement.init()
    ed2hallway.init()
    edna2hallway.init()
    green2secondfloor.init()
    hallway2warehouse.init()
    hallway2secondfloor.init()
    hallway2ed.init()
    hallway2edna.init()
    kitchen2laundry.init()
    kitchen2playroom.init()
    laundry2kitchen.init()
    lobby2outside.init()
    lobby2playroom.init()
    lobby2secondfloor.init()
    lobby2study.init()
    outside2car.init()
    outside2lobby.init()
    playroom2kitchen.init()
    playroom2lobby.init()
    playroom2roof.init()
    roof2attic.init()
    roof2playroom.init()
    sad2secondfloor.init()
    secondfloor2hallway.init()
    secondfloor2lobby.init()
    secondfloor2green.init()
    secondfloor2sad.init()
    secondfloor2suite.init()
    study2lobby.init()
    suite2secondfloor.init()
    warehouse2attic.init()
    warehouse2hallway.init()
    water2car.init()

class CarToWater(Door):
    def __init__(self):
        super(CarToWater, self).__init__()
    def init(self):
        self.rect = pygame.Rect(550, 0, 90, 170)
        self.description = 'path'
        self.is_open = True
        self.to = water2car
        self.room = room.car
    def on_open(self):
        pass
    def on_close(self):
        pass
 
class CarToOutside(Door):
    def __init__(self):
        super(CarToOutside, self).__init__()
    def init(self):
        self.rect = pygame.Rect(175, 0, 150, 150)
        self.is_open = True
        self.description = 'motel'
        self.to = outside2car
        self.room = room.car
    def on_open(self):
        pass
    def on_close(self):
        pass
 
class PlayroomToLobby(Door):
    def __init__(self):
        super(PlayroomToLobby, self).__init__()
    def init(self):
        self.image = load_image('playroom2lobby.png')
        self.room = room.playroom
        self.to = lobby2playroom
        self.rect = pygame.Rect(48, 80, 112, 176)
        self.x = 48
        self.y = 80

class LobbyToBasement(Door):
    def __init__(self):
        super(LobbyToBasement, self).__init__()
    def init(self):
        self.dirty = 2
        self.visible = True
        self.delay = 60
        self.pause = self.delay
        self.frame = 0
        self.frames = [0,1,2,1]
        self.description = 'grandfather clock'
        self.images = load_images('01.png', '02.png', '03.png',
                '04.png', name='clock')
        self.image = self.images[0]
        self.rect = self.image.get_rect()  
        self.x = 640
        self.y = 112
        self.room = room.lobby
        self.to = basement2lobby
        self.room = room.lobby
        self.is_open

    def on_open(self):
        if not self.is_open:
            self.is_open = True
            self.dirty = 1
            self.image = self.images[3]
            self.rect = pygame.Rect(592, 112, 144, 80)
            self.x = 592
            self.y = 112
            self.description = 'dark passage'

    def on_close(self):
        if self.is_open:
            self.is_open = False
            self.dirty = 2
            self.frame = 0
            self.image = self.images[self.frame]
            self.x = 640
            self.y = 112
            self.rect = self.image.get_rect()  
            self.description = 'old clock'

    def on_walk(self):
        if self.is_open:
            self.game.change_room(self.to.room)

    def update(self):
        self.rect.x = self.x + self.room.x 
        self.rect.y = self.y + self.room.y
        if not self.is_open:
            self.pause = self.pause - 1
            if self.pause <= 0:
                self.pause = self.delay
                self.frame = (self.frame + 1) % 4
                self.image = self.images[self.frames[self.frame]]


class LobbyToOutside(Door):
    def __init__(self):
        super(LobbyToOutside, self).__init__()
        self.x = 96
        self.y = 64
    def init(self):
        self.rect = pygame.Rect(96, 64, 80, 176)
        self.image = load_image('lobby2outside.png')
        self.room = room.lobby
        self.to = outside2lobby
#    def on_open(self):
#        super(LobbyToOutside, self).on_open()
## #       game.room['car'].add_patch('room/car/open.png', Rect(160, 64, 48, 48))
#    def on_close(self):
#        super(LobbyToOutside, self).on_close()
###        game.room['car'].add_patch('room/car/closed.png', Rect(160, 64, 48, 48))
        
class LobbyToSecondfloor(Door):
    def __init__(self): 
        super(LobbyToSecondfloor, self).__init__()
        self.x = 770
        self.y = 0
    def init(self):
        self.rect = pygame.Rect(750, 0, 170, 280)
        self.is_open = True
        self.visible = False
        self.to = secondfloor2lobby
        self.room = room.lobby
        self.description = 'stairs'
        
    def on_open(self):
        pass

    def on_close(self):
        pass

class SecondfloorToHallway(Door):
    def __init__(self):
        super(SecondfloorToHallway, self).__init__()
        self.x = 750
        self.y = 80
    def init(self):
                #self.poly = Polygon((794, 90), (844, 90), (823, 160), (773, 153)); 
        self.rect = pygame.Rect(750, 80, 110, 90)
        self.is_open = True
        self.visible = False
        self.to = hallway2secondfloor
        self.room = room.secondfloor
        self.description = 'stairs'
    def on_open(self):
        pass
    def on_close(self):
        pass

class LobbyToPlayroom(Door):
    def __init__(self):
        super(LobbyToPlayroom, self).__init__()
        self.visible = False
        self.x = 240
        self.y = 80
    def init(self):
        self.image = load_image('lobby2playroom.png')
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(240, 80, 160, 128)
        self.room = room.lobby
        self.to = playroom2lobby 

class LobbyToStudy(Door):
    def __init__(self):
        super(LobbyToStudy, self).__init__()
        self.x = 448
        self.y = 64
    def init(self):
        #self.poly = Polygon((480,  113), (531,  81),  (552,  128),  (563,  175),  (560,  207),  (552,  218),  (520,  214))
        self.rect = pygame.Rect(448, 64, 80, 144)
        self.image = load_image('lobby2study.png')
        self.room = room.lobby
        self.to = study2lobby

class StudyToLobby(Door):
    def __init__(self):
        super(StudyToLobby, self).__init__()
        self.x = 96
        self.y = 64
    def init(self):
        self.rect = pygame.Rect(96, 64, 112, 160)
        self.image = load_image('study2lobby.png')
        self.room = room.study
        self.to = lobby2study

class OutsideToCar(Door):
    def __init__(self):
        super(OutsideToCar, self).__init__()
    def init(self):
        self.rect = pygame.Rect(900, 0, 50, 300)
        self.x = 900
        self.y = 0
        self.is_open = True
        self.description = 'parking lot'
        self.to = car2outside
        self.room = room.outside
    def on_close(self):
        pass
    def on_open(self):
        pass

class OutsideToLobby(Door):
    def __init__(self):
        super(OutsideToLobby, self).__init__()
        self.x = 384
        self.y = 0
    def init(self):
        self.rect = pygame.Rect(384, 0, 96, 128)
        self.image = load_image('outside2lobby.png')
        self.room = room.outside
        self.to = lobby2outside
    def on_open(self):
        super(OutsideToLobby, self).on_open()
        #game.room['car'].add_patch('room/car/open.png', Rect(160, 64, 48, 48))
    def on_close(self):
        super(OutsideToLobby, self).on_close()
        #game.room['car'].add_patch('room/car/closed.png', Rect(160, 64, 48, 48))

class KitchenToPlayroom(Door):
    def __init__(self):
        super(KitchenToPlayroom, self).__init__()
        self.x = 368
        self.y = 64
    def init(self):
        self.rect = pygame.Rect(368, 64, 80, 128)
        self.is_open = True
        self.visible = False
        self.room = room.kitchen
        self.to = playroom2kitchen
    def on_open(self):
        pass
    def on_close(self):
        pass

class LaundryToKitchen(Door):
    def __init__(self):
        super(LaundryToKitchen, self).__init__()
        self.x = 144
        self.y = 64
    def init(self):
        self.rect = pygame.Rect(144, 64, 80, 160)
        self.image = load_image('laundry2kitchen.png')
        self.to = kitchen2laundry
        self.room = room.laundry

class PlayroomToKitchen(Door):
    def __init__(self):
        super(PlayroomToKitchen, self).__init__()
        self.x = 288
        self.y = 80
    def init(self):
        self.rect = pygame.Rect(288, 80, 80, 112)
#        self.poly = Polygon((360,192), (374, 98), (327, 97), (330, 189))
        self.is_open = True
        self.description = 'swinging door'
        self.room = room.playroom
        self.to = kitchen2playroom
    def on_open(self):
        pass
    def on_close(self):
        pass 

class KitchenToLaundry(Door):
    def __init__(self):
        super(KitchenToLaundry, self).__init__()
        self.x = 464
        self.y = 32
    def init(self):
        self.rect = pygame.Rect(464, 32, 64, 172)
        self.image = load_image('kitchen2laundry.png')
        self.to = laundry2kitchen
        self.room = room.kitchen

class PlayroomToRoof(Door):
    def __init__(self):
        super(PlayroomToRoof, self).__init__()
        self.x = 415
        self.y = 95
    def init(self):
        #self.poly = Polygon((433, 129), (593, 111), (487, 214), (457, 211))
        self.rect = pygame.Rect(415, 95, 75, 100)
        self.room = room.playroom
        self.to = roof2playroom
        self.is_open = True
        self.visible = False
        self.description = 'chimney'
    def on_open(self):
        pass
    def on_close(self):
        pass 
 
class RoofToAttic(Door):
    def __init__(self):
        super(RoofToAttic, self).__init__()
        self.x = 415
        self.y = 165
    def init(self):
        #self.poly = Polygon((440, 185), (496, 185), (504, 236), (466, 238))
        self.rect = pygame.Rect(415, 165, 75, 60)
        self.is_open = True
        self.is_visible = False
        self.to = attic2roof
        self.room = room.roof
        self.description = 'window'
    def on_open(self):
        pass
    def on_close(self):
        pass

class RoofToPlayroom(Door):
    def __init__(self):
        super(RoofToPlayroom, self).__init__()
        self.x = 125
        self.y = 70
    def init(self):
        self.to = playroom2roof
        self.room = room.roof
        self.rect = pygame.Rect(125, 70, 95, 70)
#        self.poly = Polygon((140, 141), (169, 115), (227, 123), (233, 194), (196, 206))
        self.is_open = True
        self.visible = False
        self.description = 'chimney'
    def on_open(self):
        pass
    def on_close(self):
        pass

class AtticToRoof(Door):
    def __init__(self):
        super(AtticToRoof, self).__init__()
        self.x = 125
        self.y = 92
    def init(self):
        self.is_open = True
        self.is_visible = False
#        self.poly = Polygon((127, 92), (152, 100), (152, 157), (118, 175))
        self.rect = pygame.Rect(125, 92, 50, 70)
        self.description = 'window'
        self.to = roof2attic
        self.room = room.attic
    def on_open(self):
        pass
    def on_close(self):
        pass

class AtticToWarehouse(Door):
    def __init__(self):
        super(AtticToWarehouse, self).__init__()
        self.x = 432
        self.y = 32
    def init(self):
        self.rect = pygame.Rect(432, 32, 96, 160) 
        self.image = load_image('attic2file.png')
        self.to = warehouse2attic
        self.room = room.attic
    def on_open(self):
        super(AtticToWarehouse, self).on_open()

    def on_close(self):
        super(AtticToWarehouse, self).on_close()

class BasementToLobby(Door):
    def __init__(self):
        super(BasementToLobby, self).__init__()
        self.x = 716
        self.y = 10
    def init(self):
        self.rect = pygame.Rect(716, 10, 80, 115)
        self.is_open = True
        self.is_visible = False
        self.to = lobby2basement
        self.room = room.basement
    def on_open(self):
        pass
    def on_close(self):
        pass
    def on_walk(self):
        self.to.on_open()
        super(BasementToLobby, self).on_walk()

class SuiteToSecondfloor(Door):
    def __init__(self):
        super(SuiteToSecondfloor, self).__init__()
        self.x = 0
        self.y = 0
        self.has_key = True
    def init(self):
        self.rect = pygame.Rect(0, 0, 128, 192)
        self.visible = False
        self.to = secondfloor2suite
        self.room = room.suite
        self.image = load_image('suite2secondfloor.png')

    def on_open(self):
        super(SuiteToSecondfloor, self).on_open()
        if self.has_key:
            item.keys.rect = item.keys.rects[1]
            item.keys.image = item.keys.images[1]
            item.keys.dirty = 1
 
    def on_close(self):
        super(SuiteToSecondfloor, self).on_close()
        if self.has_key:
            item.keys.rect = item.keys.rects[0]
            item.keys.image = item.keys.images[0]
            item.keys.dirty = 1

class SecondfloorToSuite(Door):
    def __init__(self):
        super(SecondfloorToSuite, self).__init__()
        self.x = 224
        self.y = 32
    def init(self):
        self.rect = pygame.Rect(224, 32, 96, 160)
        self.image = load_image('secondfloor2suite.png')
        self.room = room.secondfloor
        self.to = suite2secondfloor 

class SecondfloorToSad(Door):
    def __init__(self):
        super(SecondfloorToSad, self).__init__()
        self.x = 496
        self.y = 32
    def init(self):
        self.rect = pygame.Rect(496, 32, 80, 160)
        self.image = load_image('secondfloor2sad.png')
        self.to = sad2secondfloor
        self.room = room.secondfloor

class SecondfloorToGreen(Door):
    def __init__(self):
        super(SecondfloorToGreen, self).__init__()
        self.x = 656
        self.y = 64
    def init(self):
        self.rect = pygame.Rect(656, 64, 64, 96)
        self.image = load_image('secondfloor2green.png')
        self.to = green2secondfloor
        self.room = room.secondfloor
       
class SecondfloorToLobby(Door):
    def __init__(self):
        super(SecondfloorToLobby, self).__init__()
        self.x = 151
        self.y = 102
    def init(self):
        self.visible = False
        self.to = lobby2secondfloor
        self.room = room.secondfloor
        self.rect = pygame.Rect(151, 102, 50, 70)
        self.is_open = True
        self.description = 'stairs'
    def on_open(self):
        pass
    def on_close(self):
        pass

class WarehouseToAttic(Door):
    def __init__(self):
        super(WarehouseToAttic, self).__init__()
        self.x = 464
        self.y = 48
    def init(self):
        self.rect = pygame.Rect(464, 48, 112, 160)
        self.image = load_image('warehouse2attic.png')
        self.to = attic2warehouse
        self.room = room.warehouse

class WarehouseToHallway(Door):
    def __init__(self):
        super(WarehouseToHallway, self).__init__()
        self.x = 16
        self.y = 128
    def init(self):
        self.rect = pygame.Rect(16, 128, 192, 160)
        self.image = load_image('warehouse2hallway.png')
        self.is_open = True
        self.visible = True
        self.room = room.warehouse
        self.to = hallway2warehouse
 
class HallwayToEd(Door):
    def __init__(self):
        super(HallwayToEd, self).__init__()
        self.x = 384
        self.y = 16
    def init(self):
        self.rect = pygame.Rect(384, 16, 80, 192)
        self.room = room.hallway
        self.to = ed2hallway
        self.image = load_image('hallway2ed.png')

class HallwayToEdna(Door):
    def __init__(self):
        super(HallwayToEdna, self).__init__()
        self.x = 176
        self.y = 16
    def init(self):
        self.rect = pygame.Rect(176, 16, 96, 176)
        self.image = load_image('hallway2edna.png')
        self.room = room.hallway
        self.to = edna2hallway

class HallwayToSecondfloor(Door):
    def __init__(self):
        super(HallwayToSecondfloor, self).__init__()
        self.x = 280
        self.y = 0
        #self.poly = Polygon((338, 13), (350, 120), (307, 150), (227, 47), (292, 13))
    def init(self):
        self.rect = pygame.Rect(280, 0, 50, 120)
        self.is_open = True
        self.is_visible = False
        self.description = 'stairway'
        self.to = secondfloor2hallway
        self.room = room.hallway
    def on_open(self):
        pass
    def on_close(self):
        pass

class HallwayToWarehouse(Door):
    def __init__(self):
        super(HallwayToWarehouse, self).__init__()
        self.x = 0
        self.y = 0
    def init(self):
        #self.poly = Polygon((138, 207), (217, 251), (186, 300))
        self.rect = pygame.Rect(0, 0, 150, 280)
        self.is_open = True
        self.is_visible = False
        self.description = 'stairway'
        self.room = room.hallway
        self.to = warehouse2hallway
    def on_open(self):
        pass
    def on_close(self):
        pass
    def on_walk(self):
        if warehouse2hallway.is_open == False:
            warehouse2hallway.on_open()
        self.game.change_room(self.to.room)
    #        if not game.doors[self.to].is_open:
    #            game.doors[self.to].is_open = True
    #            game.doors[self.to].state = OPEN
    #        game.room = game.room[game.doors[self.to].room]    
        #if not Door.d[self.to].is_open:
        #    Door.d[self.to].is_open = True
        #    Door.d[self.to].state = OPEN
        #game.room = game.room[Door.d[self.to].room]

class EdToHallway(Door):
    def __init__(self):
        super(EdToHallway, self).__init__()
        self.x = 112
        self.y = 32
    def init(self):
        self.rect = pygame.Rect(112, 32, 64, 176)
        self.image = load_image('edd2hallway.png')
        self.to = hallway2ed
        self.room = room.ed

class EdnaToHallway(Door):
    def __init__(self):
        super(EdnaToHallway, self).__init__()
        self.x = 528
        self.y = 48
    def init(self):
        self.to = hallway2edna
        self.room = room.edna
        self.rect = pygame.Rect(528, 48, 80, 160)
        self.image = load_image('edna2hallway.png')

class SadToSecondfloor(Door):
    def __init__(self):
        super(SadToSecondfloor, self).__init__()
        self.x = 448
        self.y = 48
        self.is_locked = True
    def init(self):
        self.rect = pygame.Rect(448, 48, 96, 192)
        self.visible = False
        self.image = load_image('sad2secondfloor_locked.png')
        self.to = secondfloor2sad
        self.room = room.sad
    def on_close(self):
        # if the door is locked...
        if self.is_locked:
            super(SadToSecondfloor, self).on_close()
            self.game.change_room(room.secondfloor)

class GreenToSecondfloor(Door):
    def __init__(self):
        super(GreenToSecondfloor, self).__init__()
        self.x = 144
        self.y = 0
    def init(self):
        self.rect = pygame.Rect(144, 0, 160, 160)
        self.image = load_image('green2secondfloor.png')
        self.to = secondfloor2green 
        self.room = room.green

class WaterToCar(Door):
    def __init__(self):
        super(WaterToCar, self).__init__()
    def init(self):
        self.rect = pygame.Rect(0, 0, 150, 300)
        self.is_open = True
        self.description = 'path'
        self.to = car2water
        self.room = room.water
    def on_open(self):
        pass
    def on_close(self):
        pass
 
### global variables
attic2warehouse = AtticToWarehouse()
attic2roof = AtticToRoof()
basement2lobby = BasementToLobby()
car2outside = CarToOutside()
car2water =  CarToWater()
ed2hallway = EdToHallway()
edna2hallway = EdnaToHallway()
green2secondfloor = GreenToSecondfloor()
hallway2secondfloor = HallwayToSecondfloor()
hallway2ed = HallwayToEd()
hallway2edna = HallwayToEdna()
hallway2warehouse = HallwayToWarehouse()
kitchen2laundry = KitchenToLaundry()
kitchen2playroom = KitchenToPlayroom()
laundry2kitchen = LaundryToKitchen()
lobby2basement = LobbyToBasement()
lobby2playroom = LobbyToPlayroom()
lobby2outside = LobbyToOutside()
lobby2secondfloor = LobbyToSecondfloor()
lobby2study = LobbyToStudy()
playroom2kitchen = PlayroomToKitchen()
playroom2lobby = PlayroomToLobby()
playroom2roof = PlayroomToRoof()
sad2secondfloor = SadToSecondfloor()
secondfloor2suite = SecondfloorToSuite()
secondfloor2sad =  SecondfloorToSad()
secondfloor2green = SecondfloorToGreen()
secondfloor2lobby = SecondfloorToLobby()
secondfloor2hallway = SecondfloorToHallway()
suite2secondfloor = SuiteToSecondfloor()
study2lobby = StudyToLobby()
outside2lobby = OutsideToLobby()
outside2car = OutsideToCar()
roof2attic = RoofToAttic()
roof2playroom =  RoofToPlayroom() 
warehouse2hallway = WarehouseToHallway()
warehouse2attic = WarehouseToAttic()
water2car =  WaterToCar()
