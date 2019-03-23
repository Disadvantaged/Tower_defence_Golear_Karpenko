from Rectangle import Rectangle


class Road(Rectangle):
    def __init__(self, position, size, groups=None):
        super().__init__(position, size, 'road.png', groups=groups)
