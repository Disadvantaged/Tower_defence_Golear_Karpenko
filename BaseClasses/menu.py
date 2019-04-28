from Entity.button import *
from BaseClasses.rectangle import Rectangle
from EntityController.tower_builder import *
from config import *


class Menu(Rectangle):
    def __init__(self, position, width, height, b_color=MENU_BG_COLOR):
        self.but_pos = (MENU_NUM_BUTTON * (BUTTON_WIDTH + MENU_DIST_BUTTON)) // 2
        self.position = position
        self.width = width
        self.height = height
        self.b_color = b_color
        self.items = pygame.sprite.Group()
        self.rect = pygame.Rect(position, (width, height))
        self.add_button(button_type=NewWaveButton)
        self.add_button(button_type=PlayButton)
        self.add_button(button_type=ExitButton)
        self.tower_num = 0
        self.curr_tow = 0
        self.customers_money = config.CUSTOMER_MONEY
        self.customer_status = config.FONT.render(f"Customers money: {self.customers_money}", 1, (config.RED))
        self.customer_status_pos = self.customer_status.get_rect(center=self.rect.center)
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
        self.customer_status = config.FONT.render(f"Customers money: {self.customers_money}", 1, config.RED)
        for button in self.items:
            if isinstance(button, Tower):
                if self.customers_money < button.get_price():
                    button.get_image()

    def add_button(self, button_type=None, button=None):
        """
        :param button_type: creates button with given type, if None then finds place for button
        :param button: finds place for a button, if None then button_type should not be None
        :return: None
        """
        if (button_type is None and button is None) or (button is not None and button_type is not None):
            return None
        if button_type:
            button = button_type((0, 0))
            pos = self.next_item_position(button)
            button.set_position(pos)
        else:
            pos = self.next_TowBut_position(button)
            button.set_position(pos)
        self.items.add(button)

    def next_item_position(self, btn):
        pos = self.rect.centerx - self.but_pos, self.rect.centery - btn.get_height() // 2
        self.but_pos -= (MENU_DIST_BUTTON + BUTTON_WIDTH)
        return pos

    def next_TowBut_position(self, btn):
        pos = (self.rect.centerx - self.rect.centerx // 1.2 + self.dist_tow_but,
               self.rect.centery - btn.get_height() // 2)
        self.dist_tow_but += BUTTON_WIDTH
        return pos

    def draw(self, surface):
        surface.fill(self.b_color, self.rect)
        self.items.draw(surface)
        surface.blit(self.customer_status, self.customer_status_pos)

    def load_data(self):
        path = os.path.join('assets', config.TOWER_FOLDER, TOWERS_FILE)
        with open(path, 'r') as f:
            self.tower_num = int(f.readline()[:1])
            for line in f:
                self.towers_data.append(line.strip())
