import collections
import os

import Fabrics
import config


class World:
    def __init__(self, world_name):
        self.tile_size = config.DEFAULT_TILESIZE
        self.width = self.height = self.start_x = self.start_y = 0
        self.layout = []
        self.cell_generator = collections.defaultdict(Fabrics.CellFabric)
        self.cell_generator[0] = Fabrics.GrassFabric
        self.cell_generator[1] = Fabrics.BlockFabric
        self.cell_generator[2] = Fabrics.RoadFabric
        self.cell_generator[3] = Fabrics.RoadFabric
        self.load_level(world_name)

    def load_level(self, world_name):
        """
        Loads level from file. Then processes it and creates Tiles.
        :param world_name: String, filename of world file
        """
        self.empty_data()
        path = os.path.join('assets', config.WORLD_FOLDER, world_name)
        with open(path, 'r') as f:
            self.width, self.height, self.start_x, self.start_y = [int(x) for x in f.readline().split()]
            layout = []
            for i in range(self.height):
                s = f.readline().strip()
                if len(s) != self.width:
                    raise RuntimeError('file format is wrong: expected len = ' + str(self.width) + ' buf found ' +
                                       str(len(s)))
                layout.append(s)
            if len(layout) != self.height:
                raise RuntimeError('file format is wrong: expected ' + str(self.height) + ' rows buf found ' +
                                   str(len(layout)))
        self.tile_size = config.SCREEN_WIDTH // self.width, config.SCREEN_HEIGHT // self.height
        for row in range(len(layout)):
            cell_row = []
            for col in range(len(layout[row])):
                x = col * self.tile_size[0]
                y = row * self.tile_size[1]
                cell_row.append(self.cell_generator[int(layout[row][col])].new_cell((x, y), self.tile_size))
            self.layout.append(cell_row)

    def get_layout(self):
        return self.layout

    def get_row(self, i):
        return self.layout[i]

    def empty_data(self):
        self.width = self.height = self.start_y = self.start_x = 0
        self.layout = []
