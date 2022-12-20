import pygame


from Scenes.base_scene import Base_scene
from settings import Settings
from Button.button import Button


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

def set_scene(index):
    Settings.scene_changed = True
    Settings.scene_index = index

def set_menu_scene():
    set_scene(0)

def set_game_scene():
    set_scene(1)

def set_records_scene():
    set_scene(3)