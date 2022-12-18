import pygame

gridDisplay = pygame.display.set_mode((1200, 900))


class Settings:
    BACKGROUND_COLOR = pygame.Color('black')
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 900
    SCORE = 0
    scene_changed = True
    scene_index = 0


def Score():
    return Settings.SCORE
