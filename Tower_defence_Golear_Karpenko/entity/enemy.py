from Tower_defence_Golear_Karpenko import config
from Tower_defence_Golear_Karpenko.base_classes import sprite
from Tower_defence_Golear_Karpenko.base_classes.coordinate import Coordinate


def normalize(heading):
    normal = (heading[0] ** 2 + heading[1] ** 2) ** 0.5
    return heading / normal


class Enemy(sprite.Sprite):
    def __init__(self, position, size=config.TILE_SIZE + config.ENEMY_SIZE_DIFF,
                 image='enemy.png', num_waypoints=0):
        super().__init__(position, size, image)
        self.speed = config.ENEMY_SPEED_DEFAULT
        self.current_waypoint = 1
        self.num_waypoints = num_waypoints
        self.destination = Coordinate(0, 0)
        self.heading = Coordinate(1, 0)
        self.visited = False
        self.life = config.ENEMY_LIFE_DEFAULT
        self.is_active = False

    def set_destination(self, destination):
        self.destination = destination
        self.set_heading(destination)

    def get_destination(self):
        return self.destination

    def get_current_waypoint(self):
        return self.current_waypoint

    def update_current_waypoint(self, cur_waypoint, next_waypoint):
        self.current_waypoint += 1
        if self.current_waypoint == self.num_waypoints:
            self.kill()
        else:
            self.destination = next_waypoint
            self.heading = next_waypoint - cur_waypoint
            self.heading = normalize(self.heading)

    def activate(self):
        self.is_active = True

    def is_on_waypoint(self):
        return self.position == self.heading

    def attacked(self, damage):
        self.life -= damage
        if self.life <= 0:
            self.kill()

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    def get_heading(self):
        return self.heading

    def set_heading(self, heading):
        self.heading = heading - self.position
        self.heading = normalize(self.heading)

    def get_life(self):
        return self.life

    def out_of_bounds(self, bounds):
        if (self.rect.left > bounds.right
                or self.rect.right < bounds.left
                or self.rect.bottom < bounds.top
                or self.rect.top > bounds.bottom):
            return True
        return False

    def update(self, bounds):
        if not self.is_active:
            return None
        if self.out_of_bounds(bounds):
            self.kill()
        steps = self.speed

        while steps > 0:
            self.move(*self.heading)
            steps -= 1
            if self.position == self.destination:
                self.visited = True
                break
