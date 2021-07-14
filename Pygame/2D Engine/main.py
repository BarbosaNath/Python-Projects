# <> Imports
from globals import pygame
from globals import SCREEN_SIZE
#from globals import HALF_SCREEN
from globals import GAME_SCALE
from player  import Player
from World.tile  import Tile
from World.world import World
from World.tile_set import TileSet

from camera import Camera
from camera import Follow
from camera import Border
from camera import Auto
#</>

################### GLOBALS ###################
SCREEN      = pygame.display.set_mode(SCREEN_SIZE)
clock       = pygame.time.Clock()
vec = pygame.math.Vector2

################### Player Loading ###################
p = Player([ SCREEN_SIZE[0]/2,  SCREEN_SIZE[1]/2],  (16, 16), "Assets/Character-sheet.png", GAME_SCALE)
p.animation_speed = 120

player_group = pygame.sprite.Group(p)


################### World Loading ###################
ts = TileSet((16,16), "Assets/tile_set.png")
w = World("Assets/map.png",(16,16), GAME_SCALE,
    [
        Tile("Grass" , ts.tiles[0], ( 73, 150, 150)),
        Tile("Orange", ts.tiles[1], (132,  90,  73)),
        Tile("Purple", ts.tiles[2], (123,  65,  98))
    ]
)

################### Camera Loading ###################
cam = Camera(p)
p.camera = cam
w.camera = cam
follow = Follow(cam, p)
border = Border(cam, p, (
        w.rect.x * w.tile_size[0] * w.scale[0],
        w.rect.y * w.tile_size[1] * w.scale[1],
        w.rect.w * w.tile_size[0] * w.scale[0],
        w.rect.h * w.tile_size[1] * w.scale[1]))
auto   = Auto(cam, p)

cam.set_method(follow)

################### Game Loop ###################
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: cam.set_method(follow); print("Follow")
            if event.key == pygame.K_2: cam.set_method(border); print("Border")
            if event.key == pygame.K_3: cam.set_method( auto ); print(" Auto ")


    p.key_input(pygame.key.get_pressed())

    SCREEN.fill((0,0,0))

    cam.scroll()
    w.draw(SCREEN)

    player_group.update()
    player_group.draw(SCREEN)


    print("Camera offset {}".format(cam.offset))
    print("Player offset {}".format(p.camera.offset))
    print("World  offset {}".format(w.camera.offset))
    print()

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
