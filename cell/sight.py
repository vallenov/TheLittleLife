import pygame
from GObject import GObject, Constants


class Sight(GObject):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = pygame.Surface((self.size, self.size))
        self.image.set_alpha(0)
        self.image.fill(Constants.YELLOW.value)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

    def update(self, x, y):
        self.rect.x = x
        self.rect.y = y
        pygame.display.get_surface().blit(self.image, (x, y))