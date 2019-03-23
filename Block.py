import Rectangle
import pygame


class Block(Rectangle):
    """
    Blocks on grass that deny placing the tower.
    """
    def __init__(self, position, size, groups=None):
        super().__init__(position, size, 'block.png', groups=groups)
