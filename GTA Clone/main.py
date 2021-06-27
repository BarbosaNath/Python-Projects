from globals import pygame
from player  import Player
# from spritesheet import SpriteSheet

# GLOBALS
SCREEN_SIZE = (600, 400)
SCREEN      = pygame.display.set_mode(SCREEN_SIZE)
clock       = pygame.time.Clock()

background  = pygame.image.load("Assets/Debug/bg.jpg")

p = Player( ( 0,  0),  (16, 16), "Assets/Debug/sprite_sheet.png")

# # DEBUGING VARIABLES
#
# test = SpriteSheet("Assets/Debug/sprite_sheet.png", (16, 16))
# frames = test.get_frames()
#
# frame = 0
# # END

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        p.key_input(pygame.key.get_pressed())
        # if event.type == pygame.KEYUP:
        #     p.key_input(event.key, True)
        # TODO: corrigir o bug de andar pra sempre
    #     # DEBUGING KEYMAPS
    #         frame += 1
    #     # END
    #
    # # DEBUGING ACTIONS
    # frame = frame % len(frames)
    #
    SCREEN.blit(background, (0,0))
    SCREEN.blit(p.image, p.position)
    # SCREEN.blit(frames[frame], (200,200))
    # # END

    p.update()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
