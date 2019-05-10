import logging

import pygame

from Tower_defence_Golear_Karpenko import config
from Tower_defence_Golear_Karpenko.entity.enemy import Enemy


class EnemyController(object):
    def __init__(self, waypoints):
        self.enemies = pygame.sprite.Group()
        self.waypoints = waypoints
        self.start = waypoints[0]
        self.last = waypoints[-1]
        self.current_wave = 0
        self.max_wave = config.ENEMY_MAX_WAVE
        self.wave_len = config.ENEMY_WAVE_LEN
        self.num_enemies = 0
        self.finished = True

    def get_enemies(self):
        return self.enemies.sprites()

    def reset(self):
        pygame.time.set_timer(config.ENEMY_SPAWN_EVENT,
                              config.ENEMY_SPAWN_DELAY)
        self.num_enemies = 0
        self.current_wave += 1
        if self.current_wave != 1:
            self.wave_len = int(self.wave_len * config.ENEMY_COEFFICIENT)
        self.finished = False

    def set_wave_len(self, wave_len):
        self.wave_len = wave_len

    def get_group(self):
        return self.enemies

    def update(self, bounds):
        if not self.enemies and not self.finished:
            self.finished = True
        else:
            self.enemies.update(bounds)
            for enemy in self.enemies.sprites():
                cur = enemy.get_current_waypoint()
                if enemy.visited:
                    enemy.visited = False
                    if cur + 1 == len(self.waypoints):
                        enemy.kill()
                        logging.info('%d', self.num_enemies)
                        if self.check_for_win():
                            config.GAME.win()
                        self.num_enemies -= 1
                        config.GAME.customer.money -= config.ENEMY_COST
                        if config.GAME.customer.money <= 0:
                            config.GAME.set_lost()
                    else:
                        enemy.update_current_waypoint(self.waypoints[cur],
                                                      self.waypoints[cur + 1])

    def check_for_win(self):
        return self.num_enemies == 0 and self.current_wave == self.max_wave

    def draw(self, surface):
        self.enemies.draw(surface)

    def clear(self):
        self.enemies.empty()
        pygame.time.set_timer(config.ENEMY_SPAWN_EVENT, 0)
        self.num_enemies = 0
        self.wave_len = config.ENEMY_WAVE_LEN
        self.current_wave = 0
        self.finished = True

    def spawn(self):
        if self.wave_len != self.num_enemies:
            self.finished = False
            self.num_enemies += 1
            new_enemy = Enemy(self.start, num_waypoints=len(self.waypoints))
            new_enemy.set_destination(self.waypoints[1])
            new_enemy.activate()
            self.enemies.add(new_enemy)
            return False
        return True
