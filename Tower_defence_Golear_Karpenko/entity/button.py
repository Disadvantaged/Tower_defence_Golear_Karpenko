import os

import Tower_defence_Golear_Karpenko.base_classes.command as command
from Tower_defence_Golear_Karpenko import config
from Tower_defence_Golear_Karpenko.base_classes.sprite import Sprite


class Button(Sprite):
    def __init__(self, position=(0, 0), image=None, command_type=command.Command):
        if image is not None:
            image = os.path.join(config.BUTTON_PATH, image)
        super().__init__(position, (config.BUTTON_WIDTH,
                                    config.BUTTON_HEIGHT), image)
        self.command = command_type()
        self.is_activated = True

    def activate(self):
        self.is_activated = True

    def deactivate(self):
        self.is_activated = False

    def action(self, pos):
        self.command.action(is_activated=self.is_activated)


class ExitButton(Button):
    def __init__(self, position):
        super().__init__(position, 'quit.png', command.CommandExit)


class NewWaveButton(Button):
    def __init__(self, position):
        super().__init__(position, 'nextWave.png', command.CommandNewWave)


class PlayButton(Button):
    def __init__(self, position):
        super().__init__(position, 'play.png', command.CommandPlay)
