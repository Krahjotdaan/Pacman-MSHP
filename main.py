import pygame
from settings import Settings
from Map.map import Map
from Packman.packman import Packman
from Music.music import playMusic
from Ghost.ghost import Ghost
from Scenes.scenes import *

my_map = Map()

gridDisplay = pygame.display.set_mode((1200, 900))
pygame.display.get_surface().fill((200, 200, 200))  # background
packman = Packman([30, 120], [0, 0], "Packman/pacmanOpen.png")
playMusic('Music/pacman_music.mp3')
list_ghosts = Ghost.creating_ghosts()
Ghost.gosts_activate(list_ghosts)


def main():
    global event
    pygame.font.init()
    scenes = [Menu_scene(), Game_scene(), Game_Over_scene(), Records_scene()]

    game_over = False

    while not game_over:
        screen = pygame.display.set_mode([Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT])

        for event in pygame.event.get():
            if Settings.scene_changed:
                Settings.scene_changed = False

            game_over = check_for_quit(event)

            if not Settings.scene_changed:
                scenes[Settings.scene_index].event(event)
                scenes[Settings.scene_index].logic()
                scenes[Settings.scene_index].draw(screen)

        pygame.display.flip()
    exit(0)


def check_for_quit(event):
    return event.type == pygame.QUIT


if __name__ == '__main__':
    main()