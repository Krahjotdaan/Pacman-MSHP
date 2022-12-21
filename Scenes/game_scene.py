from Scenes.menu_scene import set_scene
from  Scenes.base_scene import Base_scene
from Map.map import Map
from Packman.packman import Packman
from Ghost.ghost import end_chasing, minus_life, check, creating_ghosts, ghosts_move_random, move_xy, ghosts_out, \
    gosts_activate
from score import Score

my_map = Map()

list_ghosts = creating_ghosts()
gosts_activate(list_ghosts)
packman = Packman([30, 120], [0, 0], "Packman/pacmanOpen.png", 3)


class Game_scene(Base_scene):
    def __init__(self):
        super().__init__()
        self.out = False

    def logic(self):
        for sd in my_map.seeds:  # проверка того, что пакман съедает семку
            if int((packman.get_position()[0] + 15) / 30) == int(sd.pos[0] / 30) and int(
                    (packman.get_position()[1] + 15) / 30) == int(sd.pos[1] / 30):
                if sd.is_super == True:
                    my_map.seeds.remove(sd)
                    # Settings.SCORE += 5  # начисление очков за большую семку
                else:
                    my_map.seeds.remove(sd)
                    # Settings.SCORE += 1  # начисление очков за обычную семку

        packman.logic(my_map.matrix)

    def draw(self, screen):
        Map().visualizeGrid()
        Map().draw_seeds()
        packman.draw(screen)
        #packman.damag()
        if packman.hps():
            set_scene(0)

        # self.timer = end_chasing(self.timer, list_ghosts)
        if minus_life(packman, list_ghosts):
            self.out = False

        if self.out:  # если все призраки вышли
            self.timer = check(list_ghosts, packman, Map(), self.timer)
            ghosts_move_random(list_ghosts, screen, Map())
            self.out = True
        else:
            move_xy(list_ghosts, screen)

        if ghosts_out(list_ghosts):  # проверка что вышли все призраки
            self.out = True

    def event(self, event):
        packman.event(event)
        self.escape(event)
