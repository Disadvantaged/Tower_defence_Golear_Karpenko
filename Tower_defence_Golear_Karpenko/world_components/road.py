from ..base_classes.sprite import Sprite


class Road(Sprite):
    """
    Road where creeps can go.
    """
    def __init__(self, position, size):
        super().__init__(position, size, 'road.png')
        self.can_build = False
