import pygame
from settings import Settings
from Map.map import Map
from Packman.packman import Packman
from Ghost.ghost import Ghost
from Button.button import Button

list_ghosts = Ghost.creating_ghosts()
Ghost.gosts_activate(list_ghosts)
my_map = Map()
packman = Packman([30, 120], [0, 0], "Packman/pacmanOpen.png")

def set_scene(index):
    Settings.scene_changed = True
    Settings.scene_index = index

def set_menu_scene():
    set_scene(0)
def set_game_scene():
    set_scene(1)
def set_records_scene():
    set_scene(3)
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

class Records_scene(Base_scene): # сцена рекордов
    BUTTON_STYLE = {
        "hover_color": pygame.Color('blue'),
        "clicked_color": pygame.Color('green'),
        "clicked_font_color": pygame.Color('black'),
        "hover_font_color": pygame.Color('orange'),
    }
    def __init__(self, dct={"pythonist":1000000, "player":0}): # получает словарь
        super().__init__()
        self.arr = list(dct)
        self.dict = dct
        scene_2_button_back_geometry = pygame.Rect(Settings.WINDOW_WIDTH / 2 - 100 / 2,
                                                   Settings.WINDOW_HEIGHT / 2 + 300 - 50,
                                                   100, 50)
        BUTTON_STYLE = {
            "hover_color": pygame.Color('blue'),
            "clicked_color": pygame.Color('green'),
            "clicked_font_color": pygame.Color('black'),
            "hover_font_color": pygame.Color('orange'),
        }

        back_button = Button(scene_2_button_back_geometry, pygame.Color('gray'), set_menu_scene,
                             text='Back', **BUTTON_STYLE)
        self.buttons = [back_button]
    def draw(self, screen): # рисуем таблицу
        pygame.draw.rect(screen, ("black"), [Settings.WINDOW_WIDTH // 2 - 350, Settings.WINDOW_HEIGHT // 6, 700, 500])
        for i in range(len(self.buttons)):
            self.buttons[i].update(screen)
        f1 = pygame.font.SysFont('ubuntu', 24) # шрифт
        text = f1.render("Leaderboard", False,
                          (255, 255, 255)) # заголовок
        screen.blit(text, (Settings.WINDOW_WIDTH // 2 - 75, Settings.WINDOW_HEIGHT - 800))
        for i in range(len(self.arr)):
            s = f1.render("{}:{} {}".format(self.arr[i],(40-len(self.arr[i])) * ' .', self.dict[self.arr[i]]), False,
                          (255, 255, 255))
            screen.blit(s,(Settings.WINDOW_WIDTH // 2 - 300, Settings.WINDOW_HEIGHT - 750 + (i+1) * 40))
    def event(self, event):
        for button in self.buttons:
            button.check_event(event)


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
        new_game_button = Button(scene_0_button_new_geometry, pygame.Color('gray'), set_game_scene,
                                 text='New game', **BUTTON_STYLE)
        exit_button = Button(scene_0_button_exit_geometry, pygame.Color('gray'), exit,
                             text='Exit', **BUTTON_STYLE)

        self.buttons = [records_button, new_game_button, exit_button]
    def draw(self, screen):
        for i in range(len(self.buttons)):
            self.buttons[i].update(screen)

    def event(self, event):
        for button in self.buttons:
            button.check_event(event)

class Game_scene(Base_scene):
    def __init__(self):
        super().__init__()
        self.out = False

    def logic(self):
        for sd in my_map.seeds:  # проверка того, что пакман съедает семку
            if int((packman.get_position()[0] + 15) / 30) == int(sd.pos[0]/30) and int((packman.get_position()[1] + 15) / 30) == int(sd.pos[1]/30):
                if sd.is_super == True:
                    my_map.seeds.remove(sd)
                    Settings.SCORE += 5  # начисление очков за большую семку
                else:
                    my_map.seeds.remove(sd)
                    Settings.SCORE += 1  # начисление очков за обычную семку

        packman.logic(my_map.matrix)
        # pygame.display.flip()

        if self.out:  # если все призраки вышли
            Ghost.ghosts_move_random(list_ghosts)
            self.out = True
        else:
            Ghost.move_xy(list_ghosts)
        if Ghost.ghosts_out(list_ghosts):  # проверка что вышли все призраки
            self.out = True
    def draw(self, screen):
        my_map.visualizeGrid()
        my_map.draw_seeds()
        packman.draw(screen)

    def event(self, event):
        packman.event(event)
        self.escape(event)

class Game_Over_scene(Base_scene):
    def __init__(self):
        super().__init__()
