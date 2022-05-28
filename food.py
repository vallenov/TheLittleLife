import pygame
import random
import datetime
from GObject import GObject, Constants


class Food(GObject):
    def __init__(self, energy):
        pygame.sprite.Sprite.__init__(self)
        self.size = 5
        self.energy = energy
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(Constants.BLUE.value)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(2, Constants.WIDTH.value - 1)
        self.rect.bottom = random.randint(2, Constants.HEIGHT.value - 1)
