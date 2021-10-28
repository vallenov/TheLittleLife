import pygame
import enum
import random

class constants(enum.Enum):
    HEIGHT = 500  # высота мира
    WIDTH = 1000  # ширина мира
    FPS = 30

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 100)
    GREEN = (50, 100, 50)
    BLUE = (0, 0, 255)
    YELLOW = (100, 100, 0)

class LL(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = 10
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(constants.GREEN.value)
        self.rect = self.image.get_rect()
        self.rect.centerx = constants.WIDTH.value // 2
        self.rect.bottom = constants.HEIGHT.value // 2
        pygame.draw.circle(self.image,
                           constants.RED.value,
                           (self.size // 2, self.size // 2), self.size // 2)

        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.rect.x += random.randint(-1,1)
        self.rect.y += random.randint(-1,1)

class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = 4
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(constants.GREEN.value)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(2, constants.WIDTH.value -1)
        self.rect.bottom = random.randint(2, constants.HEIGHT.value  -1)
        pygame.draw.circle(self.image,
                           constants.BLUE.value,
                           (self.size // 2, self.size // 2), self.size // 2)

class Smell(pygame.sprite.Sprite):
    def __init__(self, x, y, sz):
        pygame.sprite.Sprite.__init__(self)
        self.size = 80
        #self.maxsize = 70
        self.image = pygame.Surface((self.size, self.size))
        self.image.set_alpha(128)
        self.image.fill(constants.GREEN.value)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y + (self.size // 2 - sz)
        pygame.draw.circle(self.image,
                           constants.YELLOW.value,
                           (self.size // 2, self.size // 2), self.size // 2)

class Wall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = 20
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(constants.BLACK.value)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(2, constants.WIDTH.value -1)
        self.rect.bottom = random.randint(2, constants.HEIGHT.value  -1)