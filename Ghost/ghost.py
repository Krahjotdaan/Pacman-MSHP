import random
import pygame


class Ghost:
    def __init__(self, pos, filename):
        self.pos = pos #координаты
        self.shift = [0, 0] #смещение по осям x и y
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.steps = 0 #количество шагов (смещений)
        self.dir = random.randint(1,4) #направление для рандомного движения

    def activate(self):#возвращение к начальной позиции и настройкам призрака
        self.rect.top = self.pos[0]
        self.rect.left = self.pos[1]
        self.steps = 0
        self.shift = [0, 0]

    def draw(self, screen):#отрисовка
        screen.blit(self.image, [self.rect.top, self.rect.left])

    def step(self):#перемещение на 1 пиксель и подсчет шагов
        self.rect.top += self.shift[0]
        self.rect.left += self.shift[1]
        self.steps += 1

    def move_left(self):#движение влево
        self.shift[0] = -1
        self.shift[1] = 0
        self.step()

    def move_right(self):#движение вправо
        self.shift[0] = 1
        self.shift[1] = 0
        self.step()

    def move_up(self):#движение вверх
        self.shift[0] = 0
        self.shift[1] = -1
        self.step()

    def move_down(self):#движение вниз
        self.shift[0] = 0
        self.shift[1] = 1
        self.step()

    def stop(self):#движение остановка
        self.shift = [0, 0]

    def move_1(self, screen):#движение к выходу из прямоугольника для 1 призрака
        self.draw(screen)
        if self.steps < 90:
            self.move_right()
        elif (self.steps >= 90) and (self.steps < 110):
            self.move_up()
        elif self.steps == 110:
            self.stop()

    def move_2(self, screen):#движение к выходу из прямоугольника для 2 призрака
        self.draw(screen)
        if self.steps < 120:
            self.move_up()
        elif (self.steps >= 120) and (self.steps < 210):
            self.move_right()
        elif (self.steps >= 210) and (self.steps < 230):
            self.move_up()
        elif self.steps == 230:
            self.stop()

    def move_3(self, screen):#движение к выходу из прямоугольника для 3 призрака
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

    def move_4(self, screen):#движение к выходу из прямоугольника для 4 призрака
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

    def out_1(self):#проверка вышел ли 1 призрак
        if self.steps == 110:
            return True
        else:
            return False

    def move_random(self, screen):#изменение направления движения рандомно
        if self.steps % 120 == 0:
            self.dir = random.randint(1, 4)
        self.direction(screen, self.dir)

    def direction(self, screen, rand):#движение рандомно
        if rand == 1:
            self.draw(screen)
            self.move_up()
        if rand == 2:
            self.draw(screen)
            self.move_down()

        if rand == 3:
            self.draw(screen)
            self.move_left()

        if rand == 4:
            self.draw(screen)
            self.move_right()

    def out_2(self):#проверка вышел ли 2 призрак
        if self.steps == 230:
            return True
        else:
            return False

    def out_3(self):#проверка вышел ли 3 призрак
        if self.steps == 410:
            return True
        else:
            return False

    def out_4(self):#проверка вышел ли 4 призрак
        if self.steps == 530:
            return True
        else:
            return False

#################################################################################
#Реализация в мэин

