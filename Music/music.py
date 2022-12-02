# music
import pygame

def playMusic(filepath):
    pygame.mixer.init()
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play(-1, 0.0)
    # music
