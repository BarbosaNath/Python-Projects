import pygame

pygame.init()
pygame.font.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

WHITE = (255,255,255)
BLACK = (  0,  0,  0)

GAME_SPEED = 10

clock = pygame.time.Clock()

COMIC_SANS = pygame.font.SysFont("Comic Sans MS", 30)
