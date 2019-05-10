import os

import pygame

from Tower_defence_Golear_Karpenko import config
from Tower_defence_Golear_Karpenko.base_classes.rectangle import Rect
from Tower_defence_Golear_Karpenko.base_classes.sprite import Sprite
from Tower_defence_Golear_Karpenko.entity.button\
    import PlayButton, ExitButton, NewWaveButton
from Tower_defence_Golear_Karpenko.entity.tower import Tower
from Tower_defence_Golear_Karpenko.entity_controller.tower_builder\
    import TowerBuilder


class Menu(Sprite):
    def __init__(self, position, width, height, b_color=config.MENU_BG_COLOR):
        self.but_pos = (config.MENU_NUM_BUTTON *
                        (config.BUTTON_WIDTH + config.MENU_DIST_BUTTON)) // 2
        self.position = position
        self.width = width
        self.height = height
        self.b_color = b_color
        self.items = pygame.sprite.Group()
        self.rect = Rect(position, (width, height))
        self.add_button(button_type=NewWaveButton)
        self.add_button(button_type=PlayButton)
        self.add_button(button_type=ExitButton)
        self.tower_num = 0
        self.curr_tow = 0
        self.customers_money = config.CUSTOMER_MONEY
        self.customer_status = config.FONT.render(
            f"Customers money: {self.customers_money}", 1, config.RED
        )
        self.customer_status_pos = self.customer_status.get_rect(
            center=self.rect.center
        )
        self.customer_status_pos.x += 300
        self.dist_tow_but = 20
        self.towers_data = []
        self.load_data()
        self.tower_builder = TowerBuilder()
        for i in range(self.tower_num):
            self.tower_builder.clear()
            for arg in self.towers_data[i].split(' '):
                self.tower_builder.set_property(*arg.split('='))
            self.add_button(button=self.tower_builder.new_tower_button())

            self.curr_tow = i

    def get_status(self):
        return self.customer_status

    def get_items(self):
        return self.items

    def update(self):
        self.customers_money = config.GAME.customer.money
        if config.GAME.game_started:
            self.customer_status = config.FONT.render(
                f"Customers money: {self.customers_money}", 1, config.RED
            )
        for button in self.items:
            if isinstance(button, Tower):
                if self.customers_money < button.get_price():
                    button.get_image()

    def add_button(self, button_type=None, button=None):
        """
        Either of parameters should not be None
        :param button_type: creates button with given type
        :param button: finds place for a button
        :return: None
        """
        if (button_type is None) == (button is None):
            raise ValueError
        if button_type:
            button = button_type((0, 0))
            pos = self.next_item_position(button)
            button.set_position(pos)
        else:
            pos = self.next_tower_button_position(button)
            button.set_position(pos)
        self.items.add(button)

    def next_item_position(self, btn):
        pos = self.rect.centerx - self.but_pos,\
              self.rect.centery - btn.get_height() // 2
        self.but_pos -= (config.MENU_DIST_BUTTON + config.BUTTON_WIDTH)
        return pos

    def next_tower_button_position(self, btn):
        pos = (self.rect.centerx - self.rect.centerx // 1.2 + self.dist_tow_but,
               self.rect.centery - btn.get_height() // 2)
        self.dist_tow_but += config.BUTTON_WIDTH
        return pos

    def draw(self, surface):
        surface.fill(self.b_color, self.rect)
        self.items.draw(surface)
        surface.blit(self.customer_status, self.customer_status_pos)

    def load_data(self):
        path = os.path.join(config.CWD, 'assets',
                            config.TOWER_FOLDER, config.TOWERS_FILE)
        with open(path, 'r') as file:
            self.tower_num = int(file.readline()[:1])
            for line in file:
                self.towers_data.append(line.strip())

    def set_lost(self):
        self.customer_status = config.FONT.render(
            "You lost. Pressed Start.", 1, config.RED)
        for button in self.items:
            button.deactivate()

    def start_game(self):
        for button in self.items:
            button.activate()

    def win(self):
        self.customer_status = config.FONT.render(
            "You won. Congratulations!", 1, config.RED
        )
        for button in self.items:
            button.deactivate()
