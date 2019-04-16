import pygame

import config
from Game import Game

pygame.init()

g_game = Game()
config.GAME = g_game


def main():
    g_game.main_loop()


if __name__ == '__main__':
    main()
