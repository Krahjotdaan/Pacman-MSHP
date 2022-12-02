import pygame
from Map.map import Map
class Packman:
    def __init__(self, pos, shift, filename):
        self.pos = pos
        self.shift = shift # то, куда пакман будет постоянно идти
        self.direction = '' # то же самое, что и сверху, но понятнее
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
        self.angle = 0

    def draw(self, screen):
        screen.blit(self.image, self.pos)

    def set_angle(self, angle):
        self.angle = 360 - self.angle
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.angle = angle
        self.image = pygame.transform.rotate(self.image, self.angle)

    def set_shift_and_angle(self, key, shift, angle, event):
        if (event.key == key):
            self.shift = shift
            self.set_angle(angle)

    def event(self, event): # надо убрать дублирование кода если это возможно
        if(event.type == pygame.KEYDOWN):
            self.set_shift_and_angle(pygame.K_DOWN, [0, 1], 270, event)
            self.set_shift_and_angle(pygame.K_UP, [0, -1], 90, event)
            self.set_shift_and_angle(pygame.K_LEFT, [-1, 0], 180, event)
            self.set_shift_and_angle(pygame.K_RIGHT, [1, 0], 0, event)

    def move(self):
        self.pos[0] += self.shift[0]
        self.pos[1] += self.shift[1]

# def main():
#     pygame.init()
#     pygame.font.init()
#     screen = pygame.display.set_mode([Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT])
#
#
#     # Основной цикл программы
#     game_over = False
#     while not game_over:
#         pass
#     exit(0)
#
# if __name__ == '__main__':
#     main()
