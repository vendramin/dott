import pygame
from pygame.locals import *
 
class Font:
    def __init__(self, filename, size):
        self.font = pygame.font.Font(filename, size) 
 
    def write(self, surface, x, y, text, color, antialias=False):
        font_surf = self.font.render(text, antialias, color)
        font_rect = font_surf.get_rect()
        font_rect.x = x
        font_rect.y = y
        surface.blit(font_surf, font_rect)

