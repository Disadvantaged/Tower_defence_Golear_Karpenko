import pygame

import config
from World import World


class Game(object):
    """
    Basic game class. Keeps information of all the game data. Handles user input and main loop
    """

    def __init__(self):
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption(config.TITLE)
        self.clock = pygame.time.Clock()
        self.FPS = config.FPS
        self.caption = config.TITLE
        self.cells = []
        self.world = None
        self.pressed_cell = None  # if player pressed on the cell, shows it's information
        self.all_sprites = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()
        self.load_data()

    def load_data(self):
        """
        Loads data from assets.
        """
        self.world = World(config.WORLD1)
        for row in self.world.get_layout():
            self.tiles.add(*row)
            self.all_sprites.add(*row)
            self.cells.extend(row)

    def new(self):
        """
        Adds all the added sprites to the screen and initializes the game.
        """
        self.all_sprites.draw(self.screen)

    def handle_events(self):
        """
        Reads user input.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.check_mouse_pressed(event.pos)

    def check_mouse_pressed(self, pos):
        """
        If player pressed left mouse button, checks if he pressed on a cell or not.
        :param pos: position of mouse click.
        """
        for cell in self.cells:
            if cell.get_rect().collidepoint(pos):
                if self.pressed_cell is None:
                    self.pressed_cell = cell
                    print('pressed')
                    break
                else:
                    cell.set_image(self.pressed_cell.get_image().copy())
                    self.pressed_cell = None

    def update(self):
        pass

    def draw(self):
        self.all_sprites.draw(self.screen)

    def main_loop(self):
        while True:
            self.clock.tick(self.FPS)

            self.handle_events()
            self.draw()
            pygame.display.update()
