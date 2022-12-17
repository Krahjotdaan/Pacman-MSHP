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

    def move_1(self):#движение к выходу из прямоугольника для 1 призрака
        # self.draw(screen)
        if self.steps < 90:
            self.move_right()
        elif (self.steps >= 90) and (self.steps < 110):
            self.move_up()
        elif self.steps == 110:
            self.stop()

    def move_2(self):#движение к выходу из прямоугольника для 2 призрака
        # self.draw(screen)
        if self.steps < 120:
            self.move_up()
        elif (self.steps >= 120) and (self.steps < 210):
            self.move_right()
        elif (self.steps >= 210) and (self.steps < 230):
            self.move_up()
        elif self.steps == 230:
            self.stop()

    def move_3(self):#движение к выходу из прямоугольника для 3 призрака
        # self.draw(screen)
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

    def move_4(self):#движение к выходу из прямоугольника для 4 призрака
        # self.draw(screen)
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



    def move_random(self):#изменение направления движения рандомно
        if self.steps % 120 == 0:
            self.dir = random.randint(1, 4)
        self.direction(self.dir)

    def direction(self, rand):#движение рандомно
        if rand == 1:
            # self.draw(screen)
            self.move_up()
        if rand == 2:
            # self.draw(screen)
            self.move_down()

        if rand == 3:
            # self.draw(screen)
            self.move_left()

        if rand == 4:
            # self.draw(screen)
            self.move_right()

    def out_1(self):#проверка вышел ли 1 призрак
        return self.steps == 110
    def out_2(self):#проверка вышел ли 2 призрак
        return self.steps == 230

    def out_3(self):#проверка вышел ли 3 призрак
        return self.steps == 410

    def out_4(self):#проверка вышел ли 4 призрак
        return self.steps == 530

#################################################################################
#Реализация в мэин
    def ghosts_move_random(list_ghosts):
        for ghost in list_ghosts:
            ghost.move_random()

    def ghosts_out(list_ghosts):
        if list_ghosts[0].out_1() and list_ghosts[1].out_2() and list_ghosts[2].out_3() and list_ghosts[3].out_4():  # проверка что вышли все призраки
            return True
        else:
            return False

    def move_xy(list_ghosts):
        list_ghosts[0].move_1()
        list_ghosts[1].move_2()
        list_ghosts[2].move_3()
        list_ghosts[3].move_4()

    def creating_ghosts():
        ghost_1 = Ghost([480, 390], "Ghost/ghost_2.png")  # создание призраков
        ghost_2 = Ghost([480, 510], "Ghost/ghost_2.png")
        ghost_3 = Ghost([660, 510], "Ghost/ghost_2.png")
        ghost_4 = Ghost([660, 390], "Ghost/ghost_2.png")
        list_ghosts = [ghost_1, ghost_2, ghost_3, ghost_4]
        return list_ghosts

    def gosts_activate(list_ghosts):
        for ghost in list_ghosts:
            ghost.activate()

