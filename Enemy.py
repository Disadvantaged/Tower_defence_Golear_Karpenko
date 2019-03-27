import Rectangle
import config


def normalize(heading):
    normal = (heading[0] ** 2 + heading[1] ** 2) ** 0.5
    return heading[0] / normal, heading[1] / normal


class Enemy(Rectangle.Rectangle):
    def __init__(self, position, size=config.DEFAULT_ENEMY_SIZE, image='default_enemy.png', num_waypoints=0):
        super().__init__(position, size, image)
        self.speed = config.DEFAULT_ENEMY_SPEED
        self.current_waypoint = 0
        self.num_waypoints = num_waypoints
        self.destination = (0, 0)
        self.heading = (1, 0)
        self.visited = False
        self.life = config.DEFAULT_ENEMY_LIFE
        self.is_active = False
        print('qwe')

    def set_destination(self, destination):
        self.destination = destination
        self.set_heading(destination)

    def get_destination(self):
        return self.destination

    def get_current_waypoint(self):
        return self.current_waypoint

    def update_current_waypoint(self, cur_waypoint, next_waypoint):
        print('1')
        self.current_waypoint += 1
        if self.current_waypoint == self.num_waypoints:
            self.kill()
        else:
            print(cur_waypoint, next_waypoint)
            self.destination = next_waypoint
            self.heading = next_waypoint[0] - cur_waypoint[0], next_waypoint[1] - cur_waypoint[1]
            self.heading = normalize(self.heading)
            print(self.heading)

    def activate(self):
        self.is_active = True

    def is_on_waypoint(self):
        return self.position == self.heading

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    def get_heading(self):
        return self.heading

    def set_heading(self, heading):
        self.heading = heading[0] - self.position[0], heading[1] - self.position[1]
        self.heading = normalize(self.heading)
        print(self.heading)

    def get_life(self):
        return self.life

    def out_of_bounds(self, bounds):
        if (self.rect.left > bounds.right or self.rect.right < bounds.left
                or self.rect.bottom < bounds.top or self.rect.top > bounds.bottom):
            return True
        return False

    def update(self, bounds):
        if not self.is_active:
            return None
        if self.out_of_bounds(bounds):
            self.kill()
        steps = self.speed
        while steps > 0:
            self.move(self.heading[0] * 1, self.heading[1] * 1)
            steps -= 1
            if self.position == self.destination:
                self.visited = True
                break
