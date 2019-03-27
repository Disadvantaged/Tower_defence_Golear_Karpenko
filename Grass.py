from Rectangle import Rectangle


class Grass(Rectangle):
    """
    Player can build towers on grass on.
    """
    def __init__(self, position, size):
        super().__init__(position, size, 'grass.png')
        self.can_build = True
