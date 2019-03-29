import os

import pygame

import config
from Rectangle import Rectangle


class Button(Rectangle):
    def __init__(self, position=(0, 0), image=None):
        if image is not None:
            image = os.path.join(config.BUTTON_PATH, image)
        super().__init__(position, (config.BUTTON_WIDTH, config.BUTTON_HEIGHT), image)

    def action(self, pos):
        raise NotImplementedError


class ExitButton(Button):
    def __init__(self, position):
        super().__init__(position, 'quit.png')

    def action(self, pos):
        print('exiting')
        pygame.quit()
        exit()


class NewWaveButton(Button):
    def __init__(self, position):
        super().__init__(position, 'nextWave.png')

    def action(self, pos):
        print('new wave has started')


class PlayButton(Button):
    def __init__(self, position):
        super().__init__(position, 'play.png')

    def action(self, pos):
        if Main.g_game.game_started:
            print('the game has already started')
        else:
            Main.g_game.start_game()
