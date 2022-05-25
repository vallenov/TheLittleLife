import pygame
from GObject import GObject, Constants


class Text(GObject):
    def __init__(self, size: int):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.font = pygame.font.SysFont(pygame.font.match_font('arial'), self.size)
        self.text = ''
        self.angle = 0

    def update(self, xy: tuple, color: tuple, text=''):
        text = self.text if self.text != '' else text
        text_surface = self.font.render(str(text), True, color)
        text_surface = pygame.transform.rotate(text_surface, self.angle)
        text_rect = text_surface.get_rect()
        text_rect.midtop = xy
        pygame.display.get_surface().blit(text_surface, text_rect)
