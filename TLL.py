import pygame
import random

from TLLclasses import Constants, LL, Food, Smell, Wall

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((Constants.WIDTH.value, Constants.HEIGHT.value))
pygame.display.set_caption("TheLittleLife")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')

all_sprites = pygame.sprite.Group()
food = pygame.sprite.Group()
walls = pygame.sprite.Group()

LittleLife = LL()
all_sprites.add(LittleLife)


def walls_generate():
    for _ in range(random.randint(20, 100)):
        w = Wall()
        all_sprites.add(w)
        walls.add(w)


def new_food():
    f = Food()
    all_sprites.add(f)
    food.add(f)


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, Constants.WHITE.value)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


walls_generate()

running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(Constants.FPS.value)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    if len(food.sprites()) // 2 < 2:
        new_food()

    all_sprites.update()

    # Рендеринг
    screen.fill(Constants.GREEN.value)
    all_sprites.draw(screen)

    #draw_text(screen, 'LL', 10, LittleLife.rect.centerx, LittleLife.rect.bottom - LittleLife.size-2)

    pygame.display.flip()

pygame.quit()