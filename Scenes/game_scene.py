import time

from Scenes.menu_scene import set_scene
from Scenes.base_scene import Base_scene
from all_vatiable import packman
from all_vatiable import map
from all_vatiable import score
from all_vatiable import settings
from Ghost.ghost import end_chasing, minus_life, check, creating_ghosts, ghosts_move_random, move_xy, ghosts_out, \
    gosts_activate
import pygame
from time import *

screen = pygame.display.set_mode((1200, 900))
# Внимание! Есть огромное различие
# map = Map() - это один определённый объект
# Map() - при каждом использовонии новый объект


list_ghosts = creating_ghosts()
gosts_activate(list_ghosts)


class Game_scene(Base_scene):
    def __init__(self):
        super().__init__()
        self.out = False
        self.timer = 0
        self.paused = False
        self.pause_f1 = pygame.font.SysFont('ubuntu', 150)  # шрифт
        self.pause_text = self.pause_f1.render("Paused", False,
                                               (255, 255, 255))  # заголовок

    def logic(self):
        for sd in map.seeds:  # проверка того, что пакман съедает семку
            if int((packman.get_position()[0] + 15) / 30) == int(sd.pos[0] / 30) and int(
                    (packman.get_position()[1] + 15) / 30) == int(sd.pos[1] / 30):
                if sd.is_super == True:
                    map.seeds.remove(sd)
                    score.add_score(10)  # начисление очков за большую семку
                else:
                    map.seeds.remove(sd)
                    score.add_score(10)  # начисление очков за обычную семку

        packman.logic(map.matrix)

    def draw(self, screen):
        map.visualizeGrid()
        map.draw_seeds()
        packman.draw(screen)
        # <--------отрисовка изображений жизни-->
        packman.draw_pac_img(screen)
        # <------------------------->

        if packman.hps():
            set_scene(0)

        self.timer = end_chasing(self.timer, list_ghosts)
        if minus_life(packman, list_ghosts):
            self.out = False

        if self.out:  # если все призраки вышли
            self.timer = check(list_ghosts, packman, map, self.timer)
            ghosts_move_random(list_ghosts, screen, map)
            self.out = True
        else:
            move_xy(list_ghosts, screen)

        if ghosts_out(list_ghosts):  # проверка что вышли все призраки
            self.out = True
        # if self.paused:

    def pause(self):
        loop = 1
        self.paused = True
        while loop:
            for event in pygame.event.get():
                screen.blit(self.pause_text, (settings.WINDOW_WIDTH // 2 - self.pause_text.get_rect().w // 2,
                                              settings.WINDOW_HEIGHT // 2 - self.pause_text.get_rect().h))
                if event.type == pygame.QUIT:
                    loop = 0
                    self.paused = False
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        loop = 0
                        self.paused = False
            pygame.display.update()
            # screen.fill((0, 0, 0))
            pygame.time.wait(60)

    def check_for_pause(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                self.pause()

    def event(self, event):
        packman.event(event)
        self.escape(event)
        self.check_for_pause(event)
