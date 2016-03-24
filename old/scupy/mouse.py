import pygame
from geometry import Point2D

class Mouse(object):

    def __init__(self, filename=None):
        if filename:
            self.set_cursor(filename)
        else:
            self.image = pygame.mouse.get_cursor()

    def get_pos(self):
        return pygame.mouse.get_pos()

    def set_cursor(self, filename):
        pygame.mouse.set_visible(False)
        self.image = pygame.image.load(filename).convert_alpha()

    def set_pos(self, position):
        pygame.mouse.set_pos(position)


