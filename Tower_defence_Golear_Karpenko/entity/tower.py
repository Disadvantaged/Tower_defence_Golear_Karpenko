import logging
import math
import os

from Tower_defence_Golear_Karpenko import config
from Tower_defence_Golear_Karpenko.base_classes.sprite import Sprite


class Tower(Sprite):
    def __init__(self, position=(0, 0), image=None, price=config.TOWER_PRICE):
        if image is not None:
            if isinstance(image, str):
                image = os.path.join('towers', image)
        super().__init__(position, config.BUTTON_SIZE, image)
        self.can_build = False
        self.wait = False
        self.is_on_field = False  # Tower can shoot
        self.is_activated = False  # Tower is in menu and pressable
        self.price = price
        self.waiting_time = 0
        self.damage = config.TOWER_DAMAGE_DEFAULT
        self.delay = config.TOWER_DELAY_DEFAULT
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
        tower.damage = self.damage
        tower.delay = self.delay
        tower.range = self.range
        logging.info('%d %d %d', self.range, self.delay, self.damage)
        return tower

    def update(self):
        if self.is_on_field:
            if self.wait:
                self.waiting_time += config.GAME.clock.tick()
            if self.waiting_time >= self.delay:
                self.wait = False
                self.waiting_time = 0
            for enemy in config.GAME.enemies.get_enemies():
                if self.compute_distance(enemy.get_position()) < self.range:
                    if not self.wait:
                        self.wait = True
                        enemy.attacked(self.damage)
                if not enemy.alive():
                    config.GAME.enemies.num_enemies -= 1
                if config.GAME.enemies.check_for_win():
                    config.GAME.win()

    def set_range(self, ran):
        self.range = ran

    def set_on_field(self):
        self.is_on_field = True

    def activate(self):
        self.is_activated = True

    def deactivate(self):
        self.is_activated = False

    def action(self, _):
        if self.is_activated:
            config.GAME.customer.attach(self)

    def compute_distance(self, pos):
        return math.sqrt((pos[0] - self.position[0]) ** 2 +
                         (pos[1] - self.position[1]) ** 2)

    def set_delay(self, param):
        self.delay = param

    def set_dmg(self, param):
        self.damage = param
