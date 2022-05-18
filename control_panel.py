import pygame
from GObject import GObject, Constants


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
        GObject.control_panel.add(self)
