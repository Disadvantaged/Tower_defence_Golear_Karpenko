from Enemy import Enemy
import pygame


class EnemyController(object):
    def __init__(self, game):
        self.enemies = pygame.sprite.Group()
        self.waypoints = game.world.get_waypoints()
        self.start = game.world.get_starting_position()
        self.last = game.world.get_last_position()
        enemy = Enemy(self.start, game.world.get_tile_size(), 'grass.png', num_waypoints=len(self.waypoints))
        enemy.set_destination(self.waypoints[0])
        self.enemies.add(enemy)
        for elem in self.enemies.sprites():
            elem.activate()

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
