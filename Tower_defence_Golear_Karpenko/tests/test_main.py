import unittest
from pathlib import Path
import pygame

from Tower_defence_Golear_Karpenko import config
from Tower_defence_Golear_Karpenko.base_classes.coordinate import Coordinate
from Tower_defence_Golear_Karpenko.base_classes.world import World


class WorldTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        config.CWD = Path(__file__).parent.parent
        cls.world = World(config.WORLD2, transform=False)

    @classmethod
    def tearDownClass(cls):
        pygame.quit()

    def test_find_next_pos(self):
        pass

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
