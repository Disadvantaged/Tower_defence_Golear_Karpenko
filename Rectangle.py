import os

import pygame

import config


class Rectangle(pygame.sprite.Sprite):
    def __init__(self, position, size, image=None):
        """
        :param position: tuple(left, top)
        :param size: int tuple(width, height)
        :param image: filename or prepared image
        """
        pygame.sprite.Sprite.__init__(self)
        if position is None:
            position = (0, 0)
        self.position = position
        self.size = size
        self.rect = pygame.Rect(*position, *size)
        self.can_build = False
        if image is None:
            image = 'empty.png'
        if isinstance(image, str):
            if image not in config.ASSETS:
                config.ASSETS[image] = pygame.image.load(os.path.join('assets', config.IMG_FOLDER, image)).convert()
            self.image = config.ASSETS[image]
            self._rescale()
        elif isinstance(image, pygame.Surface):
            self.image = image.copy()

    def get_image(self):
        return self.image

    def set_image(self, image):
        """
        :param image: if type == str then appends assets and loads image. else copies the image
        :return: None
        """
        if isinstance(image, str):
            if image not in config.ASSETS:
                config.ASSETS[image] = pygame.image.load(os.path.join('assets', config.IMG_FOLDER, image)).convert()
            self.image = config.ASSETS[image]
        else:
            self.image = image.copy()
        self.image = pygame.transform.scale(self.image, self.size)

    def move(self, x, y):
        self.position = (self.position[0] + x, self.position[1] + y)
        self.rect.move_ip(x, y)

    def copy(self, position=None):
        """
        :param position: the position for new rectangle. None if position as in self
        :return: new Rectangle
        """
        if position is None:
            position = self.position
        rect = Rectangle(position, self.size, self.image)
        rect.can_build = self.can_build
        return rect

    def get_rect(self):
        return self.rect

    def set_rect(self, rect):
        self.rect = rect
        self.size = self.rect.size
        self._rescale()

    def set_size(self, size):
        self.size = size
        self.rect.size = self.size
        self._rescale()

    def _rescale(self):
        self.image = pygame.transform.scale(self.image, self.size)

    def get_position(self):
        return self.position

    def set_position(self, pos):
        self.position = pos
        self.rect = pygame.Rect(self.position, self.size)

    def get_width(self):
        return self.size[0]

    def get_height(self):
        return self.size[1]

    def get_center(self):
        center_x = self.position[0] + self.size[0] // 2
        center_y = self.position[1] + self.size[1] // 2
        return center_x, center_y
