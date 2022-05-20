import pygame
from GObject import GObject, Constants
from text import Text
from graph import Graph


class ControlPanel(GObject):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 300
        self.image = pygame.Surface((self.width, Constants.HEIGHT.value))
        self.image.set_alpha(100)
        self.image.fill(Constants.WHITE.value)
        self.rect = self.image.get_rect()
        self.rect.right = Constants.WIDTH.value
        self.rect.bottom = Constants.HEIGHT.value
        # GObject.all_objects.add(self)
        GObject.control_panel.add(self)

        self.population_graph = Graph(y=GObject.current_population_list, x=GObject.duration_list, size=(280, 100))
        self.population_graph.rect.center = (Constants.WIDTH.value - 150, 60)
        self.fps = Text(30)
        self.current_food = Text(30)
        self.total_food = Text(30)
        self.current_population = Text(30)
        self.total_born = Text(30)

    def update(self):
        pygame.display.get_surface().blit(self.image, (self.rect.x, self.rect.y))
        self.fps.update(f'Duration: {GObject.duration // 60}m or {GObject.duration // 3600}h',
                        (Constants.WIDTH.value - 150, Constants.HEIGHT.value - 180),
                        Constants.BLACK.value)
        self.fps.update(f'FPS: {GObject.fps}',
                        (Constants.WIDTH.value - 150, Constants.HEIGHT.value - 150),
                        Constants.BLACK.value)
        self.current_food.update(f'Current food: {len(GObject.food)}',
                                 (Constants.WIDTH.value - 150, Constants.HEIGHT.value - 120),
                                 Constants.BLACK.value)
        self.total_food.update(f'Total food: {GObject.cnt_of_food_ever}',
                               (Constants.WIDTH.value - 150, Constants.HEIGHT.value - 90),
                               Constants.BLACK.value)
        self.current_population.update(f'Current population: {len(GObject.cells)}',
                                       (Constants.WIDTH.value - 150, Constants.HEIGHT.value - 60),
                                       Constants.BLACK.value)
        self.total_born.update(f'Total born: {GObject.cnt_of_cells_ever}',
                               (Constants.WIDTH.value - 150, Constants.HEIGHT.value - 30),
                               Constants.BLACK.value)
        # pygame.display.get_surface().blit(self.population_graph.image, self.population_graph.rect.center)
        self.population_graph.update()

