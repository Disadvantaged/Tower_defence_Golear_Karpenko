from Rectangle import Rectangle


class Grass(Rectangle):
    def __init__(self, position, dimensions):
        super().__init__(position, dimensions, 'grass.png')
        self.can_build = True
