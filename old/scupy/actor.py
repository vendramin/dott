import pygame

__metaclass__ = type

class Actor(object):
    def __init__(self, name=''):
        self.items = [] 
        self.name = name
        self.room = None

    @property
    def inventory(self):
        return self.items

    def take_item(self, name):
        self.items.append(name)
#        if name in self.items:
#            self.items[name] = self.items[name] + 1
#        else:
#            self.items[name] = 1
#        self.items[name] = self.items[name] + 1 
#        self.items[item.name] = item

    def drop_item(self, name):
        self.items.remove(name)
        #if name in self.inventory:
        #    del self.items[name]

    def has_item(self, name):
        return name in self.inventory

    def walk(self, where):
        pass

    def look(self, stuff):
        pass

    def talk(self, other):
        pass

    def use(self, item):
        pass

    def open(self,  door):
        if not door.is_open:
            door.is_open = True
        
    def close(self, door):
        if door.is_open:
            door.is_open = False

    def info(self):
        print self.name
        print "%s has..." % self.name
        print self.inventory


class Player(Actor):
    pass
