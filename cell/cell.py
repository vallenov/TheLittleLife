import pygame
import random
import datetime
from GObject import GObject, Constants
from text import Text
from TheLittleLife.cell.sight import Sight
from TheLittleLife.cell.genotype import Genotype


class Cell(GObject):

    def __init__(self, x=Constants.WIDTH.value // 2, y=Constants.HEIGHT.value // 2, genotype=None):
        pygame.sprite.Sprite.__init__(self)
        self.gen = Genotype() if not genotype else Genotype.transfer_genotype(genotype)
        self.dna = self.gen.dna
        print(self.gen)
        self.energy = 500
        self.size = self.dna['size']
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(self.dna['color'])
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.text = Text(20)
        self.sight = Sight(self.rect.x, self.rect.y, self.dna['sight_distance'])
        self.goal = None

        self.speed = self.rand_speed()

        self.position = pygame.math.Vector2(x, y)

    def rand_speed(self):
        return pygame.math.Vector2(random.choice([-1, 0, 1]) * self.size, random.choice([-1, 0, 1]) * self.size)

    def __repr__(self):
        dt = str(datetime.datetime.now()).split()[1]
        return f'{dt}'

    def born(self):
        new_life = Cell(x=self.rect.x, y=self.rect.y, genotype=self.gen)
        GObject.count_of_cells_ever += 1
        GObject.cells.add(new_life)
        GObject.all_objects.add(new_life)

    def die(self):
        GObject.all_objects.remove(self)
        GObject.cells.remove(self)
        del self

    def eat(self, food):
        if self.energy < self.dna['max_energy']:
            GObject.food.remove(food)
            GObject.all_objects.remove(food)
            self.energy += food.energy
            self.goal = None

    def check_energy(self):
        if self.energy <= 0:
            self.die()
        elif self.energy >= self.dna['born_energy']:
            self.born()
            self.energy -= self.dna['birth_losses']

    def next_step(self, goal):
        pos = pygame.math.Vector2(self.rect.center)
        goal_pos = pygame.math.Vector2(goal.rect.center)
        dist = goal_pos - pos
        if abs(dist.x) > self.size / 2 and abs(dist.y) > self.size / 2:
            self.speed.update(self.size if dist.x >= self.size / 2 else -self.size,
                              self.size if dist.y >= self.size / 2 else -self.size)
        elif abs(dist.x) > self.size / 2 > abs(dist.y):
            self.speed.update(self.size if dist.x > 0 else -self.size, 0)
        elif abs(dist.y) > self.size / 2 > abs(dist.x):
            self.speed.update(0, self.size if dist.y > 0 else -self.size)
        else:
            self.speed.update(self.size if dist.x > 0 else -self.size,
                              self.size if dist.y > 0 else -self.size)

    def update(self):
        self.energy -= 1
        self.check_energy()
        if not self.goal:
            for food in GObject.food:
                if self.sight.rect.colliderect(food.rect):
                    self.goal = food if self.goal is None else self.goal
                    break
            if not self.goal and random.randint(0, 100) < 5:
                self.speed = self.rand_speed()
        elif not self.sight.rect.colliderect(self.goal.rect):
            self.goal = None
        else:
            if self.rect.colliderect(self.goal.rect):
                self.eat(self.goal)
            else:
                self.next_step(self.goal)

        if self.rect.centerx >= Constants.WIDTH.value:
            self.position.x = self.size
        elif self.rect.centerx <= 0:
            self.position.x = Constants.WIDTH.value

        if self.rect.centery >= Constants.HEIGHT.value:
            self.position.y = self.size
        elif self.rect.centery <= 0:
            self.position.y = Constants.HEIGHT.value

        self.position += self.speed.x, self.speed.y
        self.rect.center = self.position.x, self.position.y

        pygame.display.get_surface().blit(self.image, (self.rect.x, self.rect.y))
        self.text.update(text=str(self.energy / 10), xy=(self.rect.x + 5, self.rect.y - 20),
                         color=Constants.WHITE.value)
        self.sight.update(self.rect.x - ((self.sight.size / 2) - (self.size / 2)),
                          self.rect.y - ((self.sight.size / 2) - (self.size / 2)))
