import pygame

class Settings:
    BACKGROUND_COLOR = pygame.Color('black')
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode([Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT])


    # Основной цикл программы
    game_over = False
    while not game_over:
        pass
    exit(0)

if __name__ == '__main__':
    main()
