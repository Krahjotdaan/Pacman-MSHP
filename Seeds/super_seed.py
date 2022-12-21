import pygame

from Seeds.seed import Seed

class Super_seed(Seed):
    def __init__(self, color, pos):
        self.color = color
        self.pos = pos
        self.rad = 8.5
        self.is_super = True

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.rad)

    def __del__(self):
        pass