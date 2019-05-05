import os

import pygame

import config


class SoundController:
    def __init__(self):
        self.background = os.path.join('assets', 'sounds', 'background.ogg')
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
