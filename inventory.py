__metaclas__ = type 

class Button(pygame.sprite.DirtySprite):
    def __init__(self):
        super(Button, self).__init__()
    def init(self):
        self.image = pygame.image.load('open1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 301
        self.visible = False
        self.dirty = 1
    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.visible = True
        else:
            self.visible = False

class Give(Button):
    pass
class Open(Button):
    pass
class Close(Button):
    pass
class PickUp(Button):
    pass
class LockUp(Button):
    pass
class TalkTo(Button):
    pass
class Use(Button):
    pass
class Push(Button):
    pass
class Pull(Button):
    pass
class Up(Button):
    pass
class Down(Button):
    pass

class GUI(object):
    pass

class Inventory(pygame.sprite.Sprite):
    def __init__(self):
        super(Inventory, self).__init__()
        self.step = 0
        self.items = []
    def move_down(self):
        if self.step < len(self.player.inventory)-6:
            self.step = self.step + 3
    def move_up(self):
        if self.step > 0:
            self.step = self.step - 3
    def move_to_bottom(self):
        pass
    def move_to_top(self):
        pass
    def draw(self):
        j = 0
        p = [(320, 299), (400, 299), (480, 299), (320, 348), (400, 348), (480, 348)] 
        for name in self.player.inventory[self.j:]:
            self.screen.blit(self.items[name].image, p[j])
            if j == 5:
                break
            else:
                j = j+1


