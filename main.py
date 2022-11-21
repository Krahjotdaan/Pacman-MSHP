import pygame

class Settings:
    BACKGROUND_COLOR = pygame.Color('black')
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
class Packman:
    def __init__(self, pos, shift, filename):
        self.pos = pos
        self.shift = shift # то, куда пакман будет постоянно идти
        self.direction = '' # то же самое, что и сверху, но понятнее
        self.color = pygame.Color('yellow')
        # self.image = pygame.image.load(filename)
        # self.rect = self.image.get_rect()
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, 25, 0)
    def event(self, event):
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_DOWN):
                self.shift = [0, 1]
                self.direction = 'down'
            if (event.key == pygame.K_UP):
                self.shift = [0, -1]
                self.direction = 'up'

            if (event.key == pygame.K_LEFT):
                self.shift = [-1, 0]
                self.direction = 'left'

            if (event.key == pygame.K_RIGHT):
                self.shift = [1, 0]
                self.direction = 'right'

    def move(self):
        self.pos[0] += self.shift[0]
        self.pos[1] += self.shift[1]
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
