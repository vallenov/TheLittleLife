import pygame
import enum


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
    control_panel = pygame.sprite.Group()

    count_of_extinction = 0

    count_of_cells_ever = 0
    count_of_food_ever = 0
    fps = 0
    duration = 0
    current_population_list = []
    current_food_list = []
    duration_cell_list = []
    duration_food_list = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
