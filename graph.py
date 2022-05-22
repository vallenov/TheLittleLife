import pygame
import math
from GObject import GObject, Constants
from text import Text


class Graph(GObject):
    def __init__(self, y: list, x: list, size: tuple):
        pygame.sprite.Sprite.__init__(self)
        self.x_list = x
        self.y_list = y
        self.size = size  # size of graph
        self.scale = 20
        self.color = Constants.BLACK.value
        self.part_size = self.size[0] // self.scale
        self.image = pygame.Surface(size, 5)
        self.image.fill(Constants.BLACK.value)
        self.rect = self.image.get_rect()
        self.center = tuple()
        # self.zero = Text(20)
        self.y_top_text = Text(20)

    @staticmethod
    def compress(lst):
        step = 10
        i = 0
        while len(lst) > step:
            step = step if step <= len(lst[i:]) else len(lst[i:]-1)
            lst[i] = math.ceil(sum(lst[i:step+i]) / len(lst[i:step+i]))
            for _ in range(step-1):
                lst.pop(i+1)
            i += 1
        return lst

    def update(self):
        if len(self.x_list) >= 100:
            self.x_list = self.compress(self.x_list)
            self.y_list = self.compress(self.y_list)
        pygame.draw.rect(pygame.display.get_surface(), Constants.BLACK.value, self, 1)
        self.y_top_text.update(str(max(self.y_list)), (self.rect.left - 5, self.rect.top - 10), Constants.BLACK.value)
        startxy = (self.rect.left, self.rect.bottom)
        percent = max(self.y_list)
        self.scale = len(self.x_list)
        self.part_size = self.size[0] / self.scale
        for part in range(self.scale):
            pygame.draw.line(pygame.display.get_surface(),
                             self.color,
                             startxy,
                             (self.rect.left + int((part+1)*self.part_size),
                              self.rect.bottom - (self.y_list[part] / percent) * self.size[1]), 3)
            startxy = (self.rect.left + int((part+1)*self.part_size),
                       self.rect.bottom - int((self.y_list[part] / percent) * self.size[1]))
