import pygame

class Settings:
    BACKGROUND_COLOR = pygame.Color('black')
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
class Ghost:
    def __init__(self, pos, shift, filename):
        self.pos = pos
        self.shift = shift
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode([Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT])
    ghost_1 = Ghost((800, 0),(0, 1), "ghost.png")

    # Основной цикл программы
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
    exit(0)

if __name__ == '__main__':
    main()
