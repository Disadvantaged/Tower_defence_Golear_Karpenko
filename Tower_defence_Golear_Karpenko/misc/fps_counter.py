import logging

from Tower_defence_Golear_Karpenko import config
from Tower_defence_Golear_Karpenko.base_classes.coordinate import Coordinate


class FPSCounter:
    def __init__(self, clock, pos=Coordinate(0, 0)):
        self.pos = pos
        self.clock = clock
        self.text = config.FONT.render(
            'FPS: {:.0f}'.format(self.clock.get_fps()), 1, config.RED)

    def update(self):
        logging.debug(self.clock.get_fps())
        self.text = config.FONT.render(
            'FPS: {:.0f}'.format(self.clock.get_fps()), 1, config.RED)

    def draw(self, screen):
        screen.blit(self.text, self.pos)
