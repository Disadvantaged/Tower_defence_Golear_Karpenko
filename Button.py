import os

import pygame

import config
from Rectangle import Rectangle


class Button(Rectangle):
    def __init__(self, position, image=None, groups=None):
        img = os.path.join(config.BUTTON_PATH, image)
        super().__init__(position, (config.BUTTON_WIDTH, config.BUTTON_HEIGHT), img, groups)

    def action(self, pos):
        raise NotImplementedError


class ExitButton(Button):
    def __init__(self, position, groups=None):
        super().__init__(position, 'quit.png', groups=groups)

    def action(self, pos):
        pygame.quit()
        exit()
