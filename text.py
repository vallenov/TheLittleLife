import pygame
import random
from GObject import GObject, Constants
#from TLL import Game


class Text(GObject):
    def __init__(self, text: str, size: int, xy: tuple):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont(pygame.font.match_font('arial'), size)
        self.text_surface = self.font.render(text, True, Constants.WHITE.value)
        self.text_rect = self.text_surface.get_rect()

    def update(self, text, xy: tuple):
        self.text_surface = self.font.render(text, True, Constants.WHITE.value)
        self.text_rect.midtop = xy
        pygame.display.get_surface().blit(self.text_surface, self.text_rect)
