import pygame
import random
from Nemap import Map
class Settings:
    BACKGROUND_COLOR = pygame.Color('black')
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 900
class Ghost:
    def __init__(self, pos, filename):
        self.pos = pos #координаты
        self.shift = [0, 0] #смещение по осям x и y
        self.shift_matrix = [0, 0]
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.steps = 0 #количество шагов (смещений)
        self.dir = random.randint(1,4) #направление для рандомного движения
        self.pos_matrix = [pos[0]//30, pos[1]//30]
    def activate(self):#возвращение к начальной позиции и настройкам призрака
        self.rect.top = self.pos[0]
        self.rect.left = self.pos[1]
        self.steps = 0
        self.steps_matrix = 0
        self.shift = [0, 0]

    def draw(self, screen):#отрисовка
        screen.blit(self.image, [self.rect.top, self.rect.left])

    def step(self):#перемещение на 1 пиксель и подсчет шагов
        self.rect.top += self.shift[0]
        self.rect.left += self.shift[1]
        self.steps += 1
        if self.steps % 30 == 0:
            self.pos_matrix[0] += self.shift_matrix[0]
            self.pos_matrix[0] += self.shift_matrix[0]
            self.steps_matrix += 1

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
            print(self.steps_matrix)

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


def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode([Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT])
    ghost_1 = Ghost([480, 390], "ghost_2.png") #создание призраков
    ghost_1.activate()
    ghost_2 = Ghost([480, 510], "ghost_2.png")
    ghost_2.activate()
    ghost_3 = Ghost([660, 510], "ghost_2.png")
    ghost_3.activate()
    ghost_4 = Ghost([660, 390], "ghost_2.png")
    ghost_4.activate()
    out = False #показывает вышли призраки или нет
    # Основной цикл программы
    map = Map()
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        screen.fill(Settings.BACKGROUND_COLOR)
        #pygame.display.get_surface().fill((200, 200, 200))
        map.visualizeGrid()
        if out:#если все призраки вышли
            ghost_1.move_random(screen)
            ghost_2.move_random(screen)
            ghost_3.move_random(screen)
            ghost_4.move_random(screen)
            out = True
        else:
            ghost_1.move_1(screen)
            ghost_2.move_2(screen)
            ghost_3.move_3(screen)
            ghost_4.move_4(screen)
        if ghost_1.out_1() and ghost_2.out_2() and ghost_3.out_3() and ghost_4.out_4(): #проверка что вышли все призраки
            out = True

        pygame.display.flip()
        pygame.time.wait(3)
    exit(0)

if __name__ == '__main__':
    main()
