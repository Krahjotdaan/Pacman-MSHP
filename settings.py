import pygame

gridDisplay = pygame.display.set_mode((1200, 900))


def createSquare(x, y, color, grid_node_width=30, grid_node_height=30):
    pygame.draw.rect(gridDisplay, color, [x, y, grid_node_width, grid_node_height])


class Settings:
    BACKGROUND_COLOR = pygame.Color('black')
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 900
    SCORE = 0


def Score():
    return Settings.SCORE
