import pygame
from Map.map import Map

# *----------------------------
player_img = pygame.image.load('Packman/pacmanOpen.png')
player_mini_img = pygame.transform.scale(player_img, (35, 35))
# *----------------------------

class Packman:
    def __init__(self, pos, shift, filename, hp):
        self.hp = hp  # кол-во жизней
        self.pos = pos
        self.shift = shift  # то, куда пакман будет постоянно идти
        self.cash_shift = shift
        self.direction = ''  # то же самое, что и сверху, но понятнее
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
        self.angle = 0

    def get_position(self):
        return self.pos

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        text = pygame.font.SysFont('ubuntu', 30).render('Heath: ' + str(self.get_hp()), True, (255, 255, 255))
        screen.blit(text, (425, 170))

    def draw_pac_img(self, screen):  # функция отрисовки жизней пакмена
        for i in range(self.get_hp()):
            x_i = 425
            img_rect = player_mini_img.get_rect()
            img_rect.x = x_i + 50 * i
            img_rect.y = 220
            screen.blit(player_mini_img, img_rect)

    def set_angle(self, angle):
        self.angle = 360 - self.angle
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.angle = angle
        self.image = pygame.transform.rotate(self.image, self.angle)

    def set_shift_and_angle(self, key, shift, angle, event, matrix):
        if (event.key == key):
            if matrix[self.pos[1] // 30 + shift[1]][self.pos[0] // 30 + shift[0]] == 0 and \
                    matrix[(self.pos[1] + 29) // 30 + shift[1]][(self.pos[0] + 29) // 30 + shift[0]] == 0:
                self.shift = shift
                self.set_angle(angle)
            self.cash_shift = shift

    def event(self, event):  # надо убрать дублирование кода если это возможно
        if (event.type == pygame.KEYDOWN):
            self.set_shift_and_angle(pygame.K_DOWN, [0, 1], 270, event, Map().matrix)
            self.set_shift_and_angle(pygame.K_UP, [0, -1], 90, event, Map().matrix)
            self.set_shift_and_angle(pygame.K_LEFT, [-1, 0], 180, event, Map().matrix)
            self.set_shift_and_angle(pygame.K_RIGHT, [1, 0], 0, event, Map().matrix)

    def logic(self, matrix):  # проверка коллизии
        if (matrix[self.pos[1] // 30 + self.cash_shift[1]][self.pos[0] // 30 + self.cash_shift[0]] == 0 and
            matrix[(self.pos[1] + 29) // 30 + self.cash_shift[1]][
                (self.pos[0] + 29) // 30 + self.cash_shift[0]]) == 0 and \
                matrix[(self.pos[1]) // 30 + self.cash_shift[1]][(self.pos[0] + 29) // 30 + self.cash_shift[0]] == 0 and \
                matrix[(self.pos[1] + 29) // 30 + self.cash_shift[1]][(self.pos[0]) // 30 + self.cash_shift[0]] == 0:
            self.shift = self.cash_shift
            if (self.shift == [0, 1]):
                self.set_angle(270)
            if (self.shift == [0, -1]):
                self.set_angle(90)
            if (self.shift == [1, 0]):
                self.set_angle(0)
            if (self.shift == [-1, 0]):
                self.set_angle(180)
        if matrix[self.pos[1] // 30][self.pos[0] // 30] == 1 or matrix[(self.pos[1] + 29) // 30][
            (self.pos[0] + 29) // 30] == 1 or matrix[(self.pos[1] + 29) // 30][(self.pos[0]) // 30] == 1 or \
                matrix[(self.pos[1]) // 30][(self.pos[0] + 29) // 30] == 1:
            self.pos = [self.pos[0] - self.shift[0],
                        self.pos[1] - self.shift[1]]  # отодвинуть пакмана назад при коллизии с клеткой
            self.shift = [0, 0]

        self.move()

    def move(self):
        self.pos[0] += self.shift[0]
        self.pos[1] += self.shift[1]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 30, 30)

    def get_hp(self):
        return self.hp

    def damag(self):  # вызываете когда пакмен должен получить урон
        self.hp -= 1

    def hps(self):  # проверка на то умер ли пакмен
        from all_vatiable import map
        if self.get_hp() <= 0 or len(map.seeds) == 0:  # смерть пакмена
            # self.pos = [0, 0]
            self.hp = 3
            # self.image = pygame.image.load("Packman/pacmanDead.png").convert()
            return True
        return False
