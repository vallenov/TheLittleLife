import pygame
import enum
import random


class Constants(enum.Enum):
    HEIGHT = 900  # высота мира
    WIDTH = 1500  # ширина мира
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
        self.energy = 50
        self.size = 10
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(Constants.RED.value)
        self.rect = self.image.get_rect()
        self.rect.centerx = Constants.WIDTH.value // 2
        self.rect.bottom = Constants.HEIGHT.value // 2

        self.speedx = random.randint(-1, 1)
        self.speedy = random.randint(-1, 1)

    def eat(self, energy):
        self.energy += energy

    def update(self):
        self.speedx = -self.speedx if Constants.WIDTH.value < self.rect.x or self.rect.x < 0 else self.speedx
        self.speedy = -self.speedy if Constants.HEIGHT.value < self.rect.y or self.rect.y < 0 else self.speedy
        self.rect.x += self.speedx # random.randint(-1, 1)
        self.rect.y += self.speedy # random.randint(-1, 1)


class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = 4
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(Constants.BLUE.value)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(2, Constants.WIDTH.value - 1)
        self.rect.bottom = random.randint(2, Constants.HEIGHT.value - 1)


class Smell(pygame.sprite.Sprite):
    def __init__(self, x, y, sz):
        pygame.sprite.Sprite.__init__(self)
        self.size = 2
        self.maxsize = 80
        self.image = pygame.Surface((self.size, self.size))
        self.image.set_alpha(128)
        self.image.fill(Constants.GREEN.value)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y + (self.size // 2 - sz)
        pygame.draw.circle(self.image,
                           Constants.YELLOW.value,
                           (self.size // 2, self.size // 2), self.size // 2)

    def update(self):
        if self.size < self.maxsize:
            self.size += 2
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
            self.image.fill(Constants.GREEN.value)
            pygame.draw.circle(self.image,
                               Constants.YELLOW.value,
                               (self.size // 2, self.size // 2), self.size // 2)
            self.rect.centerx -= self.size / self.maxsize
            self.rect.bottom -= self.size / self.maxsize


class Wall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = 20
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(Constants.BLACK.value)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(2, Constants.WIDTH.value - 1)
        self.rect.bottom = random.randint(2, Constants.HEIGHT.value - 1)
