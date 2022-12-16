import pygame

from settings import Settings
from Map.map import Map
from Packman.packman import Packman
from Music.music import playMusic
from Ghost.ghost import Ghost
from Button.button import Button
my_map = Map()
# for row in my_map.collision_matrix:
#     for item in row:
#         print(item, end=' ')
#     print()
gridDisplay = pygame.display.set_mode((1200, 900))
pygame.display.get_surface().fill((200, 200, 200))  # background
packman = Packman([30, 120], [0, 0], "Packman/pacmanOpen.png")
playMusic('Music/pacman_music.mp3')

def main():
    # Основной цикл программы
    pygame.init()
    pygame.font.init()

    game_over = False
    score = 0

    list_ghosts = Ghost.creating_ghosts()
    Ghost.gosts_activate(list_ghosts)

    out = False  # показывает вышли призраки или нет
    # Основной цикл программы
class Settings2:
    scene_changed = True
    scene_index = 0

def set_scene(index):
    Settings2.scene_changed = True
    Settings2.scene_index = index

def set_game_scene():
    set_scene(1)
def set_menu_scene():
    set_scene(0)
def set_records_scene():
    set_scene(3)

background_color = pygame.Color('black')

def main():
    # Основной цикл программы
    # Инициализация сцены 0 (menu)
    global event
    pygame.font.init()
    scene_0_button_records_geometry = pygame.Rect(Settings.WINDOW_WIDTH / 2 - 100 / 2, Settings.WINDOW_HEIGHT / 2 - 10 - 50,
                                              100, 50)
    scene_0_button_back_geometry = pygame.Rect(Settings.WINDOW_WIDTH / 2 - 100 / 2,
                                                  Settings.WINDOW_HEIGHT / 2 + 300 - 50,
                                                  100, 50)
    scene_0_button_new_geometry = pygame.Rect(Settings.WINDOW_WIDTH / 2 - 100 / 2, Settings.WINDOW_HEIGHT / 2 - 80 - 50, 100, 50)
    scene_0_button_exit_geometry = pygame.Rect(Settings.WINDOW_WIDTH / 2 - 100 / 2, Settings.WINDOW_HEIGHT / 2 + 10, 100, 50)

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

    list_ghosts = Ghost.creating_ghosts()
    Ghost.gosts_activate(list_ghosts)
    score = 0

    out = False  # показывает вышли призраки или нет

    game_over = False

    while not game_over:
        # обработка событий
        screen = pygame.display.set_mode([Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT])

########СЕМЕКЧКИ#################################################################
        # my_map.draw_seeds()
        # for sd in my_map.seeds: # проверка того, что пакман съедает семку
        #     if packman.get_position()[0] + 15 == sd.pos[0] and packman.get_position()[1] + 15 == sd.pos[1]:
        #         if sd.is_super == True:
        #             my_map.seeds.remove(sd)
        #             score += 5 # начисление очков за большую семку
        #         else:
        #             my_map.seeds.remove(sd)
        #             score += 1 # начисление очков за обычную семку
#################################################################################

########ПРИЗРАКИ#################################################################

        if out:  # если все призраки вышли
            Ghost.ghosts_move_random(list_ghosts, screen)
            out = True
        else:
            Ghost.move_xy(list_ghosts, screen)
        if Ghost.ghosts_out(list_ghosts):  # проверка что вышли все призраки
            out = True
        pygame.time.wait(3)
#################################################################################

########ПАКМАН#################################################################
        # packman.draw(screen)
        # packman.move()
        # packman.logic(my_map.matrix)
        # pygame.display.flip()
#################################################################################
        for event in pygame.event.get():
            packman.event(event)

            if Settings2.scene_changed:
                Settings2.scene_changed = False

            if event.type == pygame.QUIT:
                game_over = True
            if Settings2.scene_index == 0:  # menu
                records_button.check_event(event)
                back_button.check_event(event)
                new_game_button.check_event(event)
                exit_button.check_event(event)
            elif Settings2.scene_index == 1:  # game
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    Settings2.scene_changed = True
                    Settings2.scene_index = 0
            elif Settings2.scene_index == 2:  # gameover
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    Settings2.scene_changed = True
                    Settings2.scene_index = 0

        if not Settings2.scene_changed:
            screen.fill(background_color)
            if Settings2.scene_index == 0:  # menu
                records_button.update(screen)
                new_game_button.update(screen)
                exit_button.update(screen)
            elif Settings2.scene_index == 1:  # game

                my_map.draw_seeds()
                for sd in my_map.seeds:  # проверка того, что пакман съедает семку
                    if packman.get_position()[0] + 15 == sd.pos[0] and packman.get_position()[1] + 15 == sd.pos[1]:
                        if sd.is_super == True:
                            my_map.seeds.remove(sd)
                            score += 5  # начисление очков за большую семку
                        else:
                            my_map.seeds.remove(sd)
                            score += 1  # начисление очков за обычную семку

                my_map.visualizeGrid()
                packman.draw(screen)
                packman.move()
                packman.logic(my_map.matrix)
                pygame.display.flip()

                if out:  # если все призраки вышли
                    Ghost.ghosts_move_random(list_ghosts, screen)
                    out = True
                else:
                    Ghost.move_xy(list_ghosts, screen)
                if Ghost.ghosts_out(list_ghosts):  # проверка что вышли все призраки
                    out = True


                pass #сюда пишется отрисовка всей игры
            elif Settings2.scene_index == 2:  # gameover
                pass

            pygame.display.flip()
    exit(0)




def check_for_exit(event):
    return event.type == pygame.QUIT

if __name__ == '__main__':
    main()

