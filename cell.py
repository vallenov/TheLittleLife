import pygame
import random
from TLLclasses import GObject, Constants
from text import Text


class Cell(GObject):

    def __init__(self, x=Constants.WIDTH.value // 2, y=Constants.HEIGHT.value // 2):
        pygame.sprite.Sprite.__init__(self)
        self.energy = 500
        self.size = 20
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(Constants.RED.value)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

        self.text = Text(str(self.energy), 20, (self.rect.x, self.rect.y))

        self.speedx = random.randint(-1, 1) * self.size
        self.speedy = random.randint(-1, 1) * self.size

    def born(self):
        new_life = Cell(x=self.rect.x, y=self.rect.y)
        GObject.cnt_of_cells_ever += 1
        GObject.cells.add(new_life)
        GObject.all_objects.add(new_life)
        print(f'Current population: {len(GObject.cells)}')
        print(f'Total born: {GObject.cnt_of_cells_ever}')

    def die(self):
        GObject.all_objects.remove(self)
        GObject.cells.remove(self)
        del self

    def eat(self, food, energy):
        if self.energy < 1000:
            GObject.food.remove(food)
            GObject.all_objects.remove(food)
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
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.text.update(str(self.energy // 10), (self.rect.x + 10, self.rect.y - 20))
