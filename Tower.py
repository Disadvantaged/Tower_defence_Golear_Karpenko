import os

import config
from Rectangle import Rectangle


class Tower(Rectangle):
    def __init__(self, position=(0, 0), image=None, price=config.TOWER_PRICE):
        if image is not None:
            image = os.path.join('towers', image)
        super().__init__(position, config.TILESIZE_DEFAULT, image)
        self.is_activated = False
        self.price = price
        self.range = config.TOWER_RANGE_DEFAULT

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_range(self):
        return self.range

    def set_range(self, ran):
        self.range = ran

    def activate(self):
        self.is_activated = True
        print('tower activated')

    def deactivate(self):
        self.is_activated = False

    def action(self, pos):
        print('tower pressed')
