import pygame
from GObject import GObject, Constants


class Text(GObject):
    def __init__(self, size: int):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.font = pygame.font.SysFont(pygame.font.match_font('arial'), self.size)
        self.text = ''
        self.angle = 0
        self.text_surface = self.font.render(str(self.text), True, Constants.BLACK.value)
        self.text_rect = self.text_surface.get_rect()

    def update(self, xy: tuple, color: tuple, text=''):
        self.text = text if text != '' else self.text
        self.text_surface = self.font.render(str(self.text), True, color)
        self.text_surface = pygame.transform.rotate(self.text_surface, self.angle)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.midtop = xy

    def draw(self):
        pygame.display.get_surface().blit(self.text_surface, self.text_rect)
