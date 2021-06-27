from globals import pygame
from player  import Player

# GLOBALS
SCREEN_SIZE = (600, 400)
SCREEN      = pygame.display.set_mode(SCREEN_SIZE)
clock       = pygame.time.Clock()

background  = pygame.image.load("Assets/Debug/bg.jpg")

p = Player(( 200,  200),  (16, 16), "Assets/Debug/sprite_sheet.png")

player_group = pygame.sprite.Group(p)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    p.key_input(pygame.key.get_pressed())
    SCREEN.blit(background, (0,0))
    player_group.update()
    player_group.draw(SCREEN)


    pygame.display.update()
    clock.tick(60)

pygame.quit()
