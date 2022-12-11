import pygame

from settings import Settings
from Map.map import Map
from Packman.packman import Packman
from Music.music import playMusic
from Ghost.ghost import Ghost

my_map = Map()

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

    list_ghosts = creating_ghosts()
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
            ghosts_move_random(list_ghosts, screen)
            out = True
        else:
            move_xy(list_ghosts, screen)
        if ghosts_out(list_ghosts):  # проверка что вышли все призраки
            out = True
        pygame.time.wait(3)
#################################################################################

########ПАКМАН#################################################################
        packman.draw(screen)
        packman.event(event)
        packman.move()
        pygame.display.flip()
#################################################################################
    exit(0)

def ghosts_move_random(list_ghosts, screen):
    for ghost in list_ghosts:
        ghost.move_random(screen)

def ghosts_out(list_ghosts):
    if list_ghosts[0].out_1() and list_ghosts[1].out_2() and list_ghosts[2].out_3() and list_ghosts[3].out_4():  # проверка что вышли все призраки
        return True
    else:
        return False

def move_xy(list_ghosts,screen):
    list_ghosts[0].move_1(screen)
    list_ghosts[1].move_2(screen)
    list_ghosts[2].move_3(screen)
    list_ghosts[3].move_4(screen)

def creating_ghosts():
    ghost_1 = Ghost([480, 390], "Ghost/ghost_2.png")  # создание призраков
    ghost_2 = Ghost([480, 510], "Ghost/ghost_2.png")
    ghost_3 = Ghost([660, 510], "Ghost/ghost_2.png")
    ghost_4 = Ghost([660, 390], "Ghost/ghost_2.png")
    list_ghosts = [ghost_1, ghost_2, ghost_3, ghost_4]
    for ghost in list_ghosts:
        ghost.activate()
    return list_ghosts



def check_for_exit(event):
    return event.type == pygame.QUIT

if __name__ == '__main__':
    main()

