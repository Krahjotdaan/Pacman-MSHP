import pygame

# shfsjkh
from settings import Settings
from Map.map import Map
from Map.map import visualizeGrid
from Packman.packman import Packman
from Music.music import playMusic

my_map = Map()

gridDisplay = pygame.display.set_mode((1200, 900))
pygame.display.get_surface().fill((200, 200, 200))  # background
packman = Packman([30, 120], [0, 0], "Packman/pacmanOpen.png")
playMusic('Music/pacman_music.mp3')


def main():
    pygame.font.init()
    # Основной цикл программы
    game_over = False
    while not game_over:
        # обработка событий
        for event in pygame.event.get():
            game_over = check_for_exit(event)
        screen = pygame.display.set_mode([Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT])
        visualizeGrid()
        # for sd in my_map.seeds:
        #     if packman.get_position()[0] + 15 == sd.pos[0] and packman.get_position()[1] + 15 == sd.pos[1]:
        #         my_map.seeds.remove(sd)
        #         sd.color = (0, 0, 0)
        #         sd.draw(screen)
        packman.draw(screen)
        packman.event(event)
        packman.move()
        pygame.display.flip()

    exit(0)


def check_for_exit(event):
    return event.type == pygame.QUIT


if __name__ == '__main__':
    main()
