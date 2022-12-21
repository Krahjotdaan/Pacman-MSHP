import pygame

class Health():
    def __init__(self):
        self.health = 3

    def minus_health(self):
        self.health -= 1

    def get_health(self):
        return self.health

    def draw(self, gridDisplay):
        sys = pygame.font.SysFont('ubuntu', 30)
        text = sys.render('Heatr: ' + str(self.get_health()), True, (255, 255, 255))
        gridDisplay.blit(text, (450, 140))