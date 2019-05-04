import os

import pygame


class SoundController:
    def __init__(self):
        self.background = os.path.join('assets', 'sounds', 'background.ogg')
        pygame.mixer_music.load(self.background)
        pygame.mixer_music.play(-1)
