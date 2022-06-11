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

        self.population_graph = Graph(y=GObject.current_population_list,
                                      x=GObject.duration_cell_list,
                                      size=(250, 150))
        self.population_graph.rect.centerx, self.population_graph.rect.top = (Constants.WIDTH.value - 150, 20)
        self.population_graph.color = Constants.RED.value
        self.population_graph.xlabel.text = 'Frames'
        self.population_graph.ylabel.text = 'Count of cells'

        self.current_food_graph = Graph(y=GObject.current_food_list,
                                        x=GObject.duration_food_list,
                                        size=(250, 150))
        self.current_food_graph.rect.centerx = Constants.WIDTH.value - 150
        self.current_food_graph.rect.top = self.population_graph.rect.bottom + 40
        self.current_food_graph.color = Constants.BLUE.value
        self.current_food_graph.xlabel.text = 'Frames'
        self.current_food_graph.ylabel.text = 'Count of food'

        self.count_of_extinction = Text(30)
        self.fps = Text(30)
        self.duration = Text(30)
        self.current_food = Text(30)
        self.total_food = Text(30)
        self.current_population = Text(30)
        self.total_born = Text(30)

    def update(self):
        self.count_of_extinction.update(text=f'Count of extinction: {GObject.count_of_extinction}',
                               xy=(Constants.WIDTH.value - 150, Constants.HEIGHT.value - 210),
                               color=Constants.BLACK.value)
        self.duration.update(text=f'Duration: {GObject.duration // 60}m or {GObject.duration // 3600}h',
                        xy=(Constants.WIDTH.value - 150, Constants.HEIGHT.value - 180),
                        color=Constants.BLACK.value)
        self.fps.update(text=f'FPS: {GObject.fps}',
                        xy=(Constants.WIDTH.value - 150, Constants.HEIGHT.value - 150),
                        color=Constants.BLACK.value)
        self.current_food.update(text=f'Current food: {len(GObject.food)}',
                                 xy=(Constants.WIDTH.value - 150, Constants.HEIGHT.value - 120),
                                 color=Constants.BLACK.value)
        self.total_food.update(text=f'Total food: {GObject.count_of_food_ever}',
                               xy=(Constants.WIDTH.value - 150, Constants.HEIGHT.value - 90),
                               color=Constants.BLACK.value)
        self.current_population.update(text=f'Current population: {len(GObject.cells)}',
                                       xy=(Constants.WIDTH.value - 150, Constants.HEIGHT.value - 60),
                                       color=Constants.BLACK.value)
        self.total_born.update(text=f'Total born: {GObject.count_of_cells_ever}',
                               xy=(Constants.WIDTH.value - 150, Constants.HEIGHT.value - 30),
                               color=Constants.BLACK.value)
        self.population_graph.update()
        self.current_food_graph.update()

    def draw(self):
        pygame.display.get_surface().blit(self.image, (self.rect.x, self.rect.y))
        self.count_of_extinction.draw()
        self.duration.draw()
        self.fps.draw()
        self.current_food.draw()
        self.total_food.draw()
        self.current_population.draw()
        self.total_born.draw()
        self.population_graph.draw()
        self.current_food_graph.draw()
