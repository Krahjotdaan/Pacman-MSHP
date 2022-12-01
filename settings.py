import pygame

gridDisplay = pygame.display.set_mode((800, 600))
def createSquare(x, y, color, grid_node_width = 20, grid_node_height = 20):
    pygame.draw.rect(gridDisplay, color, [x, y, grid_node_width, grid_node_height])

class Settings:
    BACKGROUND_COLOR = pygame.Color('black')
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

