import pygame
from Game import Game

pygame.init()


def main():
    game = Game()
    game.new()
    game.main_loop()


if __name__ == '__main__':
    main()
