import pygame
import random

from TLLclasses import Constants, LL, Food, Wall


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((Constants.WIDTH.value, Constants.HEIGHT.value))
        pygame.display.set_caption("TheLittleLife")
        self.clock = pygame.time.Clock()

        self.font_name = pygame.font.match_font('arial')

        self.cells = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.food = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

    def born(self):
        new_life = LL()
        self.cells.add(new_life)
        self.all_sprites.add(new_life)

    def walls_generate(self):
        for _ in range(random.randint(20, 100)):
            w = Wall()
            self.all_sprites.add(w)
            self.walls.add(w)

    def new_food(self):
        f = Food()
        self.all_sprites.add(f)
        self.food.add(f)

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
            self.born()
        while running:
            # Держим цикл на правильной скорости
            self.clock.tick(Constants.FPS.value)
            # Ввод процесса (события)
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    running = False
            for cell in self.cells:
                for ind, f in enumerate(self.food):
                    if cell.rect.colliderect(f.rect):
                        self.food.remove(f)
                        self.all_sprites.remove(f)
                        del f
                        cell.eat(10)

            if len(self.food.sprites()) < 500:
                self.new_food()

            self.all_sprites.update()

            # Рендеринг
            self.screen.fill(Constants.GREEN.value)
            self.all_sprites.draw(self.screen)

            #draw_text(screen, 'LL', 10, LittleLife.rect.centerx, LittleLife.rect.bottom - LittleLife.size-2)

            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
