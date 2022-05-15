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
        self.sight = Sight(self.rect.x, self.rect.y)
        self.goal = None

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
            self.goal = None

    def check_energy(self):
        if self.energy <= 0:
            self.die()
        elif self.energy >= 1000:
            self.born()
            self.energy -= 700

# 00 01 02 03
# 10 11 12 13
# 20 21 22 23
# 30 31 32 33

    def update(self):
        self.energy -= 1
        self.check_energy()
        if not self.goal:
            for food in GObject.food:
                if self.sight.rect.colliderect(food.rect):
                    print('foooood')
                    self.goal = food if self.goal is None else self.goal
                    print((self.rect.x, self.rect.y), (self.goal.rect.x, self.goal.rect.y))
                    print((self.rect.x - self.goal.rect.x, self.rect.y - self.goal.rect.y))
        else:
            print((self.rect.x, self.rect.y), (self.goal.rect.x, self.goal.rect.y))
            print((self.rect.x - self.goal.rect.x, self.rect.y - self.goal.rect.y))
            if self.rect.colliderect(self.goal.rect):
                self.eat(self.goal, 100)
            if -(self.size / 2) <= self.rect.x - self.goal.rect.x <= self.size / 2:
                self.speedx = 0 if self.speedy else self.speedx
            elif self.rect.x - self.goal.rect.x <= -(self.size / 2):
                self.speedx = self.size
                self.speedx = +self.speedx
            elif self.rect.x - self.goal.rect.x >= self.size / 2:
                self.speedx = self.size
                self.speedx = -self.speedx
            if -(self.size / 2) <= self.rect.y - self.goal.rect.y <= self.size / 2:
                self.speedy = 0 if self.speedx else self.speedy
            elif self.rect.y - self.goal.rect.y <= -(self.size / 2):
                self.speedy = self.size
                self.speedy = +self.speedy
            elif self.rect.y - self.goal.rect.y >= self.size / 2:
                self.speedy = self.size
                self.speedy = -self.speedy
        self.speedx = -self.speedx if Constants.WIDTH.value <= self.rect.x or self.rect.x <= 0 else self.speedx
        self.speedy = -self.speedy if Constants.HEIGHT.value <= self.rect.y or self.rect.y <= 0 else self.speedy
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.text.update(str(self.energy // 10), (self.rect.x + 10, self.rect.y - 20))
        self.sight.update(self.rect.x - ((self.sight.size / 2) - (self.size / 2)),
                          self.rect.y - ((self.sight.size / 2) - (self.size / 2)))


class Sight(GObject):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.size = 150
        self.image = pygame.Surface((self.size, self.size))
        self.image.set_alpha(128)
        self.image.fill(Constants.YELLOW.value)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

    def update(self, x, y):
        self.rect.x = x
        self.rect.y = y
        GObject.screen.blit(self.image, (x, y))
