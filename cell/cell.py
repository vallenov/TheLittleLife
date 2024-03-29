import pygame
import random
import datetime
from GObject import GObject, Constants
from text import Text
from TheLittleLife.cell.sight import Sight
from TheLittleLife.cell.genotype import Genotype


class Cell(GObject):

    def __init__(self, x=None, y=None, genotype=None):
        pygame.sprite.Sprite.__init__(self)
        self.genotype = Genotype() if genotype is None else Genotype.transfer_genotype(genotype)
        self.dna = self.genotype.dna
        self.energy = self.dna['start_energy'].value
        self.size = self.dna['size'].value
        self.speed = self.dna['speed'].value
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(self.dna['color'].value)
        self.rect = self.image.get_rect()
        self.rect.centerx = x if x else random.randint(10, Constants.WIDTH.value - 10)
        self.rect.centery = y if y else random.randint(10, Constants.HEIGHT.value - 10)

        self.text = Text(20)
        self.sight = Sight(self.rect.x, self.rect.y, self.dna['sight_distance'].value)
        self.goal = None

        self.direction = self.rand_direction()

        self.position = pygame.math.Vector2(self.rect.centerx, self.rect.centery)

    def rand_direction(self):
        return pygame.math.Vector2(random.choice([-1, 0, 1]) * self.speed,
                                   random.choice([-1, 0, 1]) * self.speed)

    def __repr__(self):
        dt = str(datetime.datetime.now()).split()[1]
        return f'{dt}'

    @property
    def hungry(self):
        return True if self.energy < self.dna['max_energy'].value else False

    @property
    def ready_to_born(self):
        return True if self.energy >= self.dna['energy_for_born'].value else False

    def born(self):
        new_life = Cell(x=self.rect.x, y=self.rect.y, genotype=self.genotype)
        print(self.genotype)
        GObject.count_of_cells_ever += 1
        GObject.cells.add(new_life)
        GObject.all_objects.add(new_life)
        self.energy -= self.dna['birth_losses'].value

    def die(self):
        GObject.all_objects.remove(self)
        GObject.cells.remove(self)
        del self

    def eat(self, food):
        if self.hungry:
            GObject.food.remove(food)
            GObject.all_objects.remove(food)
            self.energy += food.energy
            self.goal = None
            del food

    def kill_cell(self, cell):
        if abs((sum(cell.dna['color'].value) / 3) - (sum(self.dna['color'].value) / 3)) > 10 and self.hungry:
            if self.dna['anger'].value > cell.dna['anger'].value and not cell.is_run():
                self.energy += cell.energy // 5
                cell.die()

    def is_run(self):
        return True if random.randint(0, 100) in range(self.dna['run_chance'].value) else False

    def check_energy(self):
        if self.energy <= 0:
            self.die()
        elif self.ready_to_born:
            self.born()

    def next_step(self, goal):
        pos = pygame.math.Vector2(self.rect.center)
        goal_pos = pygame.math.Vector2(goal.rect.center)
        dist = goal_pos - pos
        if abs(dist.x) > self.size / 2 and abs(dist.y) > self.size / 2:
            self.direction.update(self.speed if dist.x >= self.size / 2 else -self.speed,
                                  self.speed if dist.y >= self.size / 2 else -self.speed)
        elif abs(dist.x) > self.size / 2 > abs(dist.y):
            self.direction.update(self.speed if dist.x > 0 else -self.speed, 0)
        elif abs(dist.y) > self.size / 2 > abs(dist.x):
            self.direction.update(0, self.speed if dist.y > 0 else -self.speed)
        else:
            self.direction.update(self.speed if dist.x > 0 else -self.speed,
                                  self.speed if dist.y > 0 else -self.speed)

    def update(self):
        self.energy -= self.size // 10
        self.check_energy()
        for cell in GObject.cells:
            if self != cell and self.rect.colliderect(cell.rect):
                self.kill_cell(cell)
        if not self.goal:
            for food in GObject.food:
                if self.sight.rect.colliderect(food.rect):
                    self.goal = food if self.goal is None else self.goal
                    break
            if not self.goal and random.randint(0, 100) < 5:
                self.direction = self.rand_direction()
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

        self.position += self.direction.x, self.direction.y
        self.rect.center = self.position.x, self.position.y
        self.text.update(text=str(self.energy / 10), xy=(self.rect.x + 5, self.rect.y - 20),
                         color=Constants.WHITE.value)
        self.sight.update(self.rect.x - ((self.sight.size / 2) - (self.size / 2)),
                          self.rect.y - ((self.sight.size / 2) - (self.size / 2)))

    def draw(self):
        pygame.display.get_surface().blit(self.image, (self.rect.x, self.rect.y))
        self.sight.draw()
        self.text.draw()
