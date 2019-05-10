import logging

from Tower_defence_Golear_Karpenko import config
from Tower_defence_Golear_Karpenko.entity.tower import Tower


class Customer:
    def __init__(self):
        self.item = None
        self.money = config.CUSTOMER_MONEY

    def attach(self, item: Tower):
        logging.debug('attached')
        if self.money >= item.price:
            self.item = item

    def enough_money(self):
        return self.money >= self.item.get_price()

    def add_money(self, money):
        self.money += money

    def detach(self):
        logging.debug('detached')
        item = self.item
        self.item = None
        return item

    def item_attached(self):
        return self.item is not None

    def buy_tower(self):
        item = self.detach()
        self.money -= item.get_price()
        return item

    def reset(self):
        self.money = config.CUSTOMER_MONEY
