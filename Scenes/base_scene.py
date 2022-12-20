import pygame


from settings import Settings


class Base_scene:
    def __init__(self):
        self.react_to_escape = True
    def activate(self):
        pass
    def event(self, event):
        self.escape(event)

    def escape(self, event):
        if self.react_to_escape:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                Settings.scene_changed = True
                Settings.scene_index = 0
    def logic(self):
        pass
    def draw(self, screen):
        pass

    def do_everything(self, event, screen):
        self.event(event)
        self.draw(screen)