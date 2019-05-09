from ..base_classes.sprite import Sprite


class Grass(Sprite):
    """
    Player can build towers on grass on.
    """
    def __init__(self, position, size):
        super().__init__(position, size, 'grass.png')
        self.can_build = True
