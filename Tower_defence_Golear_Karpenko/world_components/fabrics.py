from ..base_classes import sprite
from ..world_components import grass, block, road


class CellFabric:
    """
    Fabric for producing cells. Creates cell on a given position.
    """
    @staticmethod
    def new_cell(position, size, **kwargs):
        """
        :param position: tuple(int, int)
        :param size: tuple(int, int)
        :param kwargs: can contain img
        :return: created cell
        """
        img = kwargs.get('img')  # by default: None
        return sprite.Sprite(position, size, img)


class GrassFabric(CellFabric):
    @staticmethod
    def new_cell(position, size, **kwargs) -> sprite:
        return grass.Grass(position, size)


class RoadFabric(CellFabric):
    @staticmethod
    def new_cell(position, size, **kwargs) -> sprite:
        return road.Road(position, size)


class BlockFabric(CellFabric):
    @staticmethod
    def new_cell(position, size, **kwargs):
        return block.Block(position, size)
