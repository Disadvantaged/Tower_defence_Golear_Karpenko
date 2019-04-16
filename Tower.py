import os

import config
from Rectangle import Rectangle


class Tower(Rectangle):
    def __init__(self, position=(0, 0), image=None, price=config.TOWER_PRICE):
        if image is not None:
            if isinstance(image, str):
                image = os.path.join('towers', image)
        super().__init__(position, config.TILESIZE_DEFAULT, image)
        self.can_build = False
        self.is_on_field = False  # Tower can shoot
        self.is_activated = False  # Tower is in menu and pressable
        self.price = price
        self.range = config.TOWER_RANGE_DEFAULT

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_range(self):
        return self.range

    def copy(self, position=None):
        tower = Tower(self.position, self.image, self.price)
        tower.is_on_field = self.is_on_field
        tower.is_activated = self.is_activated
        tower.range = self.range
        return tower

    def update(self, *args):
        if self.is_on_field:
            pass

    def set_range(self, ran):
        self.range = ran

    def set_on_field(self):
        self.is_on_field = True

    def activate(self):
        self.is_activated = True
        print('tower activated')

    def deactivate(self):
        self.is_activated = False

    def action(self, pos):
        if self.is_activated:
            config.GAME.customer.attach(self)
