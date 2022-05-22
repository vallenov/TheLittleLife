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
        self.color = Constants.BLACK.value  # line color
        self.part_size = self.size[0] // self.scale
        self.image = pygame.Surface(size, 5)
        self.image.fill(Constants.BLACK.value)
        self.rect = self.image.get_rect()
        self.y_top_text = Text(20)  # print max(self.y_list) on the left-top edge
        self.x_bottom_text = Text(20)  # print last element self.x_list on the right-bottom edge
        self.y_last_value = Text(20)
        self.xlabel = Text(20)  # name of x axis
        self.ylabel = Text(20)  # name of y axis
        self.compress = True

    @staticmethod
    def _compress(lst):
        step = 2
        finaly_len = len(lst) // step
        i = 0
        while len(lst) > finaly_len:
            step = step if step <= len(lst[i:]) else len(lst[i:])
            if max(lst) in lst[i:step + i]:
                lst[i] = max(lst)
            elif min(lst) in lst[i:step + i]:
                lst[i] = min(lst)
            else:
                lst[i] = math.ceil(sum(lst[i:step + i]) / len(lst[i:step + i]))
            for _ in range(step - 1):
                lst.pop(i + 1)
            i += 1
        return lst

    def update(self):
        if self.compress and len(self.x_list) >= 30:
            self.x_list = self._compress(self.x_list)
            self.y_list = self._compress(self.y_list)
        pygame.draw.rect(pygame.display.get_surface(), Constants.BLACK.value, self, 1)
        self.y_top_text.update(text=str(max(self.y_list)),
                               xy=(self.rect.left, self.rect.top - 15),
                               color=Constants.BLACK.value)
        self.x_bottom_text.update(text=str(self.x_list[-1]),
                                  xy=(self.rect.right, self.rect.bottom + 5),
                                  color=Constants.BLACK.value)
        self.ylabel.update(xy=(self.rect.centerx, self.rect.top - 15), color=Constants.BLACK.value)
        self.xlabel.update(xy=(self.rect.centerx, self.rect.bottom + 5), color=Constants.BLACK.value)
        startxy = (self.rect.left, self.rect.bottom)
        percent = max(self.y_list) if max(self.y_list) > 0 else 1
        self.scale = len(self.x_list)
        self.part_size = self.size[0] / self.scale
        for part in range(self.scale):
            pygame.draw.line(pygame.display.get_surface(),
                             self.color,
                             startxy,
                             (self.rect.left + int((part + 1) * self.part_size),
                              self.rect.bottom - (self.y_list[part] / percent) * self.size[1]), 2)
            startxy = (self.rect.left + int((part + 1) * self.part_size),
                       self.rect.bottom - int((self.y_list[part] / percent) * self.size[1]))
        self.y_last_value.update(text=str(self.y_list[-1]),
                           xy=(self.rect.right + 10, startxy[1] - 5),
                           color=Constants.BLACK.value)
