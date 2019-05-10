from Tower_defence_Golear_Karpenko.base_classes.sprite import Sprite
from Tower_defence_Golear_Karpenko import config


class Bullet(Sprite):
    def __init__(self, position, size=config.BULLET_SIZE_DEFAULT,
                 image=config.BULLET_IMAGE_DEFAULT):
        super().__init__(position, size, image)
        self.speed = config.BULLET_SPEED_DEFAULT

    def set_speed(self, speed):
        self.speed = speed
