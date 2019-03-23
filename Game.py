import pygame
from Grass import Grass
from Road import Road
from World import World
import config


class Game(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption(config.TITLE)
        self.clock = pygame.time.Clock()
        self.FPS = config.FPS
        self.caption = config.TITLE
        self.cells = []
        self.world = None
        self.pressed_cell = None

        self.load_data()

    def load_data(self):
        self.world = World(config.WORLD1)
        grass = Grass((50, 50), (40, 40))
        road = Road((400, 400), (50, 50))
        self.cells.append(grass)
        self.cells.append(road)

    def new(self):
        for cell in self.cells:
            self.screen.blit(cell.get_image(), cell.get_position())

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.check_mouse_pressed(event.pos)

    def check_mouse_pressed(self, pos):
        for cell in self.cells:
            if cell.get_rect().collidepoint(pos):
                self.pressed_cell = cell
        else:
            if self.pressed_cell is not None:
                x = pos[0] - self.pressed_cell.get_width() // 2
                y = pos[1] - self.pressed_cell.get_height() // 2
                rect = pygame.Rect(x, y, self.pressed_cell.get_width(), self.pressed_cell.get_height())
                if rect.collidelist(self.cells) == -1:
                    new_cell = self.pressed_cell.copy((x, y))
                    self.pressed_cell = None
                    self.screen.blit(new_cell.get_image(), new_cell.get_position())
                    self.cells.append(new_cell)

    def main_loop(self):
        while True:
            self.clock.tick(self.FPS)

            self.handle_events()
            pygame.display.update()
