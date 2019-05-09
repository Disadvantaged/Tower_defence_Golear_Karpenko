import unittest

import pygame

import config
from base_classes.coordinate import Coordinate
from base_classes.world import World


class WorldTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.world = World(config.WORLD2, transform=False)

    @classmethod
    def tearDownClass(cls):
        pygame.quit()

    def test_find_next_pos(self):
        pass

    def test_waypoints(self):
        print(self.world.waypoints)
        self.assertEqual(self.world.waypoints, [Coordinate(0, 3),
            Coordinate(9,3)])

    def test_middle_path(self):
        self.assertFalse(self.world.check_middle_path(Coordinate(0, 0),
                                                      self.world.tile_types))
        self.assertTrue(self.world.check_middle_path(Coordinate(0, 3),
                                                     self.world.tile_types))
        self.assertTrue(self.world.check_middle_path(Coordinate(3, 3),
                                                     self.world.tile_types))
        self.assertTrue(self.world.check_middle_path(Coordinate(9, 3),
                                                     self.world.tile_types))


if __name__ == '__main__':
    unittest.main()
