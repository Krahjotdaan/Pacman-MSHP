import pygame

GRID_NODE_WIDTH = 30
GRID_NODE_HEIGHT = 30
gridDisplay = pygame.display.set_mode((1200, 900))
pygame.display.get_surface().fill((200, 200, 200))  # background

class Settings:
    BACKGROUND_COLOR = pygame.Color('black')
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 900
    scene_changed = True
    scene_index = 0
