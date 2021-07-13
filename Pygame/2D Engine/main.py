from globals import pygame
from player  import Player
from World.tile  import Tile
from World.world import World
from World.tile_set import TileSet

# GLOBALS
SCREEN_SIZE = (600, 400)
HALF_SCREEN = (int(SCREEN_SIZE[0]/2), int(SCREEN_SIZE[1]/2))
SCREEN      = pygame.display.set_mode(SCREEN_SIZE)
GAME_SCALE  = (3,3)
clock       = pygame.time.Clock()

p = Player(( SCREEN_SIZE[0]/2,  SCREEN_SIZE[1]/2),  (16, 16), "Assets/Character-sheet.png", GAME_SCALE)
p.animation_speed = 120

player_group = pygame.sprite.Group(p)



ts = TileSet((16,16), "Assets/tile_set.png")
w = World("Assets/map.png",(16,16), GAME_SCALE,
    [
        Tile("Grass" , ts.tiles[0], ( 73, 150, 150)),
        Tile("Orange", ts.tiles[1], (132,  90,  73)),
        Tile("Purple", ts.tiles[2], (123,  65,  98))
    ]
)





running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    p.key_input(pygame.key.get_pressed())

    SCREEN.fill((0,0,0))

    w.draw(SCREEN)

    player_group.update()
    player_group.draw(SCREEN)

    # <> Draw some shit
    # pygame.draw.circle(
    #     SCREEN,
    #     (0,255,0),
    #     HALF_SCREEN,
    #     2,
    # )
    #
    # pygame.draw.rect(
    #     SCREEN,
    #     (255,0,0),
    #     p.rect, 1
    # )
    # pygame.draw.rect(
    #     SCREEN,
    #     (255,0,255),
    #     p.collide_box, 1
    # )
    # </>

    pygame.display.update()
    clock.tick(60)

pygame.quit()
