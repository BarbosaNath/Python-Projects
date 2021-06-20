import pygame
# import Entity from entity

# Initialize pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("Random Python Game")
icon = pygame.image.load('..\\res\\LogoWhite.png')
pygame.display.set_icon(icon)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((0, 0, 0))
    pygame.display.update()
