import pygame
import enum
import random


class Constants(enum.Enum):
    HEIGHT = 900  # высота мира
    WIDTH = 1500  # ширина мира
    FPS = 1500

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 100)
    GREEN = (50, 100, 50)
    BLUE = (0, 0, 255)
    YELLOW = (100, 100, 0)


class Object(pygame.sprite.Sprite):
    all_objects = pygame.sprite.Group()
    cells = pygame.sprite.Group()
    food = pygame.sprite.Group()
    walls = pygame.sprite.Group()

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Cell(Object):

    def __init__(self, x=Constants.WIDTH.value // 2, y=Constants.HEIGHT.value // 2):
        pygame.sprite.Sprite.__init__(self)
        self.energy = 500
        self.size = 20
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(Constants.RED.value)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

        self.speedx = random.randint(-1, 1)
        self.speedy = random.randint(-1, 1)

    def born(self):
        print(len(Object.cells))
        new_life = Cell(x=self.rect.x, y=self.rect.y)
        Object.cells.add(new_life)
        Object.all_objects.add(new_life)

    def die(self):
        Object.all_objects.remove(self)
        Object.cells.remove(self)
        del self

    def eat(self, food, energy):
        Object.food.remove(food)
        Object.all_objects.remove(food)
        self.energy += energy

    def check_energy(self):
        if self.energy <= 0:
            self.die()
        elif self.energy >= 1000:
            self.born()
            self.energy -= 700

    def update(self):
        self.energy -= 1
        self.check_energy()
        self.speedx = -self.speedx if Constants.WIDTH.value < self.rect.x or self.rect.x < 0 else self.speedx
        self.speedy = -self.speedy if Constants.HEIGHT.value < self.rect.y or self.rect.y < 0 else self.speedy
        self.rect.x += self.speedx # random.randint(-1, 1)
        self.rect.y += self.speedy # random.randint(-1, 1)


class Food(Object):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = 4
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(Constants.BLACK.value)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(2, Constants.WIDTH.value - 1)
        self.rect.bottom = random.randint(2, Constants.HEIGHT.value - 1)


class Smell(Object):
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


class Wall(Object):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = 20
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(Constants.BLACK.value)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(2, Constants.WIDTH.value - 1)
        self.rect.bottom = random.randint(2, Constants.HEIGHT.value - 1)
