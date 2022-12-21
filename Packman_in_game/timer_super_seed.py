import pygame

class Timer():
    def __init__(self):
        self.timer = 15

    def get_timer(self):
        return self.timer

    def draw(self, gridDisplay):
        sys = pygame.font.SysFont('ubuntu', 30)
        text = sys.render('Timer super seed: ' + str(self.get_timer()), True, (255, 255, 255))
        gridDisplay.blit(text, (450, 100))