import logging
import os
import pygame
from Tower_defence_Golear_Karpenko import config
from Tower_defence_Golear_Karpenko.base_classes.game import Game


def main():
    pygame.init()

    config.CWD = os.path.dirname(os.path.realpath(__file__))

    g_game = Game()
    config.GAME = g_game

    g_game.main_loop()


if __name__ == '__main__':
    logging.getLogger().setLevel(level=logging.INFO)
    logging.info("Started")
    main()
    logging.info("Finished")
