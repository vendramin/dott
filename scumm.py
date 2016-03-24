import os
import pygame

__metaclass__ = type

def init(g):
    global game
    game = g

class Actor(pygame.sprite.DirtySprite):
    def __init__(self):
        super(Actor, self).__init__()
        self.items = [] 
        self.description = 'unkown actor'
        self.room = None
        self.dirty = 2
    @property
    def game(self):
        global game
        return game
    def use_with(self, obj=None):
        if obj == None:
            return self
    def on_open(self):
        pass
    def on_close(self):
        pass
    def on_use(self):
        pass
    def on_push(self):
        pass
    def on_pull(self):
        pass
    def on_talkto(self):
        pass
    def on_pickup(self):
        pass
    def on_walk(self):
        pass
    def walk(self, where):
        pass
    def look(self, stuff):
        pass
    def talk(self, other):
        pass
    def use(self, item):
        pass

class Player(Actor):
    def __init__(self):
        super(Player, self).__init__()
    @property
    def inventory(self):
        return self.items

    def take_item(self, item):
        """ Take an item """
        self.items.append(item)
        item.owner = self
        item.image = item.inventory_image

    def drop_item(self, item):
        """ Drop an item """
        self.items.remove(item)
        item.kill()
        item.owner = None

    def has_item(self, item):
        """ Returns true if the item belongs to the inventory """
        return item in self.inventory

class Item(pygame.sprite.DirtySprite):
    def __init__(self):
        super(Item, self).__init__()
        self.description = 'unkown object'
        self.owner = None
        self.room = None
        self.x = 0
        self.y = 0

    @property
    def game(self):
        global game
        return game

    def scale(self, value):
        self.image = pygame.transform.rotozoom(self.image, 0, value)

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)

#    def update(self):
#        if not self.room == None: 
#            self.rect.x = self.x + self.room.x 
#            self.rect.y = self.y + self.room.y

    def on_use(self):
        pass

    def on_push(self):
        pass

    def on_pull(self):
        pass

    def on_walk(self):
        pass

    def on_open(self):
        pass

    def use_with(self, obj=None):
        if obj == None:
            return self

    def on_close(self):
        pass

    def on_pickup(self):
        if not self.game.player.has_item(self):
            self.kill()
            self.game.player.take_item(self)
            self.game.player.gui.move_to_bottom()
            self.game.update_inventory()


class StaticItem(Item):
    """ Class for items that cannot be taken from the room """
    def on_pickup(self):
        pass

class Door(StaticItem):
    """ Class for doors. """
    def __init__(self):
        """ 
        """
        super(Door, self).__init__()
        self.is_open = False
        self.visible = False
        self.description = 'door'
      
    def on_open(self):
        if not self.is_open:
            self.visible = True
            self.is_open = True
            self.to.on_open()

    def on_close(self):
        if self.is_open:
            self.visible = False
            self.is_open = False
            self.to.on_close()

    def on_pickup(self):
        pass

    def on_walk(self):
        if self.is_open:
            self.game.change_room(self.to.room)

class Room(object):
    def __init__(self):
        self.image = None
        self.x = 0
        self.y = 0
        
    @property
    def item(self):
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
            self.x = self.x
            self.y = self.y-20
        if event.key == K_UP:
            self.x = self.x
            self.y = self.y+20
        if event.key == K_RIGHT:
            self.x = self.x-20
            self.y = self.y
        if event.key == K_LEFT:
            self.x = self.x+20
            self.y = self.y
        print "Camera position ", self.x, self.y

    def update_sprites(self):
        for s in self.sprites:
            s.rect.x = s.x + self.x
            s.rect.y = s.y + self.y
            if not s.dirty == 2:
                s.dirty = 1
 
    def draw(self, game):
        pass


