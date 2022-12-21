import pygame

class Score():
    def __init__(self):
        self.score = 0

    def get_score(self):
        return self.score

    def add_score(self, points):
        self.score += points

    def draw(self, gridDisplay):
        sys = pygame.font.SysFont('ubuntu', 30)
        text = sys.render('Your score: ' + str(self.get_score()), True, (255, 255, 255))
        gridDisplay.blit(text, (450, 60))

