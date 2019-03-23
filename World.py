import pygame
import Rectangle
import Fabrics
import os
import config


class World:
    def __init__(self, world_name):
        self.tile_size = config.DEFAULT_TILESIZE
        self.width = self.height = self.start_x = self.start_y = 0
        self.layout = []
        self.load_level(world_name)
        self.cell_generator = [Grass_Fabric, Road_Fabric]

    def load_level(self, world_name):
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
            for col in range(len(layout[y])):
                x = col * self.tile_size[0]
                y = row * self.tile_size[1]
                cell_row = []
                if layout[row][col] == 0:
                    cell = ((x, y), self.tile_size)

    def empty_data(self):
        self.width = self.height = self.start_y = self.start_x = 0
        self.layout = []
