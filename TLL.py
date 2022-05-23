import pygame
import random
from GObject import GObject, Constants
from wall import Wall
from cell import Cell
from food import Food
from control_panel import ControlPanel


class Game:
    pygame.init()
    pygame.mixer.init()

    pygame.display.set_caption("TheLittleLife")
    clock = pygame.time.Clock()

    font_name = pygame.font.match_font('arial')

    screen = pygame.display.set_mode((Constants.WIDTH.value, Constants.HEIGHT.value))

    FPS = 1

    work_time = 0
    food_respawn = 20

    @staticmethod
    def walls_generate():
        for _ in range(random.randint(20, 100)):
            w = Wall()
            # GObject.all_objects.add(w)
            GObject.walls.add(w)

    @staticmethod
    def spawn():
        new_life = Cell()
        GObject.cells.add(new_life)
        # GObject.all_objects.add(new_life)

    @staticmethod
    def new_food():
        f = Food(energy=random.randint(50, 150))
        # GObject.all_objects.add(f)
        GObject.food.add(f)
        GObject.count_of_food_ever += 1

    def run(self):
        control_panel = ControlPanel()
        # self.walls_generate()
        running = True
        for _ in range(1):
            self.spawn()
        for _ in range(500):
            self.new_food()
        while running:
            self.clock.tick(self.FPS)
            if not GObject.cells:
                GObject.count_of_extinction += 1
                self.spawn()
            if not (Game.work_time % 60):
                GObject.duration_cell_list.append(Game.work_time)
                GObject.current_population_list.append(len(GObject.cells))
                GObject.duration_food_list.append(Game.work_time)
                GObject.current_food_list.append(len(GObject.food))
            if not (Game.work_time % Game.food_respawn):
                self.new_food()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        if self.FPS < 10:
                            self.FPS += 1
                        elif 10 <= self.FPS < 200:
                            self.FPS += 5
                    if event.button == 5:
                        if self.FPS > 10:
                            self.FPS -= 10
                        elif 1 < self.FPS <= 10:
                            self.FPS -= 1
                        elif self.FPS <= 0:
                            self.FPS = 1

            # while len(GObject.food.sprites()) < 500:
            #         self.new_food()
            Game.screen.fill(Constants.GREEN.value)

            GObject.food.draw(Game.screen)

            GObject.cells.update()
            GObject.control_panel.update()
            # GObject.all_objects.update()

            # Рендеринг
            pygame.display.flip()

            Game.work_time += Game.FPS
            GObject.fps = self.FPS
            GObject.duration = Game.work_time // Game.FPS

        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
