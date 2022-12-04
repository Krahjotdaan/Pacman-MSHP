import pygame

class Settings:
    BACKGROUND_COLOR = pygame.Color('black')
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 900
class Ghost:
    def __init__(self, pos, filename):
        self.pos = pos
        self.shift = [0, 0]
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.steps = 0

    def activate(self):
        self.rect.top = self.pos[0]
        self.rect.left = self.pos[1]
        self.steps = 0
        self.shift = [0, 0]

    def draw(self, screen):
        screen.blit(self.image, [self.rect.top, self.rect.left])

    def step(self):
        self.rect.top += self.shift[0]
        self.rect.left += self.shift[1]
        self.steps += 1

    def move_left(self):
        self.shift[0] = -1
        self.shift[1] = 0
        self.step()

    def move_right(self):
        self.shift[0] = 1
        self.shift[1] = 0
        self.step()

    def move_up(self):
        self.shift[0] = 0
        self.shift[1] = -1
        self.step()

    def move_down(self):
        self.shift[0] = 0
        self.shift[1] = 1
        self.step()

    def stop(self):
        self.shift = [0, 0]

    def move_1(self, screen):
        self.draw(screen)
        if self.steps < 90:
            self.move_right()
        elif (self.steps >= 90) and (self.steps < 110):
            self.move_up()
        elif self.steps == 110:
            self.stop()

    def move_2(self, screen):
        self.draw(screen)
        if self.steps < 120:
            self.move_up()
        elif (self.steps >= 120) and (self.steps < 210):
            self.move_right()
        elif (self.steps >= 210) and (self.steps < 230):
            self.move_up()
        elif self.steps == 230:
            self.stop()

    def move_3(self, screen):
        self.draw(screen)
        if self.steps < 180:
            self.move_left()
        elif (self.steps >= 180) and (self.steps < 300):
            self.move_up()
        elif (self.steps >= 300) and (self.steps < 390):
            self.move_right()
        elif (self.steps >= 390) and (self.steps < 410):
            self.move_up()
        elif self.steps == 410:
            self.stop()

    def move_4(self, screen):
        self.draw(screen)
        if self.steps < 120:
            self.move_down()
        elif (self.steps >= 120) and (self.steps < 300):
            self.move_left()
        elif (self.steps >= 300) and (self.steps < 420):
            self.move_up()
        elif (self.steps >= 420) and (self.steps < 510):
            self.move_right()
        elif (self.steps >= 510) and (self.steps < 530):
            self.move_up()
        elif self.steps == 530:
            self.stop()

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode([Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT])
    ghost_1 = Ghost([480, 390], "ghost_2.png")
    ghost_1.activate()
    ghost_2 = Ghost([480, 510], "ghost_2.png")
    ghost_2.activate()
    ghost_3 = Ghost([660, 510], "ghost_2.png")
    ghost_3.activate()
    ghost_4 = Ghost([660, 390], "ghost_2.png")
    ghost_4.activate()
    # Основной цикл программы
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        screen.fill(Settings.BACKGROUND_COLOR)
        ghost_1.move_1(screen)
        ghost_2.move_2(screen)
        ghost_3.move_3(screen)
        ghost_4.move_4(screen)
        pygame.display.flip()
        pygame.time.wait(3)
    exit(0)

if __name__ == '__main__':
    main()
