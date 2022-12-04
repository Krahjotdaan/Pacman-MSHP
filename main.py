import pygame
from map import Map
from packman import Packman
my_map = Map()
packman = Packman()
def main():
    my_map.visualizeGrid()
    screen = pygame.display.set_mode([1200, 700])
    # Основной цикл программы
    game_over = False
    while not game_over:
        for sd in my_map.seeds:
            if packman.get_position()[0] + 15 == sd.pos[0] and packman.get_position()[1] + 15 == sd.pos[1]:
                my_map.seeds.remove(sd)
                sd.color = (0, 0, 0)
                sd.draw(screen)
    exit(0)

if __name__ == '__main__':
    main()
