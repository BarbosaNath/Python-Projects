from globals import pygame
from entity  import Entity
from spritesheet import SpriteSheet

# GLOBALS
SCREEN_SIZE = (600, 400)
SCREEN      = pygame.display.set_mode(SCREEN_SIZE)
clock       = pygame.time.Clock()

background  = pygame.image.load("Assets/Test Material.jpg")

test = SpriteSheet("Assets/TestSpriteSheet.png", (16, 16))
frames = test.get_frames()


frame = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            frame += 1

    frame = frame % len(frames)

    SCREEN.blit(background, (0,0))
    SCREEN.blit(frames[frame], (200,200))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
