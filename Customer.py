import pygame
import config
from Tower import Tower


class Customer:
    def __init__(self):
        self.item = None
        self.money = config.CUSTOMER_MONEY

    def attach(self, item: Tower):
        if self.money >= item.price:
            self.item = item

    def enough_money(self):
        return self.money >= self.item.get_price()

    def detach(self):
        item = self.item
        self.item = None
        return item

    def item_attached(self):
        return self.item is not None

    def buy_tower(self):
        item = self.detach()
        self.money -= item.get_price()
        return item
