import pygame


from Scenes.base_scene import Base_scene
from settings import Settings
from Button.button import Button
from Scenes.menu_scene import set_menu_scene


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
