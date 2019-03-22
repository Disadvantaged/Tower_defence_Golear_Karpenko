import pygame
from Game import Game

pygame.init()

FPS: int = 60
WIDTH = 600
HEIGHT = 800


def main():
    game = Game(WIDTH, HEIGHT, FPS, "Tower Defence")
    game.main_loop()


if __name__ == '__main__':
    main()
