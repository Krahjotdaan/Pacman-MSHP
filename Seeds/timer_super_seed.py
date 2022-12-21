import pygame
from score import Score

class Timer():
    def __init__(self):
        self.time = 15

    def draw(self, gridDisplay):
        sys = pygame.font.SysFont('ubuntu', 30)
        text = sys.render('Timer super seed: ' + str(Score().get_score()), True, (255, 255, 255))
        gridDisplay.blit(text, (450, 100))