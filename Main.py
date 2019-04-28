import pygame
from BaseClasses.game import Game
import config

pygame.init()

g_game = Game()
config.GAME = g_game


def main():
    g_game.new()
    g_game.main_loop()


if __name__ == '__main__':
    main()
