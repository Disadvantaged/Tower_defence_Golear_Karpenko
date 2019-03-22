from Rectangle import Rectangle


class Road(Rectangle):
    def __init__(self, position, dimensions):
        super().__init__(position, dimensions, 'road.png')
