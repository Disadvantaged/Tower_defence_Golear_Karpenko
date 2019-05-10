import os

import pygame

from Tower_defence_Golear_Karpenko import config


class SoundController:
    def __init__(self):
        self.background = os.path.join(config.CWD, 'assets',
                                       'sounds', 'background.ogg')
        self.is_playing = config.DEFAULT_MUSIC_PLAY
        if self.is_playing:
            pygame.mixer_music.load(self.background)
            pygame.mixer_music.play(-1)

    def switch(self):
        if self.is_playing:
            pygame.mixer_music.pause()
            self.is_playing = False
        else:
            self.is_playing = True
            pygame.mixer_music.unpause()
