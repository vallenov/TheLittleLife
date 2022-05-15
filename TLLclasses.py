import pygame
import enum
import random


class Constants(enum.Enum):
    HEIGHT = 900  # высота мира
    WIDTH = 1500  # ширина мира

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 100)
    GREEN = (50, 100, 50)
    BLUE = (0, 0, 255)
    YELLOW = (100, 100, 0)


class GObject(pygame.sprite.Sprite):
    all_objects = pygame.sprite.Group()
    cells = pygame.sprite.Group()
    food = pygame.sprite.Group()
    walls = pygame.sprite.Group()

    cnt_of_cells_ever = 0
    screen = pygame.display.set_mode((Constants.WIDTH.value, Constants.HEIGHT.value))

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
