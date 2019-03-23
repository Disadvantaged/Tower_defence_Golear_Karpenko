import Rectangle
import Grass
import Road


class CellFabric(object):
    def new_cell(self, position, size, **kwargs):
        img = kwargs.get('img')
        groups = kwargs.get('groups')
        return Rectangle.Rectangle(position, size, img, groups)


class GrassFabric(CellFabric):
    def new_cell(self, position, size, **kwargs):
        return Grass.Grass(position, size, kwargs.get('groups'))


class RoadFabric(CellFabric):
    def new_cell(self, position, size, **kwargs):
        return Road.Road(position, size, kwargs.get('groups'))
