# <> Imports
from globals import pygame
from globals import SCREEN_SIZE
from globals import GAME_SCALE
from globals import zoom

from Entity.player import Player

from World.world import World

from camera import Camera
from camera import Follow
from camera import Border
from camera import Auto
# </>


# <>################## GLOBALS ###################
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
vec = pygame.math.Vector2
# </>


# <>##################  World Loading ###################
w = World("Assets/Debug/debug_world.json")
# </>


# <>################## Player Loading ###################
p = Player([w.width//2,  w.height//2], (16, 16),
           "Assets/Character.png", GAME_SCALE)
p.animation_speed = 120
p.spd = (GAME_SCALE[0]/3)*2.5

player_group = pygame.sprite.Group(p)
# </>


# <>################## Camera Loading ###################
cam = Camera(p)
w.camera_offset_x = cam.offset.x
w.camera_offset_y = cam.offset.y
follow = Follow(cam)
border = Border(cam, (0, 0, w.width, w.height))
auto = Auto(cam)

cam.set_method(follow)
# </>

# <>################## Game Loop ###################
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                cam.set_method(follow)
            if event.key == pygame.K_2:
                cam.set_method(border)
            if event.key == pygame.K_3:
                cam.set_method(auto)

            if event.key == pygame.K_6:
                cam.move_to((0, 0), follow)
            if event.key == pygame.K_7:
                cam.move_to((800, 800), follow)

    p.key_input(pygame.key.get_pressed())

    if pygame.key.get_pressed()[pygame.K_4]:
        zoom(-.01, 2)
        w.reset()
        border = Border(cam, (0, 0, w.width, w.height))
        if cam.get_method() == "Border":
            cam.set_method(border)
        p.spd = (GAME_SCALE[0]/3)*2.5

    if pygame.key.get_pressed()[pygame.K_5]:
        zoom(.01, 2)
        w.reset()
        border = Border(cam, (0, 0, w.width, w.height))
        if cam.get_method() == "Border":
            cam.set_method(border)
        p.spd = (GAME_SCALE[0]/3)*2.5
    SCREEN.fill((0, 0, 0))

    cam.scroll()
    w.camera_offset_x = cam.offset.x
    w.camera_offset_y = cam.offset.y

    p.camera_offset_x = cam.offset.x
    p.camera_offset_y = cam.offset.y

    w.draw(SCREEN)

    player_group.update()

    p.collide(w.tile_rects)

    p.draw(SCREEN)

    # <> Draw debug boxes
    # pygame.draw.circle(
    #     SCREEN,
    #     (0,255,0),
    #     HALF_SCREEN,
    #     2,
    # )
    # pygame.draw.rect(
    #     SCREEN,
    #     (255,0,0),
    #     (
    #         p.rect.x - cam.offset.x,
    #         p.rect.y - cam.offset.y,
    #         p.rect.w,
    #         p.rect.h,
    #     ), 1
    # )
    # pygame.draw.rect(
    #     SCREEN,
    #     (255,0,255),
    #     (
    #         p.collide_box.x - cam.offset.x,
    #         p.collide_box.y - cam.offset.y,
    #         p.collide_box.w,
    #         p.collide_box.h,
    #     ), 1
    # )
    # </>

    pygame.display.update()
    clock.tick(60)
# </>


pygame.quit()
