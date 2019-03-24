import Rectangle


class Block(Rectangle.Rectangle):
    """
    Blocks on grass that denies placing the tower.
    """
    def __init__(self, position, size, groups=None):
        super().__init__(position, size, 'block.png', groups=groups)
