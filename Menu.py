from Button import *
from Rectangle import Rectangle


class Menu(Rectangle):
    def __init__(self, position, width, height, b_color=config.MENU_BG_COLOR):
        self.position = position
        self.width = width
        self.height = height
        self.b_color = b_color
        self.items = pygame.sprite.Group()
        self.rect = pygame.Rect(position, (width, height))
        self.add_button(ExitButton)

    def get_items(self):
        return self.items

    def add_button(self, button_type):
        btn = button_type((0, 0))
        pos = self.next_item_position(btn)
        btn.set_position(pos)

        self.items.add(btn)

    def next_item_position(self, btn):
        pos = self.rect.centerx - btn.get_width() // 2, self.rect.centery - btn.get_height() // 2
        return pos

    def draw(self, surface):
        surface.fill(self.b_color, self.rect)
        self.items.draw(surface)
