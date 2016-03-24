import os
import pygame

from config import *

path = os.path.join('data', 'gui')

def load_image(filename):
    return pygame.image.load(os.path.join(path, filename)).convert_alpha()

__metaclas__ = type 

class Button(pygame.sprite.DirtySprite):
    def __init__(self):
        super(Button, self).__init__()
        self.visible = False
    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.visible = True
        else:
            self.visible = False

class Give(Button):
    def __init__(self):
        super(Give, self).__init__()
        self.image = load_image('give.png')
        self.rect = self.image.get_rect()
        self.rect.x = 2
        self.rect.y = 305
        self.verb = GIVE

class Open(Button):
    def __init__(self):
        super(Open, self).__init__()
        self.image = load_image('open.png')
        self.rect = self.image.get_rect()
        self.rect.x = 4
        self.rect.y = 337
        self.verb = OPEN

class Close(Button):
    def __init__(self):
        super(Close, self).__init__()
        self.image = load_image('close.png')
        self.rect = self.image.get_rect()
        self.rect.x = 3
        self.rect.y = 368
        self.verb = CLOSE

class PickUp(Button):
    def __init__(self):
        super(PickUp, self).__init__()
        self.image = load_image('pick_up.png')
        self.rect = self.image.get_rect()
        self.rect.x = 81
        self.rect.y = 305
        self.verb = PICK_UP

class LookAt(Button):
    def __init__(self):
        super(LookAt, self).__init__()
        self.image = load_image('look_at.png')
        self.rect = self.image.get_rect()
        self.rect.x = 82
        self.rect.y = 338
        self.verb = LOOK_AT

class TalkTo(Button):
    def __init__(self):
        super(TalkTo, self).__init__()
        self.image = load_image('talk_to.png')
        self.rect = self.image.get_rect()
        self.rect.x = 85 
        self.rect.y = 369
        self.verb = TALK_TO

class Use(Button):
    def __init__(self):
        super(Use, self).__init__()
        self.image = load_image('use.png')
        self.rect = self.image.get_rect()
        self.rect.x = 213
        self.rect.y = 305
        self.verb = USE

class Push(Button):
    def __init__(self):
        super(Push, self).__init__()
        self.image = load_image('push.png')
        self.rect = self.image.get_rect()
        self.rect.x = 213
        self.rect.y = 337
        self.verb = PUSH

class Pull(Button):
    def __init__(self):
        super(Pull, self).__init__()
        self.image = load_image('pull.png')
        self.rect = self.image.get_rect()
        self.rect.x = 212
        self.rect.y = 369 
        self.verb = PULL

class Up(Button):
    def __init__(self):
        super(Up, self).__init__()
        self.image = load_image('up.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = 290, 307 
        self.visible = True
    def update(self):
        pass

class Down(Button):
    def __init__(self):
        super(Down, self).__init__()
        self.image = load_image('down.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = 290, 358
        self.visible = True
    def update(self):
        pass

class GUI(object):
    pos = [(322, 301), (402, 301), (482, 301), (322, 350), (402, 350), (482, 350)]
    def __init__(self, inventory=None):
        self.open = Open()
        self.give = Give()
        self.close = Close()
        self.pick_up = PickUp()
        self.look_at = LookAt()
        self.talk_to = TalkTo()
        self.use = Use()
        self.push = Push()
        self.pull = Pull()
        self.up = Up()
        self.down = Down()

        if not inventory == None:
            self.inventory = inventory
        else:
            self.inventory = []

        self.row = 0
        self.items = pygame.sprite.LayeredDirty()
        self.verbs = pygame.sprite.LayeredDirty(self.give, self.open,
                self.close, self.pick_up, self.look_at, self.talk_to,
                self.use, self.pull, self.push) 

    def update(self):
        self.items.empty()
        if self.row > 0:
            self.up.visible = True
            self.items.add(self.up)
        else:
            self.up.kill()

        if self.row < len(self.inventory)-6:
            self.down.visible = True
            self.items.add(self.down)
        else:
            self.down.kill()

        for i, item in enumerate(self.inventory[self.row:]):
            item.rect = item.inventory_image.get_rect()
            item.rect.topleft = GUI().pos[i]
            self.items.add(item)
            if i == 5:
                break

    def move_down(self):
        if self.row < len(self.inventory)-6:
            self.row = self.row + 3
            self.update()

    def move_up(self):
        if self.row > 0:
            self.row = self.row - 3
            self.update()

    def move_to_bottom(self):
        self.row = 0
        while self.row < len(self.inventory)-6:
            self.row = self.row + 3 
        self.update()

    def move_to_top(self):
        self.row = 0
        self.update()

