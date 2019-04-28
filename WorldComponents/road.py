from BaseClasses.rectangle import Rectangle


class Road(Rectangle):
    """
    Road where creeps can go.
    """
    def __init__(self, position, size):
        super().__init__(position, size, 'road.png')
