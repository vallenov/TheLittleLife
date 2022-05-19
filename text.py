import pygame
from GObject import GObject, Constants
#from TLL import Game


class Text(GObject):
    def __init__(self, size: int):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont(pygame.font.match_font('arial'), size)

    def update(self, text, xy: tuple, color: tuple):
        text_surface = self.font.render(str(text), True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = xy
        pygame.display.get_surface().blit(text_surface, text_rect)
