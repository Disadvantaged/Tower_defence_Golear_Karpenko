from Button import *
from Rectangle import Rectangle
from TowerBuilder import *
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
        # self.add_button(button_type=NewWaveButton)
        # self.add_button(button_type=PlayButton)
        # self.add_button(button_type=ExitButton)
        self.tower_num = 0
        self.tower_row = 1
        self.curr_tow = 0
        self.dist_tow_but = 20
        self.towers_data = []
        self.load_data()
        self.tower_builder = TowerBuilder()
        for i in range(self.tower_num):
            self.tower_builder.clear()
            for arg in self.towers_data[i].split(' '):
                self.tower_builder.set_property(*arg.split('='))
            self.add_button(button=self.tower_builder.new_TowerButton())

            self.curr_tow = i

    def get_items(self):
        return self.items

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
            print(button.get_position())
        self.items.add(button)

    def next_item_position(self, btn):
        pos = self.rect.centerx - self.but_pos, self.rect.centery - btn.get_height() // 2
        self.but_pos -= (MENU_DIST_BUTTON + BUTTON_WIDTH)
        return pos

    def next_TowBut_position(self, btn):
        pos = (self.rect.centerx - self.rect.centerx // 1.8 + (self.dist_tow_but + BUTTON_WIDTH) * self.curr_tow,
               self.rect.centery // 3 - (BUTTON_HEIGHT + self.dist_tow_but) * self.tower_row)
        if self.curr_tow == 3:
            self.tower_row += 1
        return pos

    def draw(self, surface):
        surface.fill(self.b_color, self.rect)
        self.items.draw(surface)

    def load_data(self):
        path = os.path.join('assets', config.TOWER_FOLDER, TOWERS_FILE)
        with open(path, 'r') as f:
            self.tower_num = int(f.readline()[:1])
            for line in f:
                self.towers_data.append(line)
