import logging

import pygame

import config
from base_classes.game import Game

pygame.init()

g_game = Game()
config.GAME = g_game
logging.getLogger().setLevel(level=logging.INFO)


def main():
    g_game.main_loop()


if __name__ == '__main__':
    logging.info("Started")
    main()
    logging.info("Finished")
