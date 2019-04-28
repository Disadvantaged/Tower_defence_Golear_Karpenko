from BaseClasses import rectangle


class Block(rectangle.Rectangle):
    """
    Blocks on grass that denies placing the tower.
    """
    def __init__(self, position, size):
        super().__init__(position, size, 'block.png')
