import pygame

class Settings:
    BACKGROUND_COLOR = pygame.Color('black')
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
class Packman:
    def __init__(self, pos, shift, filename):
        self.pos = pos
        self.shift = shift
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
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
