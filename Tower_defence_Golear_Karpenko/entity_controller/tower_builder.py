from Tower_defence_Golear_Karpenko.entity.tower import Tower


class TowerBuilder:
    def __init__(self):
        self.tower = Tower(image='tower1.png')

    def new_tower_button(self):
        return self.tower

    def clear(self):
        self.tower = Tower(image='tower1.png')

    def set_property(self, attribute, value):
        if attribute == 'image':
            self.tower.set_image(value)
        elif attribute == 'range':
            self.tower.set_range(int(value))
        elif attribute == 'price':
            self.tower.set_price(int(value))
        elif attribute == 'damage':
            self.tower.set_dmg(int(value))
        elif attribute == 'delay':
            self.tower.set_delay(int(value))
