import pygame
import random
from Packman.packman import Packman
class Settings:
    BACKGROUND_COLOR = pygame.Color('black')
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 900

class Ghost:
    def __init__(self, pos, filename):
        self.pos = pos #координаты
        self.pos_matrix = [pos[0]//30+1, pos[1]//30+1]# координаты по матрице
        self.shift = [0, 0] #смещение по осям x и y
        self.shift_matrix = [0, 0]# смещение по матрице
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.steps = 0 # количество шагов (смещений)
        self.steps_matrix = 0 # количество шагов (смещений) по матрице
        self.dir = 0 #направление для рандомного движения
        self.chasing = False

    def activate(self):#возвращение к начальной позиции и настройкам призрака
        self.rect.top = self.pos[0]
        self.rect.left = self.pos[1]
        self.pos_matrix = [self.pos[0] // 30 + 1, self.pos[1] // 30 + 1]
        self.steps = 0
        self.steps_matrix = 0
        self.shift = [0, 0]
        self.chasing = False

    def draw(self, screen):#отрисовка
        screen.blit(self.image, [self.rect.top, self.rect.left])

    def step(self):#перемещение на 1 пиксель и подсчет шагов
        self.rect.top += self.shift[0]
        self.rect.left += self.shift[1]
        self.steps += 1
        if self.steps % 30 == 0:
            self.pos_matrix[0] += self.shift_matrix[0]
            self.pos_matrix[1] += self.shift_matrix[1]
            self.steps_matrix += 1

    def move_left(self):#движение влево
        self.shift[0] = -1
        self.shift[1] = 0
        self.shift_matrix[0] = -1
        self.shift_matrix[1] = 0
        self.step()
        self.dir = 3

    def move_right(self):#движение вправо
        self.shift[0] = 1
        self.shift[1] = 0
        self.shift_matrix[0] = 1
        self.shift_matrix[1] = 0
        self.step()
        self.dir = 4

    def move_up(self):#движение вверх
        self.shift[0] = 0
        self.shift[1] = -1
        self.shift_matrix[0] = 0
        self.shift_matrix[1] = -1
        self.step()
        self.dir = 1

    def move_down(self):#движение вниз
        self.shift[0] = 0
        self.shift[1] = 1
        self.shift_matrix[0] = 0
        self.shift_matrix[1] = 1
        self.step()
        self.dir = 2

    def stop(self):#движение остановка
        self.shift = [0, 0]
        self.shift_matrix = [0, 0]
        self.dir = 0

    def move_1(self, screen):#движение к выходу из прямоугольника для 1 призрака
        self.draw(screen)
        if self.steps_matrix < 3:
            self.move_right()
        elif (self.steps_matrix >= 3) and (self.steps_matrix < 5):
            self.move_up()
        elif self.steps_matrix == 5:
            self.stop()

    def move_2(self, screen):#движение к выходу из прямоугольника для 2 призрака
        self.draw(screen)
        if self.steps_matrix < 4:
            self.move_up()
        elif (self.steps_matrix >= 4) and (self.steps_matrix < 7):
            self.move_right()
        elif (self.steps_matrix >= 7) and (self.steps_matrix < 9):
            self.move_up()
        elif self.steps_matrix == 9:
            self.stop()

    def move_3(self, screen):#движение к выходу из прямоугольника для 3 призрака
        self.draw(screen)

        if self.steps_matrix < 6:
            self.move_left()
        elif (self.steps_matrix >= 6) and (self.steps_matrix < 10):
            self.move_up()
        elif (self.steps_matrix >= 10) and (self.steps_matrix < 13):
            self.move_right()
        elif (self.steps_matrix >= 13) and (self.steps_matrix < 15):
            self.move_up()
        elif self.steps_matrix == 15:
            self.stop()

    def move_4(self, screen):#движение к выходу из прямоугольника для 4 призрака
        self.draw(screen)
        if self.steps_matrix < 4:
            self.move_down()
        elif (self.steps_matrix >= 4) and (self.steps_matrix < 10):
            self.move_left()
        elif (self.steps_matrix >= 10) and (self.steps_matrix < 14):
            self.move_up()
        elif (self.steps_matrix >= 14) and (self.steps_matrix < 17):
            self.move_right()
        elif (self.steps_matrix >= 17) and (self.steps_matrix < 19):
            self.move_up()

        elif self.steps_matrix == 19:
            self.stop()

    def out_1(self):#проверка вышел ли 1 призрак
        if self.steps_matrix == 5:
            return True
        else:
            return False

    #НОВАЯ ФУНКЦИЯ ДВИЖЕНИЯ + КОЛЛЛИЗИЯ СО СТЕНКАМИ
    def move_random(self, screen, map):#изменение направления движения рандомно
        dirs = []
        change_dir = False
        if self.rect.top == (self.pos_matrix[0]-1)*30 and self.rect.left == (self.pos_matrix[1]-1)*30:
            if not map.is_wall(self.pos_matrix[1]-1, self.pos_matrix[0]):
                dirs.append(1)
            if not map.is_wall(self.pos_matrix[1]+1, self.pos_matrix[0]):
                dirs.append(2)
            if not map.is_wall(self.pos_matrix[1], self.pos_matrix[0]-1):
                dirs.append(3)
            if not map.is_wall(self.pos_matrix[1], self.pos_matrix[0]+1):
                dirs.append(4)
            change_dir = True
            if self.dir != 0:
                for i in range(len(dirs)):
                    if self.dir == dirs[i]:
                        change_dir = False
                        break
        else:
            dirs.append(0)

        if (change_dir or len(dirs)==3):
            self.draw(screen)
            index_dir = random.randint(0, len(dirs)-1)
            if dirs[index_dir] == 1:
                self.move_up()
            elif dirs[index_dir] == 2:
                self.move_down()
            elif dirs[index_dir] == 3:
                self.move_left()
            elif dirs[index_dir] == 4:
                self.move_right()
        else:
            self.draw(screen)
            if self.dir == 1:
                self.move_up()
            elif self.dir == 2:
                self.move_down()
            elif self.dir == 3:
                self.move_left()
            elif self.dir == 4:
                self.move_right()


    def out_2(self):#проверка вышел ли 2 призрак
        if self.steps_matrix == 9:
            return True
        else:
            return False

    def out_3(self):#проверка вышел ли 3 призрак
        if self.steps_matrix == 15:
            return True
        else:
            return False

    def out_4(self):#проверка вышел ли 4 призрак
        if self.steps_matrix == 19:
            return True
        else:
            return False

    def distance(self, pacman):
        delta_x = self.rect.top - pacman.pos[0]
        delta_y = self.rect.left - pacman.pos[1]
        return int(((abs(delta_x))**2+(abs(delta_y))**2)**0.5)

    def distance_x(self, pacman):
        return abs(self.rect.top - pacman.pos[0])

    def distance_y(self, pacman):
        return abs(self.rect.left - pacman.pos[1])

    def chase(self, pacman, map):
        self.chasing = True
        dirs = []
        if self.rect.top == (self.pos_matrix[0] - 1) * 30 and self.rect.left == (self.pos_matrix[1] - 1) * 30:
            if not map.is_wall(self.pos_matrix[1] - 1, self.pos_matrix[0]):
                dirs.append(1)
            if not map.is_wall(self.pos_matrix[1] + 1, self.pos_matrix[0]):
                dirs.append(2)
            if not map.is_wall(self.pos_matrix[1], self.pos_matrix[0] - 1):
                dirs.append(3)
            if not map.is_wall(self.pos_matrix[1], self.pos_matrix[0] + 1):
                dirs.append(4)
            if self.rect.top > pacman.pos[0]:

                for i in range(len(dirs)):
                    if dirs[i] == 3:

                        return 3
            elif self.rect.top < pacman.pos[0]:

                for i in range(len(dirs)):
                    if dirs[i] == 4:

                        return 4

            elif self.rect.left > pacman.pos[1]:

                for i in range(len(dirs)):
                    if dirs[i] == 1:

                        return 1
            elif self.rect.left < pacman.pos[1]:

                for i in range(len(dirs)):
                    if dirs[i] == 2:

                        return 2
            else:
                return self.dir
        else:
            return self.dir

        ###############

def ghosts_move_random(list_ghosts, screen, map):
    for ghost in list_ghosts:
        ghost.move_random(screen, map)

def ghosts_out(list_ghosts):
    if list_ghosts[0].out_1() and list_ghosts[1].out_2() and list_ghosts[2].out_3() and list_ghosts[
        3].out_4():  # проверка что вышли все призраки
        return True
    else:
        return False

def move_xy(list_ghosts, screen):
    list_ghosts[0].move_1(screen)
    list_ghosts[1].move_2(screen)
    list_ghosts[2].move_3(screen)
    list_ghosts[3].move_4(screen)

def gosts_activate(list_ghosts):
    for ghost in list_ghosts:
        ghost.activate()

def creating_ghosts():
    ghost_1 = Ghost([480, 390], "Ghost/ghost_2.png") #создание призраков
    ghost_2 = Ghost([480, 510], "Ghost/ghost_2.png")
    ghost_3 = Ghost([660, 510], "Ghost/ghost_2.png")
    ghost_4 = Ghost([660, 390], "Ghost/ghost_2.png")
    list_ghosts = [ghost_1, ghost_2, ghost_3, ghost_4]
    return list_ghosts


def check(Ghosts, pacman, map, timer):

    min_dist = 100000
    min_index = 0
    for i in range(len(Ghosts)):
        if Ghosts[i].distance(pacman) < min_dist:
            min_dist = Ghosts[i].distance(pacman)
            min_index = i
    if min_dist <= 500 or Ghosts[min_index].chasing:
        Ghosts[0].dir = Ghosts[0].chase(pacman, map)
        Ghosts[1].dir = Ghosts[1].chase(pacman, map)
        Ghosts[2].dir = Ghosts[2].chase(pacman, map)
        Ghosts[3].dir = Ghosts[3].chase(pacman, map)
        timer += 1
    return timer

def end_chasing(timer, Ghosts):
    if timer >= 7000:
        for i in range(len(Ghosts)):
            if Ghosts[i].chasing == True:
                Ghosts[i].chasing = False
        return 0
    else:
        return timer

def minus_life(pacman, Ghosts):
    for i in range(len(Ghosts)):
        if Ghosts[i].distance(pacman) >= 0 and Ghosts[i].distance(pacman) <= 1:
            for j in range(len(Ghosts)):
                Ghosts[j].activate()
            return True
