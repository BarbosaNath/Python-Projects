# <> Imports
from globals import pygame
from globals import SCREEN_SIZE
from globals import GAME_SCALE
from globals import HALF_SCREEN

from player  import Player

from World.world    import World
from World.tile_set import TileSet

from camera import Camera
from camera import Follow
from camera import Border
from camera import Auto
#</>

#<>################## GLOBALS ###################
SCREEN      = pygame.display.set_mode(SCREEN_SIZE)
clock       = pygame.time.Clock()
vec = pygame.math.Vector2
#</>


#<>################## Player Loading ###################
p = Player([ SCREEN_SIZE[0]/2,  SCREEN_SIZE[1]/2],  (16, 16), "Assets/Character-sheet.png", GAME_SCALE)
p.animation_speed = 120
p.spd = (GAME_SCALE[0]/3)*2

print(p.spd)

player_group = pygame.sprite.Group(p)
#</>



#<>################## World Loading ###################

ts = TileSet("Assets/tile_set.png", (16,16))
w  = World("World/map.csv", (16,16),
    [
        ts.tiles[0],
        ts.tiles[1],
        ts.tiles[2]
    ]
)
#</>



#<>################## Camera Loading ###################
cam = Camera(p)
p.camera = cam
w.camera = cam
follow = Follow(cam, p)
border = Border(cam, p, ( 0, 0, w.width, w.height))
auto   = Auto(cam, p)

cam.set_method(follow)
# </>


################### Game Loop ###################
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: cam.set_method(follow)
            if event.key == pygame.K_2: cam.set_method(border)
            if event.key == pygame.K_3: cam.set_method( auto )


    p.key_input(pygame.key.get_pressed())

    SCREEN.fill((0,0,0))

    cam.scroll()
    w.draw(SCREEN)


    player_group.update()
    p.draw(SCREEN)

    # <> Draw debug boxes
    pygame.draw.circle(
        SCREEN,
        (0,255,0),
        HALF_SCREEN,
        2,
    )
    pygame.draw.rect(
        SCREEN,
        (255,0,0),
        (
            p.rect.x - cam.offset.x,
            p.rect.y - cam.offset.y,
            p.rect.w,
            p.rect.h,
        ), 1
    )
    pygame.draw.rect(
        SCREEN,
        (255,0,255),
        p.collide_box, 1
    )
    # </>

    pygame.display.update()
    clock.tick(60)

pygame.quit()
