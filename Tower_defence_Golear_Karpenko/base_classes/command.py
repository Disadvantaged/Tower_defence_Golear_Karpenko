import logging

import pygame

from Tower_defence_Golear_Karpenko import config


class Command:
    def action(self, **kwargs):
        raise NotImplementedError


class CommandExit(Command):
    def action(self, **kwargs):
        logging.info('exit')
        pygame.quit()
        exit()


class CommandNewWave(Command):
    def action(self, **kwargs):
        if kwargs['is_activated'] and config.GAME.enemies.finished:
            if config.GAME.game_started:
                config.GAME.customer.add_money(config.NEW_WAVE_BONUS)
                config.GAME.enemies.reset()
            else:
                config.GAME.start_game()


class CommandPlay(Command):
    def action(self, **kwargs):
        if not config.GAME.game_started:
            config.GAME.start_game()


class CommandTowerPressed(Command):
    def action(self, **kwargs):
        if 'is_activated' in kwargs and kwargs['is_activated']:
            config.GAME.customer.attach(kwargs['tower'])
        elif 'is_on_field' in kwargs and kwargs['is_on_field']:
            pass  # TODO add info for user about tower.
