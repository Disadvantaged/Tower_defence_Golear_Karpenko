import os

import config
from Rectangle import Rectangle


class Tower(Rectangle):
    def __init__(self, position=(0, 0), image=None):
        if image is not None:
            image = os.path.join('towers', image)
        super().__init__(position, config.DEFAULT_TILESIZE, image)
        self.is_activated = False
        self.range = config.DEFAULT_TOWER_RANGE

    def set_range(self, range):
        self.range = range

    def activate(self):
        self.is_activated = True

    def deactivate(self):
        self.is_activated = False

    def action(self, pos):
        pass
