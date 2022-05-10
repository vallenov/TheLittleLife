import pygame
import random

from TLLclasses import Constants, Object, Cell, Food, Wall


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((Constants.WIDTH.value, Constants.HEIGHT.value))
        pygame.display.set_caption("TheLittleLife")
        self.clock = pygame.time.Clock()

        self.font_name = pygame.font.match_font('arial')

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

    def draw_text(self, surf, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, Constants.WHITE.value)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    def run(self):
        # walls_generate()
        running = True
        for _ in range(10):
            self.spawn()
        while running:
            # Держим цикл на правильной скорости
            self.clock.tick(Constants.FPS.value)
            # Ввод процесса (события)
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    running = False
            for cell in Object.cells:
                self.draw_text(self.screen, 'AAAAAAAAAAAAAAA', 10, cell.rect.centerx,
                               cell.rect.bottom - cell.size - 2)
                for ind, f in enumerate(Object.food):
                    if cell.rect.colliderect(f.rect):
                        cell.eat(f, 100)

            if len(Object.food.sprites()) < 500:
                self.new_food()

            Object.all_objects.update()

            # Рендеринг
            self.screen.fill(Constants.GREEN.value)
            Object.all_objects.draw(self.screen)


            #self.draw_text(self.screen, 'LL', 10, LittleLife.rect.centerx, LittleLife.rect.bottom - LittleLife.size-2)

            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
