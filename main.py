import pygame

import settings
from settings import Settings

from Map.map import Map
my_map = Map()

gridDisplay = pygame.display.set_mode((1200, 900))
pygame.display.get_surface().fill((200, 200, 200))  # background


def main():
    # Основной цикл программы
    game_over = False
    while not game_over:
        # обработка событий
        for event in pygame.event.get():
            game_over = check_for_exit(event)
        screen = pygame.display.set_mode([Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT])
        pygame.display.flip()

    exit(0)

def check_for_exit(event):
    return event.type == pygame.QUIT

if __name__ == '__main__':
    main()