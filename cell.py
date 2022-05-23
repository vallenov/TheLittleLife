import pygame
import random
import datetime
from GObject import GObject, Constants
from text import Text


class Cell(GObject):

    def __init__(self, x=Constants.WIDTH.value // 2, y=Constants.HEIGHT.value // 2):
        pygame.sprite.Sprite.__init__(self)
        self.energy = 500
        self.size = 15
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(Constants.RED.value)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

        self.text = Text(20)
        self.sight = Sight(self.rect.x, self.rect.y)
        self.goal = None

        self.speedx = random.choice([-1, 1]) * self.size
        self.speedy = random.choice([-1, 1]) * self.size

    def __repr__(self):
        dt = str(datetime.datetime.now()).split()[1]
        return f'{dt}'

    def born(self):
        new_life = Cell(x=self.rect.x, y=self.rect.y)
        GObject.count_of_cells_ever += 1
        GObject.cells.add(new_life)
        GObject.all_objects.add(new_life)

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

    def next_step(self, goal):
        pos = pygame.math.Vector2(self.rect.center)
        goal_pos = pygame.math.Vector2(goal.rect.center)
        dist = goal_pos - pos
        if all(list(map(lambda q: abs(q) > self.size // 2, dist))):
            self.speedx = self.size if dist.x > 0 else -self.size
            self.speedy = self.size if dist.y > 0 else -self.size
        else:
            if dist.x <= self.size // 2:
                self.speedx = 0
                self.speedy = self.size if dist.y > self.size // 2 else -self.size
            elif dist.y <= self.size // 2:
                self.speedy = 0
                self.speedx = self.size if dist.x > self.size // 2 else -self.size

    def update(self):
        self.energy -= 1
        self.check_energy()
        if not self.goal:
            for food in GObject.food:
                if self.sight.rect.colliderect(food.rect):
                    self.goal = food if self.goal is None else self.goal
        elif not self.sight.rect.colliderect(self.goal.rect):
            self.goal = None
        else:
            if self.rect.colliderect(self.goal.rect):
                self.eat(self.goal, 100)
            else:
                self.next_step(self.goal)

        if self.rect.centerx >= Constants.WIDTH.value:
            self.rect.centerx = self.size
        elif self.rect.centerx <= 0:
            self.rect.centerx = Constants.WIDTH.value

        if self.rect.centery >= Constants.HEIGHT.value:
            self.rect.centery = self.size
        elif self.rect.centery <= 0:
            self.rect.centery = Constants.HEIGHT.value

        self.rect.centerx += self.speedx
        self.rect.centery += self.speedy

        pygame.display.get_surface().blit(self.image, (self.rect.x, self.rect.y))
        self.text.update(text=str(self.energy / 10), xy=(self.rect.x + 5, self.rect.y - 20), color=Constants.WHITE.value)
        self.sight.update(self.rect.x - ((self.sight.size / 2) - (self.size / 2)),
                          self.rect.y - ((self.sight.size / 2) - (self.size / 2)))


class Sight(GObject):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.size = 300
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
