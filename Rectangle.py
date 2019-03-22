import pygame
import os


class Rectangle:
    def __init__(self, position, dimensions, image=None):
        """
        :param position: tuple(left, top)
        :param dimensions: int tuple(width, height)
        :param image: filename or prepared image
        """
        self.position = position
        self.dimensions = dimensions
        self.rect = pygame.Rect(*position, *dimensions)
        self.can_build = False
        if image is None:
            image = 'empty.png'
        if isinstance(image, str):
            self.image = pygame.image.load(os.path.join('assets', 'images', image)).convert_alpha()
            self.image = pygame.transform.scale(self.image, dimensions)
        elif isinstance(image, pygame.Surface):
            self.image = image.copy()

    def get_image(self):
        return self.image

    def copy(self, position=None):
        """
        :param position: the position for new rectangle. None if position as in self
        :return: new Rectangle
        """
        if position is None:
            position = self.position
        rect = Rectangle(position, self.dimensions, self.image)
        rect.can_build = self.can_build
        return rect

    def get_rect(self):
        return self.rect

    def get_position(self):
        return self.position

    def set_position(self, x, y):
        self.position = (x, y)
        self.rect = pygame.Rect(self.position, self.dimensions)

    def get_width(self):
        return self.dimensions[0]

    def get_height(self):
        return self.dimensions[1]

    def get_center(self):
        center_x = self.position[0] + self.dimensions[0] // 2
        center_y = self.position[1] + self.dimensions[1] // 2
        return center_x, center_y
