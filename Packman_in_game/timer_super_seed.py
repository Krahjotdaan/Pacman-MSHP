import pygame

class Timer():
    def __init__(self):
        self.timer = 1000
        self.timer_started = False

    def get_timer(self):
        return self.timer

    def tick(self):
        self.timer -= 1

    def logic(self):
        self.tick()
        if self.timer == 0:
            self.timer_started = False
            self.timer = 1000
            return False
        else:
            return True

    def draw(self, gridDisplay):
        sys = pygame.font.SysFont('ubuntu', 30)
        text = sys.render('Timer super seed: ' + str(self.get_timer()//250), True, (255, 255, 255))
        gridDisplay.blit(text, (450, 100))