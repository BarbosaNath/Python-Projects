from globals import pygame
from player  import Player

# GLOBALS
SCREEN_SIZE = (600, 400)
SCREEN      = pygame.display.set_mode(SCREEN_SIZE)
clock       = pygame.time.Clock()

background  = pygame.image.load("Assets/Debug/bg.jpg")

p = Player( ( 0,  0),  (16, 16), "Assets/Debug/sprite_sheet.png")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    p.key_input(pygame.key.get_pressed())
    p.update()
    SCREEN.blit(background, (0,0))
    SCREEN.blit(p.image, p.position)


    pygame.display.update()
    clock.tick(60)

pygame.quit()
