from scupy.item import Item
from scupy.config import *

class Textbook(Item):
    def __init__(self):
        super(Textbook, self).__init__('textbook')
        self.set_image('items/textbook.png')
        self.description = 'textbook'


