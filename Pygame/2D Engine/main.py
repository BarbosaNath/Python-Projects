# <> Imports
from globals import pygame
from globals import SCREEN_SIZE
from globals import GAME_SCALE
import globals

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


# <>################# Music ##################
pygame.mixer.music.load("Assets/Music/BaDopp.wav")
pygame.mixer.music.play(-1)
# </>


# <>##################  World Loading ###################
w = World("Assets/Debug/debug_world.json")
# </>


# <>################## Player Loading ###################
p = Player(
    position=[w.width//2,  w.height//2],
    size=(16, 16),
    image_path="Assets/Character.png",
    scale=GAME_SCALE
)
p.animation_speed = 120
p.speed = (GAME_SCALE[0]/3)*2.5

player_group = pygame.sprite.Group(p)
# </>


# <>################## Camera Loading ###################
cam = Camera(p)
w.camera_offset_x = cam.offset.x
w.camera_offset_y = cam.offset.y
follow = Follow(cam)
border = Border(cam, (0, 0, w.width, w.height))
auto = Auto(cam)

cam.set_method(border)
# </>


# <>################## Game Loop ###################
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    p.key_input(pygame.key.get_pressed())

    # SCREEN.fill((0, 0, 0))

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
    pygame.draw.circle(
        SCREEN, (0, 255, 0),
        globals.HALF_SCREEN, 2)
    pygame.draw.rect(
        SCREEN, (255, 0, 0), (
            p.rect.x - cam.offset.x,
            p.rect.y - cam.offset.y,
            p.rect.w, p.rect.h), 1)
    pygame.draw.rect(
        SCREEN, (255, 0, 255), (
            p.collide_box.x - cam.offset.x,
            p.collide_box.y - cam.offset.y,
            p.collide_box.w, p.collide_box.h), 1)
    # </>

    pygame.display.update()
    clock.tick(60)
# </>


pygame.quit()
