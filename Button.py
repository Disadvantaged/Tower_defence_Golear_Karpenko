import os

import pygame

import config
from Rectangle import Rectangle


class Button(Rectangle):
    def __init__(self, position=None, image=None, groups=None):
        if image is not None:
            image = os.path.join(config.BUTTON_PATH, image)
        super().__init__(position, (config.BUTTON_WIDTH, config.BUTTON_HEIGHT), image, groups)

    def action(self, pos):
        raise NotImplementedError


class ExitButton(Button):
    def __init__(self, position):
        super().__init__(position, 'quit.png')

    def action(self, pos):
        pygame.quit()
        exit()


class NewWaveButton(Button):
    def __init__(self, position, groups=None):
        super().__init__(position, 'nextWave.png', groups=groups)

    def action(self, pos):
        pass


class PlayButton(Button):
    def __init__(self, position, groups=None):
        super().__init__(position, 'play.png', groups=groups)

    def action(self, pos):
        pass
