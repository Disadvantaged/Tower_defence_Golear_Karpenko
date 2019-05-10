import os

import pygame

from .. import config
from ..base_classes.coordinate import Coordinate
from ..base_classes.rectangle import Rect


class Sprite(pygame.sprite.Sprite):
    def __init__(self, position, size, image=None):
        """
        :param position: tuple(left, top)
        :param size: int tuple(width, height)
        :param image: filename or prepared image
        """
        pygame.sprite.Sprite.__init__(self)
        if position is None:
            position = Coordinate(0, 0)
        self.position = Coordinate(position)
        self.size = Coordinate(size)
        self.rect = Rect(*position, *size)
        if image is None:
            image = 'empty.png'
        if isinstance(image, str):
            if image not in config.ASSETS:
                config.ASSETS[image] = pygame.image.load(
                    os.path.join(config.CWD, 'assets',
                                 config.IMG_FOLDER, image)).convert()
            self.image = config.ASSETS[image]
            self._rescale()
        elif isinstance(image, pygame.Surface):
            self.image = image.copy()

    def get_image(self) -> pygame.Surface:
        return self.image

    def kill(self) -> None:
        """
        wrap for sprite.
        :return: None
        """
        super().kill()

    def groups(self):
        return super().groups()

    def set_image(self, image) -> None:
        """
        Checks for image type and sets it properly.
        :param image: If type == str then appends assets and loads image.
                      Else copies the image
        :return: None
        """
        if isinstance(image, str):
            if image not in config.ASSETS:
                config.ASSETS[image] = pygame.image.load(
                    os.path.join(config.CWD, 'assets',
                                 config.IMG_FOLDER, image)).convert()
            self.image = config.ASSETS[image]
        else:
            self.image = image.copy()
        self.image = pygame.transform.scale(self.image, self.size)

    def move(self, x, y) -> None:
        self.position += (x, y)
        self.rect.move_ip(x, y)

    def copy(self, position=None):
        """
        Should be overwritten for child classes.
        :param position: the position for new rectangle. None if pos==self.pos
        :return: new Rectangle
        """
        if position is None:
            position = self.position
        sprite = Sprite(position, self.size, self.image)
        return sprite

    def get_rect(self):
        return self.rect

    def set_rect(self, rect):
        self.rect = rect
        self.size = Coordinate(self.rect.size)
        self._rescale()

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = Coordinate(size)
        self.rect.size = self.size
        self._rescale()

    def _rescale(self):
        """
        Transforms image because its asset larger than size.
        """
        self.image = pygame.transform.scale(self.image, self.size)

    def get_position(self):
        return self.position

    def set_position(self, pos):
        self.position = pos
        self.rect = pygame.Rect(self.position, self.size)

    def get_width(self):
        return self.size.x

    def get_height(self):
        return self.size.y

    def get_center(self):
        center = self.position + self.size // 2
        return center
