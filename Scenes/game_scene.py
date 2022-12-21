from Scenes.menu_scene import set_scene
from Scenes.base_scene import Base_scene
from all_vatiable import packman
from all_vatiable import map
from all_vatiable import score
from Ghost.ghost import end_chasing, minus_life, check, creating_ghosts, ghosts_move_random, move_xy, ghosts_out, \
    gosts_activate

# Внимание! Есть огромное различие
# map = Map() - это один определённый объект
# Map() - при каждом использовонии новый объект



list_ghosts = creating_ghosts()
gosts_activate(list_ghosts)


class Game_scene(Base_scene):
    def __init__(self):
        super().__init__()
        self.out = False
        self.timer = 0

    def logic(self):
        for sd in map.seeds:  # проверка того, что пакман съедает семку
            if int((packman.get_position()[0] + 15) / 30) == int(sd.pos[0] / 30) and int(
                    (packman.get_position()[1] + 15) / 30) == int(sd.pos[1] / 30):
                if sd.is_super == True:
                    map.seeds.remove(sd)
                    score.add_score(5)  # начисление очков за большую семку
                else:
                    map.seeds.remove(sd)
                    score.add_score(1)  # начисление очков за обычную семку

        packman.logic(map.matrix)

    def draw(self, screen):
        map.visualizeGrid()
        map.draw_seeds()
        packman.draw(screen)
        if packman.hps():
            set_scene(0)

        self.timer = end_chasing(self.timer, list_ghosts)
        if minus_life(packman, list_ghosts):
            self.out = False

        if self.out:  # если все призраки вышли
            self.timer = check(list_ghosts, packman, map, self.timer)
            ghosts_move_random(list_ghosts, screen, map)
            self.out = True
        else:
            move_xy(list_ghosts, screen)

        if ghosts_out(list_ghosts):  # проверка что вышли все призраки
            self.out = True

    def event(self, event):
        packman.event(event)
        self.escape(event)
