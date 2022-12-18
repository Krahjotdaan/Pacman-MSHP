import pygame
from settings import Settings
from Map.map import Map
from Packman.packman import Packman
from Ghost.ghost import Ghost, end_chasing, minus_life, check, creating_ghosts, ghosts_move_random, move_xy, ghosts_out, \
    gosts_activate
from Button.button import Button
my_map = Map()

list_ghosts = creating_ghosts()
gosts_activate(list_ghosts)
packman = Packman([30, 120], [0, 0], "Packman/pacmanOpen.png")

def set_scene(index):
    Settings.scene_changed = True
    Settings.scene_index = index

def set_menu_scene():
    set_scene(0)
def set_game_scene():
    set_scene(1)
def set_records_scene():
    set_scene(2)

class Base_scene:
    def __init__(self):
        self.react_to_escape = True
    def activate(self):
        pass
    def event(self, event):
        self.escape(event)

    def escape(self, event):
        if self.react_to_escape:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                Settings.scene_changed = True
                Settings.scene_index = 0
    def logic(self):
        pass
    def draw(self, screen):
        pass

    def do_everything(self, event, screen):
        self.event(event)
        self.draw(screen)

class Menu_scene(Base_scene):
    BUTTON_STYLE = {
        "hover_color": pygame.Color('blue'),
        "clicked_color": pygame.Color('green'),
        "clicked_font_color": pygame.Color('black'),
        "hover_font_color": pygame.Color('orange'),
    }
    def __init__(self):
        super().__init__()
        scene_0_button_records_geometry = pygame.Rect(Settings.WINDOW_WIDTH / 2 - 100 / 2,
                                                      Settings.WINDOW_HEIGHT / 2 - 10 - 50,
                                                      100, 50)
        scene_0_button_back_geometry = pygame.Rect(Settings.WINDOW_WIDTH / 2 - 100 / 2,
                                                   Settings.WINDOW_HEIGHT / 2 + 300 - 50,
                                                   100, 50)
        scene_0_button_new_geometry = pygame.Rect(Settings.WINDOW_WIDTH / 2 - 100 / 2,
                                                  Settings.WINDOW_HEIGHT / 2 - 80 - 50, 100, 50)
        scene_0_button_exit_geometry = pygame.Rect(Settings.WINDOW_WIDTH / 2 - 100 / 2, Settings.WINDOW_HEIGHT / 2 + 10,
                                                   100, 50)

        BUTTON_STYLE = {
            "hover_color": pygame.Color('blue'),
            "clicked_color": pygame.Color('green'),
            "clicked_font_color": pygame.Color('black'),
            "hover_font_color": pygame.Color('orange'),
        }

        records_button = Button(scene_0_button_records_geometry, pygame.Color('gray'), set_records_scene,
                                text='Records', **BUTTON_STYLE)
        back_button = Button(scene_0_button_back_geometry, pygame.Color('gray'), set_menu_scene,
                             text='Back', **BUTTON_STYLE)
        new_game_button = Button(scene_0_button_new_geometry, pygame.Color('gray'), set_game_scene,
                                 text='New game', **BUTTON_STYLE)
        exit_button = Button(scene_0_button_exit_geometry, pygame.Color('gray'), exit,
                             text='Exit', **BUTTON_STYLE)

        self.buttons = [records_button, new_game_button, exit_button, back_button]
    def draw(self, screen):
        for i in range(len(self.buttons) - 1):  # чтобы делать для всех, кроме кнопки back
            self.buttons[i].update(screen)
    def event(self, event):
        for button in self.buttons:
            button.check_event(event)

class Game_scene(Base_scene):
    def __init__(self):
        super().__init__()
        self.out = False
        self.timer = 0

    def logic(self):
        for sd in my_map.seeds:  # проверка того, что пакман съедает семку
            if packman.get_position()[0] + 15 == sd.pos[0] and packman.get_position()[1] + 15 == sd.pos[1]:
                if sd.is_super == True:
                    my_map.seeds.remove(sd)
                    Settings.SCORE += 5  # начисление очков за большую семку
                else:
                    my_map.seeds.remove(sd)
                    Settings.SCORE += 1  # начисление очков за обычную семку

        packman.logic(my_map.matrix)


    def draw(self, screen):
        my_map.visualizeGrid()
        my_map.draw_seeds()
        packman.draw(screen)

        self.timer = end_chasing(self.timer, list_ghosts)
        if minus_life(packman, list_ghosts):
            self.out = False

        if self.out:  # если все призраки вышли
            self.timer = check(list_ghosts, packman, my_map, self.timer)
            ghosts_move_random(list_ghosts, screen, my_map)
            self.out = True
        else:
            move_xy(list_ghosts, screen)

        if ghosts_out(list_ghosts):  # проверка что вышли все призраки
            self.out = True

    def event(self, event):
        packman.event(event)
        self.escape(event)

class Game_Over_scene(Base_scene):
    def __init__(self):
        super().__init__()
