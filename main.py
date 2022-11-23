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
        self.steps = 0

    def activate(self):
        self.rect.top = self.pos[0]
        self.rect.left = self.pos[1]

    def draw(self, screen):
        screen.blit(self.image, [self.rect.top, self.rect.left])
    def step(self):
        self.rect.top += self.shift[0]
        self.rect.left += self.shift[1]

    def move_1(self, screen):
        self.step()
        self.draw(screen)
        self.steps += 0.75
        if self.steps % 100 == 0:
            self.shift[1] *= -1
            self.shift[0] *= -1
        if self.steps % 50 == 0:
            self.shift[0], self.shift[1] = self.shift[1], self.shift[0]
def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode([Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT])
    ghost_1 = Ghost([530, 30],[0, 1], "ghost.png")
    ghost_1.activate()
    # Основной цикл программы
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        screen.fill(Settings.BACKGROUND_COLOR)
        ghost_1.move_1(screen)
        pygame.display.flip()
        pygame.time.wait(3)
    exit(0)

if __name__ == '__main__':
    main()
