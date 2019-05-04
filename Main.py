import pygame
import logging
from base_classes.game import Game
import config


pygame.init()

g_game = Game()
config.GAME = g_game


def main():
    g_game.main_loop()


if __name__ == '__main__':
    logging.basicConfig(filename='tower_defence.log', level=logging.INFO)
    logging.info("Started")
    main()
    logging.info("Finished")
