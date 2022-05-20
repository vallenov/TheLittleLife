import pygame
from GObject import GObject, Constants
from text import Text


class Graph(GObject):
    def __init__(self, y: list, x: list, size: tuple):
        pygame.sprite.Sprite.__init__(self)
        self.x_list = x
        self.y_list = y
        self.size = size
        self.image = pygame.Surface(size, 5)
        self.image.fill(Constants.BLACK.value)
        self.rect = self.image.get_rect()
        self.center = tuple()
        self.zero = Text(20)
        self.y_top_text = Text(20)

    def update(self):
        pygame.draw.rect(pygame.display.get_surface(), Constants.BLACK.value, self, 1)
        self.zero.update('0', (self.rect.left, self.rect.bottom), Constants.BLACK.value)
        self.zero.update(str(max(self.y_list)), (self.rect.left - 5, self.rect.top - 10), Constants.BLACK.value)
