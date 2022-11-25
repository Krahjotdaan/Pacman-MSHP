import pygame

class Settings:
    BACKGROUND_COLOR = pygame.Color('black')
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
class Map:
    def __init__(self):
        self.matric = []
def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode([Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT])


    # Основной цикл программы
    game_over = False
    while not game_over:
        # обработка событий
        for event in pygame.event.get():
            game_over = check_for_exit(event)

        screen.fill(Settings.BACKGROUND_COLOR)
        pygame.display.flip()
    exit(0)
def check_for_exit(event):
    return event.type == pygame.QUIT
if __name__ == '__main__':
    main()
