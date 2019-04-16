import pygame

import config
from EnemyController import EnemyController
from Menu import Menu
from Tower import Tower
from Customer import Customer
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
        config.FONT = pygame.font.Font(None, 38)
        self.caption = config.TITLE
        self.cells = []
        self.pressed_cell = None  # if player pressed on the cell, shows it's information
        self.all_sprites = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()
        self.world = None
        self.customer = Customer()
        self.game_started = False
        self.menu = Menu((0, config.FIELD_HEIGHT), config.MENU_WIDTH, config.MENU_HEIGHT)
        self.load()

        self.field = pygame.Surface((config.FIELD_WIDTH, config.FIELD_HEIGHT))
        self.world.set_rect(self.screen.blit(self.field, (0, 0)))

        config.ENEMY_SPAWN_EVENT = pygame.USEREVENT + 1
        self.enemies = EnemyController(self)
        self.all_sprites.add(self.enemies.get_enemies())

    def start_game(self):
        self.game_started = True

    def load(self):
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
        self.menu.draw(self.screen)
        self.all_sprites.add(self.menu.get_items())
        self.all_sprites.draw(self.field)
        self.enemies.draw(self.field)

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
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                self.customer.detach()
            elif event.type == config.ENEMY_SPAWN_EVENT:
                done = self.enemies.spawn()
                if done:
                    pygame.time.set_timer(config.ENEMY_SPAWN_EVENT, 0)

    def check_mouse_pressed(self, pos):
        """
        If player pressed left mouse button, checks if he pressed on a cell or not.
        :param pos: position of mouse click.
        """
        if self.world.get_rect().collidepoint(pos) and self.customer.item_attached():
            for cell in self.cells:
                if cell.get_rect().collidepoint(pos) and cell.can_build and self.customer.enough_money():
                    tower = self.customer.buy_tower()
                    self.world.place_tower(tower, self.world.get_cell_position(rect=cell.get_rect()))
                    tower.activate()
                    print('bought')
        elif self.menu.get_rect().collidepoint(pos):
            for item in self.menu.get_items():
                if item.get_rect().collidepoint(pos):
                    if isinstance(item, Tower):
                        self.customer.attach(item)
                    item.action(pos)

    def update(self):
        self.enemies.update(self.world.get_rect())
        self.menu.update()

    def draw(self):
        self.all_sprites.draw(self.field)
        self.enemies.draw(self.field)
        self.menu.draw(self.screen)
        self.customer.draw(self.screen)

    def main_loop(self):
        while True:
            self.clock.tick(self.FPS)

            self.handle_events()
            self.update()
            self.screen.blit(self.field, self.field.get_rect())
            self.draw()
            pygame.display.update()
