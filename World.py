import collections
import os

import Fabrics
import config


class World(object):
    def __init__(self, world_name):
        self.tile_size = config.TILESIZE_DEFAULT
        self.width = self.height = 0
        self.layout = []
        self.tile_types = []
        self.start = self.last = (0, 0)
        self.cell_generator = collections.defaultdict(Fabrics.CellFabric)
        self.cell_generator[0] = Fabrics.GrassFabric
        self.cell_generator[1] = Fabrics.BlockFabric
        self.cell_generator[2] = Fabrics.RoadFabric
        self.cell_generator[3] = Fabrics.RoadFabric
        self.rect = None
        self.waypoints = []
        self.towers = []
        self.load_data(world_name)
        self.last = self.waypoints[-1]

    def get_tile_size(self):
        return self.tile_size

    def get_waypoints(self):
        return self.waypoints

    def get_last_position(self):
        return self.last[0] * self.tile_size[0], self.last[1] * self.tile_size[1]

    def get_starting_position(self):
        return self.start[0] * self.tile_size[0], self.start[1] * self.tile_size[1]

    def set_rect(self, rect):
        self.rect = rect

    def get_rect(self):
        return self.rect

    def load_data(self, world_name):
        """
        Loads level from file. Then processes it and creates Tiles.
        :param world_name: String, filename of world file
        """
        self.empty_data()
        self.load_layout(world_name)
        self.tile_size = config.FIELD_WIDTH // self.width, config.FIELD_HEIGHT // self.height
        self.transform_layout()
        self.waypoints = self.order_waypoints(self.tile_types, self.waypoints)
        self.transform_waypoints()

    def update(self):
        for tower in self.towers:
            tower.update()

    def clear(self):
        for i, tower in enumerate(self.towers):
            row, col = tower.get_position()
            row = row // self.tile_size[0]
            col = col // self.tile_size[1]
            tile_type = self.tile_types[col][row]
            self.layout[col][row] = self.cell_generator[tile_type].new_cell(tower.get_position(), self.tile_size)
            self.layout[col][row].add(*tower.groups())
            tower.kill()
        self.towers = []

    def transform_waypoints(self):
        waypoints = self.waypoints
        self.waypoints = []
        for way_point in waypoints:
            self.waypoints.append((way_point[0] * self.tile_size[0], way_point[1] * self.tile_size[1]))

    def load_layout(self, world_name):
        path = os.path.join('assets', config.WORLD_FOLDER, world_name)
        with open(path, 'r') as f:
            self.width, self.height, start_x, start_y = [int(x) for x in f.readline().split()]
            self.start = (start_x, start_y)
            for i in range(self.height):
                s = f.readline().strip()
                if len(s) != self.width:
                    raise RuntimeError('file format is wrong: expected len = ' + str(self.width) + ' but found ' +
                                       str(len(s)))
                self.tile_types.append([int(c) for c in s])
            if len(self.tile_types) != self.height:
                raise RuntimeError('file format is wrong: expected ' + str(self.height) + ' rows but found ' +
                                   str(len(self.tile_types)))

    def transform_layout(self):
        for row in range(len(self.tile_types)):
            cell_row = []

            for col in range(len(self.tile_types[row])):
                x = col * self.tile_size[0]
                y = row * self.tile_size[1]
                if self.tile_types[row][col] == 3:
                    self.waypoints.append((col, row))
                cell_row.append(self.cell_generator[self.tile_types[row][col]].new_cell((x, y), self.tile_size))
            self.layout.append(cell_row)

    def order_waypoints(self, layout, waypoints):
        cur_pos = self.start
        visited_cells = []
        ordered_waypoints = []
        count = 0
        length = len(waypoints)
        while count < length:
            next_cell = self.next_cur_pos(layout, cur_pos, visited_cells)
            if layout[next_cell[1]][next_cell[0]] == 3:
                ordered_waypoints.append(next_cell)
                count += 1
            visited_cells.append(cur_pos)
            cur_pos = next_cell
        return ordered_waypoints

    def get_cell_position(self, rect=None):
        """
        :param rect: rect of a cell
        :return: position in the list
        """
        return rect.topleft[0] // self.tile_size[0], rect.topleft[1] // self.tile_size[1]

    def place_tower(self, tower, pos):
        tower = tower.copy(self.layout[pos[1]][pos[0]].get_position())
        tower.can_build = False
        tower.set_position(self.layout[pos[1]][pos[0]].get_position())
        tower.set_on_field()
        tower.deactivate()
        tower.add(*(self.layout[pos[1]][pos[0]].groups()))
        self.layout[pos[1]][pos[0]].kill()
        self.layout[pos[1]][pos[0]] = tower
        self.towers.append(tower)
        tower.set_size(self.tile_size)


    def next_cur_pos(self, layout, cur_pos, visited_cells):
        can_top = cur_pos[1] > 0
        can_bot = cur_pos[1] < self.height - 1
        can_left = cur_pos[0] > 0
        can_right = cur_pos[0] < self.width - 1
        if can_right:
            new_pos = (cur_pos[0] + 1, cur_pos[1])
            if self.check_middle_path(new_pos, layout) and new_pos not in visited_cells:
                return new_pos
        if can_left:
            new_pos = (cur_pos[0] - 1, cur_pos[1])
            if self.check_middle_path(new_pos, layout) and new_pos not in visited_cells:
                return new_pos
        if can_bot:
            new_pos = (cur_pos[0], cur_pos[1] + 1)
            if self.check_middle_path(new_pos, layout) and new_pos not in visited_cells:
                return new_pos
        if can_top:
            new_pos = (cur_pos[0], cur_pos[1] - 1)
            if self.check_middle_path(new_pos, layout) and new_pos not in visited_cells:
                return new_pos
        return None

    def check_middle_path(self, pos, layout):
        path_types = [2, 3]
        if layout[pos[1]][pos[0]] not in path_types:
            return False
        can_top = pos[1] > 0
        can_bot = pos[1] < self.height - 1
        can_left = pos[0] > 0
        can_right = pos[0] < self.width - 1
        if can_top:
            if layout[pos[1] - 1][pos[0]] not in path_types:
                return False
            if can_left:
                if layout[pos[1] - 1][pos[0] - 1] not in path_types:
                    return False
            if can_right:
                if layout[pos[1] - 1][pos[0] - 1] not in path_types:
                    return False
        if can_bot:
            if layout[pos[1] + 1][pos[0]] not in path_types:
                return False
            if can_right:
                if layout[pos[1] + 1][pos[0] + 1] not in path_types:
                    return False
            if can_left:
                if layout[pos[1] + 1][pos[0] - 1] not in path_types:
                    return False
        return True

    def get_layout(self):
        return self.layout

    def get_row(self, i):
        return self.layout[i]

    def empty_data(self):
        self.width = self.height = 0
        self.waypoints = []
        self.tile_types = []
        self.layout = []
        self.start = self.last = (0, 0)
