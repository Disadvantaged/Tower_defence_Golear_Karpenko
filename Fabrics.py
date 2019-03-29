import Block
import Grass
import Rectangle
import Road


class CellFabric(object):
    @staticmethod
    def new_cell(position, size, **kwargs):
        """
        :param position: tuple(int, int)
        :param size: tuple(int, int)
        :param kwargs: can contain img and groups
        :return: created cell
        """
        img = kwargs.get('img')  # by default: None
        return Rectangle.Rectangle(position, size, img)


class GrassFabric(CellFabric):
    @staticmethod
    def new_cell(position, size, **kwargs) -> Rectangle:
        return Grass.Grass(position, size)


class RoadFabric(CellFabric):
    @staticmethod
    def new_cell(position, size, **kwargs) -> Rectangle:
        return Road.Road(position, size)


class BlockFabric(CellFabric):
    @staticmethod
    def new_cell(position, size, **kwargs):
        return Block.Block(position, size)
