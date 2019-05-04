import collections
import logging
import os

import config
from base_classes.coordinate import Coordinate
from world_components import fabrics


class World(object):
    def __init__(self, world_name):
        self.tile_size = config.TILESIZE_DEFAULT
        self.width = self.height = 0
        self.layout = []
        self.tile_types = []
        self.start = self.last = Coordinate(0, 0)  # world coordinates.
        self.cell_generator = collections.defaultdict(fabrics.CellFabric)
        self.cell_generator[0] = fabrics.GrassFabric
        self.cell_generator[1] = fabrics.BlockFabric
        self.cell_generator[2] = fabrics.RoadFabric
        self.cell_generator[3] = fabrics.RoadFabric
        self.rect = None
        self.waypoints = []
        self.towers = []
        self.load_data(world_name)
        logging.info(*self.waypoints)

    def get_tile_size(self):
        return self.tile_size

    def get_waypoints(self):
        return self.waypoints

    def get_last_position(self, screen_coordinates=True):
        if screen_coordinates:
            return self.waypoints[0]
        return self.last

    def get_starting_position(self, screen_coordinates=True):
        """
        :return: start on screen coordinates
        """
        if screen_coordinates:
            return self.waypoints[0]
        return self.start

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
        self.tile_size = Coordinate(config.FIELD_WIDTH // self.width,
                                    config.FIELD_HEIGHT // self.height)
        self.transform_layout()
        self.waypoints = self.order_waypoints(self.tile_types, self.waypoints)
        self.transform_waypoints()

    def update(self):
        for tower in self.towers:
            tower.update()

    def clear(self):
        for tower in self.towers:
            row, col = tower.get_position()
            row = row // self.tile_size[0]
            col = col // self.tile_size[1]
            tile_type = self.tile_types[col][row]
            self.layout[col][row] = self.cell_generator[tile_type].new_cell(
                tower.get_position(), self.tile_size)
            self.layout[col][row].add(*tower.groups())
            tower.kill()
        self.towers = []

    def transform_waypoints(self):
        """
        Transforms waypoints from layout coordinates to screen coordinates.
        :return: None
        """
        waypoints = self.waypoints
        self.waypoints = []
        for way_point in waypoints:
            self.waypoints.append(way_point * self.tile_size)

    def load_layout(self, world_name):
        """
        Reads file and gets the layout from it.
        Raises exception if file is not formatted well.
        :param world_name: filename of world layout in world folder.
        :return: None
        """
        path = os.path.join('assets', config.WORLD_FOLDER, world_name)
        with open(path, 'r') as file:
            self.width, self.height, startx, starty = [int(x) for x in
                                                       file.readline().split()]
            self.start = Coordinate(startx, starty)
            for _ in range(self.height):
                string = file.readline().strip()
                if len(string) != self.width:
                    logging.error('file format is wrong: expected len = ' +
                                  str(self.width) + ' but found ' +
                                  str(len(string)))
                    raise RuntimeError()
                self.tile_types.append([int(c) for c in string])
            if len(self.tile_types) != self.height:
                logging.error('file format is wrong: expected ' +
                              str(self.height) + ' rows but found ' +
                              str(len(self.tile_types)))
                raise RuntimeError()

    def transform_layout(self):
        """
        Creates layout and transforms tile_types to already created cells.
        :return: None
        """
        for row in range(len(self.tile_types)):
            cell_row = []

            for col in range(len(self.tile_types[row])):
                pos = col * self.tile_size.x, row * self.tile_size.y
                if self.tile_types[row][col] == 3:
                    self.waypoints.append((col, row))
                cell_row.append(
                    self.cell_generator[self.tile_types[row][col]].new_cell(
                        pos, self.tile_size))
            self.layout.append(cell_row)

    def order_waypoints(self, layout, waypoints):
        """
        Orders cells starting from start. Ends when all the waypoints are added.
        :param waypoints: list of waypoints that needs to be ordered.
        :return: ordered list of waypoints
        """
        cur_pos = self.start
        visited_cells = []
        ordered_waypoints = []
        count = 0
        length = len(waypoints)
        while count < length:
            next_cell = self.next_cur_pos(layout, cur_pos, visited_cells)
            if layout[next_cell.y][next_cell.x] == 3:
                ordered_waypoints.append(next_cell)
                count += 1
            visited_cells.append(cur_pos)
            cur_pos = next_cell
        ordered_waypoints.insert(0, self.start)
        self.last = ordered_waypoints[-1]
        return ordered_waypoints

    def get_cell_position(self, rect=None):
        """
        :param rect: rect of a cell
        :return: position in the list
        """
        return Coordinate(rect.topleft) // self.tile_size

    def place_tower(self, tower, pos):
        """
        Changes cell on the layout.
        Previous cell is being destroyed and its groups are added to the tower.
        :param tower: Tower from the menu. Needs to be copied.
        :param pos: position where to place tower
        :return: None
        """
        tower = tower.copy(self.layout[pos.y][pos.x].get_position())
        tower.can_build = False
        tower.set_position(self.layout[pos.y][pos.x].get_position())
        tower.set_on_field()
        tower.deactivate()
        tower.add(*(self.layout[pos.y][pos.x].groups()))
        self.layout[pos.y][pos.x].kill()
        self.layout[pos.y][pos.x] = tower
        self.towers.append(tower)
        tower.set_size(self.tile_size)

    def next_cur_pos(self, layout, cur_pos, visited_cells):
        """
        Finds next position for path.
        :return: next position
        """
        can_top = cur_pos.y > 0
        can_bot = cur_pos.y < self.height - 1
        can_left = cur_pos.x > 0
        can_right = cur_pos.x < self.width - 1
        if can_right:
            new_pos = Coordinate(cur_pos.x + 1, cur_pos.y)
            if self.check_middle_path(new_pos,
                                      layout) and new_pos not in visited_cells:
                return new_pos
        if can_left:
            new_pos = Coordinate(cur_pos.x - 1, cur_pos.y)
            if self.check_middle_path(new_pos,
                                      layout) and new_pos not in visited_cells:
                return new_pos
        if can_bot:
            new_pos = Coordinate(cur_pos.x, cur_pos.y + 1)
            if self.check_middle_path(new_pos,
                                      layout) and new_pos not in visited_cells:
                return new_pos
        if can_top:
            new_pos = Coordinate(cur_pos.x, cur_pos.y - 1)
            if self.check_middle_path(new_pos,
                                      layout) and new_pos not in visited_cells:
                return new_pos
        return None

    def check_middle_path(self, pos, layout):
        """
        Checks if given cell is in the middle of path.
        For example:
        ---
        -x-
        ---
        :return: true if cell is in the middle, false otherwise.
        """
        path_types = [2, 3]
        if layout[pos.y][pos.x] not in path_types:
            return False
        can_top = pos.y > 0
        can_bot = pos.y < self.height - 1
        can_left = pos.y > 0
        can_right = pos.x < self.width - 1
        if can_top:
            if layout[pos.y - 1][pos.x] not in path_types:
                return False
            if can_left:
                if layout[pos.y - 1][pos.x - 1] not in path_types:
                    return False
            if can_right:
                if layout[pos.y - 1][pos.x - 1] not in path_types:
                    return False
        if can_bot:
            if layout[pos.y + 1][pos.x] not in path_types:
                return False
            if can_right:
                if layout[pos.y + 1][pos.x + 1] not in path_types:
                    return False
            if can_left:
                if layout[pos.y + 1][pos.x - 1] not in path_types:
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
        self.start = self.last = Coordinate(0, 0)
