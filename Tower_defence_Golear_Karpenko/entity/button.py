import os
import logging
import pygame

from Tower_defence_Golear_Karpenko import config
from Tower_defence_Golear_Karpenko.base_classes.sprite import Sprite


class Button(Sprite):
    def __init__(self, position=(0, 0), image=None):
        if image is not None:
            image = os.path.join(config.BUTTON_PATH, image)
        super().__init__(position, (config.BUTTON_WIDTH,
                                    config.BUTTON_HEIGHT), image)
        self.is_activated = True

    def activate(self):
        self.is_activated = True

    def deactivate(self):
        self.is_activated = False

    def action(self, pos):
        raise NotImplementedError


class ExitButton(Button):
    def __init__(self, position):
        super().__init__(position, 'quit.png')

    def action(self, pos):
        logging.info('exit')
        pygame.quit()
        exit()


class NewWaveButton(Button):
    def __init__(self, position):
        super().__init__(position, 'nextWave.png')

    def action(self, pos):
        if self.is_activated and config.GAME.enemies.finished:
            if config.GAME.game_started:
                config.GAME.customer.add_money(config.NEW_WAVE_BONUS)
                config.GAME.enemies.reset()
            else:
                config.GAME.start_game()


class PlayButton(Button):
    def __init__(self, position):
        super().__init__(position, 'play.png')

    def action(self, pos):
        if not config.GAME.game_started:
            config.GAME.start_game()
