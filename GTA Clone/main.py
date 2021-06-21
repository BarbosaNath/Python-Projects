import sys
from globals import pygame
from entity import Entity

# GLOBALS
SCREEN_SIZE = (600, 400)
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

pygame.init()

e = Entity((100,100),(10,10))
entity_group = pygame.sprite.Group()
entity_group.add(e)

background = pygame.image.load("Assets/Test Material.jpg")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    entity_group.draw(SCREEN)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit
