import pygame
from Map.map import Map
class Packman:
    def __init__(self, pos, shift, filename):
        self.pos = pos
        self.shift = shift # то, куда пакман будет постоянно идти
        self.cash_shift = shift
        self.direction = '' # то же самое, что и сверху, но понятнее
        self.image = pygame.image.load(filename).convert()
        self.rect = pygame.Rect(pos[0], pos[1], 25, 25)
        self.angle = 0

    def get_position(self):
        return self.pos

    def draw(self, screen):
        screen.blit(self.image, self.rect)

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

    def logic(self, matrix): # проверка коллизии
        if matrix[self.pos[1] // 30][self.pos[0] // 30] == 1 or matrix[(self.pos[1] + 25) // 30][(self.pos[0] + 25) // 30] == 1 or matrix[(self.pos[1] + 25) // 30][(self.pos[0]) // 30] == 1 or matrix[(self.pos[1]) // 30][(self.pos[0] + 25) // 30] == 1:
            self.pos = [self.pos[0] - self.shift[0], self.pos[1] - self.shift[1]] # отодвинуть пакмана назад при коллизии с клеткой
            self.shift = [0, 0]
        # if(matrix[self.pos[1] // 30 + self.shift[0]][self.pos[0] // 30 + self.shift[1]] == 1):
        #     self.
        print((self.pos[1] + 5) // 30 + self.shift[0], (self.pos[0] + 5) // 30 + self.shift[1])
        # pygame.draw.rect(screen, (255, 255, 255), ((self.pos[1] + 5) // 30 + self.shift[0], (self.pos[0] + 5) // 30 + self.shift[1]), 30, 30)
        self.move()

    def move(self):
        self.pos[0] += self.shift[0]
        self.pos[1] += self.shift[1]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 25, 25)

