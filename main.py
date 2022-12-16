import pygame

from settings import Settings
from Map.map import Map
from Packman.packman import Packman
from Music.music import playMusic
from Ghost.ghost import Ghost

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

    while not game_over:
        # обработка событий
        for event in pygame.event.get():
            game_over = check_for_exit(event)
        screen = pygame.display.set_mode([Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT])
        my_map.visualizeGrid()

########СЕМЕКЧКИ#################################################################
        my_map.draw_seeds()
        for sd in my_map.seeds: # проверка того, что пакман съедает семку
            if packman.get_position()[0] + 15 == sd.pos[0] and packman.get_position()[1] + 15 == sd.pos[1]:
                if sd.is_super == True:
                    my_map.seeds.remove(sd)
                    score += 5 # начисление очков за большую семку
                else:
                    my_map.seeds.remove(sd)
                    score += 1 # начисление очков за обычную семку
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
        packman.draw(screen)
        packman.event(event)
        packman.move()
        packman.logic(my_map.matrix)
        pygame.display.flip()
#################################################################################
    exit(0)




def check_for_exit(event):
    return event.type == pygame.QUIT

if __name__ == '__main__':
    main()

