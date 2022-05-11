import pygame
import enum
import random


class Constants(enum.Enum):
    HEIGHT = 900  # высота мира
    WIDTH = 1500  # ширина мира
    FPS = 5

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 100)
    GREEN = (50, 100, 50)
    BLUE = (0, 0, 255)
    YELLOW = (100, 100, 0)


class Game:
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((Constants.WIDTH.value, Constants.HEIGHT.value))
    pygame.display.set_caption("TheLittleLife")
    clock = pygame.time.Clock()

    font_name = pygame.font.match_font('arial')

    @staticmethod
    def walls_generate():
        for _ in range(random.randint(20, 100)):
            w = Wall()
            Object.all_objects.add(w)
            Object.walls.add(w)

    @staticmethod
    def spawn():
        new_life = Cell()
        Object.cells.add(new_life)
        Object.all_objects.add(new_life)

    @staticmethod
    def new_food():
        f = Food()
        Object.all_objects.add(f)
        Object.food.add(f)

    def run(self):
        # walls_generate()
        running = True
        for _ in range(10):
            self.spawn()
        while running:
            self.screen.fill(Constants.GREEN.value)
            Object.all_objects.update()
            # Держим цикл на правильной скорости
            self.clock.tick(Constants.FPS.value)
            # Ввод процесса (события)
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    running = False
            for cell in Object.cells:
                for ind, f in enumerate(Object.food):
                    if cell.rect.colliderect(f.rect):
                        cell.eat(f, 100)
                # self.draw_text(self.screen, str(cell.energy), 30, cell.rect.centerx,
                #                cell.rect.bottom - cell.size - 2)

            if len(Object.food.sprites()) < 500:
                self.new_food()

            # Рендеринг
            Object.all_objects.draw(self.screen)

            pygame.display.flip()

        pygame.quit()


class Object(pygame.sprite.Sprite):
    all_objects = pygame.sprite.Group()
    cells = pygame.sprite.Group()
    food = pygame.sprite.Group()
    walls = pygame.sprite.Group()

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Text(Object):
    def __init__(self, text: str, size: int, xy: tuple):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont(Game.font_name, size)
        self.text_surface = self.font.render(text, True, Constants.WHITE.value)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.midtop = xy

    def update(self, text, xy: tuple):
        self.text_surface = self.font.render(text, True, Constants.WHITE.value)
        self.text_rect.midtop = xy
        Game.screen.blit(self.text_surface, self.text_rect)

class Cell(Object):

    def __init__(self, x=Constants.WIDTH.value // 2, y=Constants.HEIGHT.value // 2):
        pygame.sprite.Sprite.__init__(self)
        self.energy = 500
        self.size = 20
        # self.font = pygame.font.Font(self.font_name)
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(Constants.RED.value)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

        self.text = Text(str(self.energy), 20, (self.rect.x, self.rect.y))

        self.speedx = random.randint(-1, 1) * self.size
        self.speedy = random.randint(-1, 1) * self.size

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
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.text.update(str(self.energy // 10), (self.rect.x + 10, self.rect.y - 20))


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
