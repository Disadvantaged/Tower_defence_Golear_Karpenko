from ..base_classes import sprite


class Block(sprite.Sprite):
    """
    Blocks on grass that denies placing the tower.
    """

    def __init__(self, position, size):
        super().__init__(position, size, 'block.png')
        self.can_build = False
