class Coordinate:
    def __init__(self, *args, **kwargs):
        """
        :param args: if len(args) == 1 then it is tuple or Coordinate.
        :param kwargs:
        """
        if len(args) == 1:
            self.x = args[0][0]
            self.y = args[0][1]
        elif len(args) == 2:
            self.x = args[0]
            self.y = args[1]
        elif len(args) > 2:
            raise ValueError
        else:
            self.x = kwargs['x']
            self.y = kwargs['y']

    @staticmethod
    def keys():
        return ['x', 'y']

    def __getitem__(self, item):
        if item == 0 or item == 'x':
            return self.x
        if item == 1 or item == 'y':
            return self.y
        return self.__getattribute__(item)

    def __len__(self):
        return 2

    def __next__(self):
        yield self.x
        yield self.y

    def __iter__(self):
        """
        :return: tuple x, y. Needed for unpacking for example.
        """
        return (i for i in (self.x, self.y))

    def __eq__(self, other):
        if isinstance(other, tuple):
            return self.x == other[0] and self.y == other[1]
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __imul__(self, other):
        if isinstance(other, Coordinate):
            self.x *= other.x
            self.y *= other.y
        elif isinstance(other, int) or isinstance(other, float):
            self.x *= other
            self.y *= other
        elif isinstance(other, tuple):
            self.x *= other[0]
            self.y *= other[1]
        return self

    def __mul__(self, other):
        temp = Coordinate(self.x, self.y)
        temp *= other
        return temp

    def __ifloordiv__(self, other):
        if isinstance(other, Coordinate):
            self.x //= other.x
            self.y //= other.y
        elif isinstance(other, int) or isinstance(other, float):
            self.x //= other
            self.y //= other
        elif isinstance(other, tuple):
            self.x //= other[0]
            self.y //= other[1]
        return self

    def __floordiv__(self, other):
        temp = Coordinate(self.x, self.y)
        temp //= other
        return temp

    def __iadd__(self, other):
        if isinstance(other, Coordinate):
            self.x += other.x
            self.y += other.y
        elif isinstance(other, int) or isinstance(other, float):
            self.x += other
            self.y += other
        elif isinstance(other, tuple):
            self.x += other[0]
            self.y += other[1]
        return self

    def __add__(self, other):
        temp = Coordinate(self.x, self.y)
        temp += other
        return temp

    def __isub__(self, other):
        if isinstance(other, Coordinate):
            self.x -= other.x
            self.y -= other.y
        elif isinstance(other, int) or isinstance(other, float):
            self.x -= other
            self.y -= other
        elif isinstance(other, tuple):
            self.x -= other[0]
            self.y -= other[1]
        return self

    def __sub__(self, other):
        temp = Coordinate(self.x, self.y)
        temp -= other
        return temp
