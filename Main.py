import pygame
from Game import Game

pygame.init()

g_game = Game()


def main():
    g_game.new()
    g_game.main_loop()


if __name__ == '__main__':
    main()
