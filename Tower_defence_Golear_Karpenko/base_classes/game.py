import logging

import pygame

from Tower_defence_Golear_Karpenko import config
from Tower_defence_Golear_Karpenko.base_classes.coordinate import Coordinate
from Tower_defence_Golear_Karpenko.base_classes.menu import Menu
from Tower_defence_Golear_Karpenko.base_classes.world import World
from Tower_defence_Golear_Karpenko.entity_controller.customer import Customer
from Tower_defence_Golear_Karpenko.entity_controller.enemy_controller \
    import EnemyController
from Tower_defence_Golear_Karpenko.misc.fps_counter import FPSCounter
from Tower_defence_Golear_Karpenko.misc.sound_controller import SoundController


class Game:
    """
    Basic game class. Keeps information of all the game data.
    Handles user input and main loop
    """

    def __init__(self):
        self.screen = pygame.display.set_mode(
            (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption(config.TITLE)
        self.field = pygame.Surface((config.FIELD_WIDTH, config.FIELD_HEIGHT))

        self.clock = pygame.time.Clock()
        self.sound_controller = SoundController()
        self.FPS = config.FPS
        config.FONT = pygame.font.Font(None, config.FONT_SIZE)
        self.fps_counter = FPSCounter(self.clock, pos=Coordinate(5, 5))
        self.caption = config.TITLE
        self.game_started = False

        self.all_sprites = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()

        self.world = None
        self.load()
        self.world.set_rect(self.screen.blit(self.field, Coordinate(0, 0)))
        self.menu = Menu((0, config.FIELD_HEIGHT),
                         config.MENU_WIDTH, config.MENU_HEIGHT)
        self.customer = Customer()
        logging.info('loaded game data')
        config.ENEMY_SPAWN_EVENT = pygame.USEREVENT + 1
        self.enemies = EnemyController(self.world.get_waypoints())

    def start_game(self):
        logging.info('game started')
        self.customer.reset()

        self.enemies.clear()
        self.enemies.reset()
        self.world.clear()
        self.menu.start_game()

        self.game_started = True

    def win(self):
        self.game_started = False
        self.menu.win()

    def load(self):
        """
        Loads data from assets.
        """
        self.world = World(config.CURRENT_WORLD)
        for row in self.world.get_layout():
            self.tiles.add(*row)
            self.all_sprites.add(*row)

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
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                self.sound_controller.switch()

    def check_mouse_pressed(self, pos):
        """
        If player pressed left mouse button, checks if he pressed on a cell.
        :param pos: position of mouse click.
        """
        if (self.world.get_rect().collidepoint(pos)
                and self.customer.item_attached()):
            for cell in self.tiles.sprites():
                if (cell.get_rect().collidepoint(pos)
                        and cell.can_build
                        and self.customer.enough_money()):
                    tower = self.customer.buy_tower()
                    self.world.place_tower(tower, self.world.get_cell_position(
                        rect=cell.get_rect()))
                    logging.info('bought tower')
        elif self.menu.get_rect().collidepoint(pos):
            for item in self.menu.get_items():
                if item.get_rect().collidepoint(pos):
                    item.action(pos)

    def update(self):
        self.enemies.update(self.world.get_rect())
        self.menu.update()
        self.world.update()
        self.fps_counter.update()

    def set_lost(self):
        self.enemies.clear()
        self.menu.set_lost()
        self.customer.money = 0
        self.game_started = False

    def draw(self):
        self.screen.blit(self.field, self.field.get_rect())
        self.all_sprites.draw(self.field)
        self.enemies.draw(self.field)
        self.menu.draw(self.screen)
        if self.customer.item_attached():
            pos = Coordinate(pygame.mouse.get_pos())
            pos = (pos - self.customer.item.get_size() // 2)
            self.screen.blit(self.customer.item.get_image(), pos)
        self.fps_counter.draw(self.screen)

    def main_loop(self):
        while True:
            self.clock.tick(self.FPS)
            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
