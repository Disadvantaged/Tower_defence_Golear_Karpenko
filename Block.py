import Rectangle
import pygame


class Block(Rectangle.Rectangle):
    """
    Blocks on grass that denies placing the tower.
    """
    def __init__(self, position, size, groups=None):
        super().__init__(position, size, 'empty.png', groups=groups)
