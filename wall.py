import pygame
import random
from GObject import GObject, Constants


class Wall(GObject):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = 20
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(Constants.BLACK.value)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(2, Constants.WIDTH.value - 1)
        self.rect.bottom = random.randint(2, Constants.HEIGHT.value - 1)
