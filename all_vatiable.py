from Packman_in_game.health import Health
from Packman_in_game.score import Score
from Packman_in_game.timer_super_seed import Timer
from Map.map import Map
from Packman.packman import Packman
from settings import Settings

map = Map()
timer = Timer()
score = Score()
health = Health()
settings = Settings()
packman = Packman([30, 120], [0, 0], "Packman/pacmanOpen.png", 3)