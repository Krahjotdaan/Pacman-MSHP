import pygame

class Settings:
    def __init__(self):
        self.BACKGROUND_COLOR = pygame.Color('black')
        self.WINDOW_WIDTH = 1200
        self.WINDOW_HEIGHT = 900
        self.scene_changed = True
        self.scene_index = 0
        self.number_of_seeds = 517
