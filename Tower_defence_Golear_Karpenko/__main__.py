import logging
import os
import pygame
from . import config
from .base_classes.game import Game

pygame.init()

config.CWD = os.path.dirname(os.path.realpath(__file__))
print(config.CWD)

g_game = Game()
config.GAME = g_game
logging.getLogger().setLevel(level=logging.INFO)


def main():
    g_game.main_loop()


if __name__ == '__main__':
    logging.info("Started")
    main()
    logging.info("Finished")
