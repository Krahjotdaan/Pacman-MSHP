import pygame


from Scenes.game_over_scene import Game_Over_scene
from all_vatiable import settings
from Music.music import playMusic
from Scenes.game_scene import *
from Scenes.menu_scene import Menu_scene
from Scenes.records_scene import Records_scene
from Packman.packman import Packman

gridDisplay = pygame.display.set_mode((1200, 900))
pygame.display.get_surface().fill((200, 200, 200))  # background
packman = Packman([30, 120], [0, 0], "Packman/pacmanOpen.png", 3)
playMusic('Music/pacman_music.mp3')


def main():
    pygame.font.init()
    scenes = [Menu_scene(), Game_scene(), Game_Over_scene(), Records_scene()]

    game_over = False

    while not game_over:
        packman.damag()
        screen = pygame.display.set_mode([settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT])
        for event in pygame.event.get():
            if settings.scene_changed:
                settings.scene_changed = False

            game_over = check_for_quit(event)

            if not settings.scene_changed:
                scenes[settings.scene_index].event(event)
                scenes[settings.scene_index].logic()
                scenes[settings.scene_index].draw(screen)

        pygame.display.flip()
    exit(0)


def check_for_quit(event):
    return event.type == pygame.QUIT


if __name__ == '__main__':
    main()