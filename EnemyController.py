from Enemy import Enemy
import pygame


class EnemyController(object):
    def __init__(self, game):
        self.enemies = pygame.sprite.Group()
        self.game = game
        self.waypoints = game.world.get_waypoints()
        self.start = game.world.get_starting_position()
        self.last = game.world.get_last_position()
        self.n_wave = 1
        self.wave_len = 5
        self.num_enemies = 0
        pygame.time.set_timer(1, 200)

    def get_enemies(self):
        return self.enemies.sprites()

    def get_group(self):
        return self.enemies

    def update(self, bounds):
        self.enemies.update(bounds)
        for enemy in self.enemies.sprites():
            cur = enemy.get_current_waypoint()
            if enemy.visited:
                enemy.visited = False
                if cur + 1 == len(self.waypoints):
                    enemy.kill()
                else:
                    enemy.update_current_waypoint(self.waypoints[cur], self.waypoints[cur + 1])

    def draw(self, surface):
        self.enemies.draw(surface)

    def spawn(self):
        if self.wave_len == self.num_enemies:
            return True
        else:
            self.num_enemies += 1
            new_enemy = Enemy(self.start, num_waypoints=len(self.waypoints))
            new_enemy.set_destination(self.waypoints[0])
            new_enemy.activate()
            self.enemies.add(new_enemy)
            return False
