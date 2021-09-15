import pygame
import random
import time
from pygame.constants import MOUSEBUTTONDOWN

from pygame.key import name

'''
This Code was made largely by myself, Oliver Waldock. In saying that 
I did use pieces of others work. If I have used others code I have refrenced
it with the code taken.
'''

pygame.init()
font = pygame.font.init()
pygame.mixer.init()
pygame.display.set_caption("BOB the Blob")

WIDTH,HEIGHT = 1100,650
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 60


chill1 = pygame.mixer.Sound("Music/fato_shadow_-_in_my_dreams.wav")
chill2 = pygame.mixer.Sound("Music/fato_shadow_-_paradise.wav")
chill1.play(1)