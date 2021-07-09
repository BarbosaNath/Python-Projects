import pygame
import math

from world import Map
from player import Player
from player import Ray

DR    = 0.0174533
HEIGHT= 600
WIDTH = 800
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)

GAMEMODE = 0

DEBUG = False


try: pygame.init()
except: print("Erro ao iniciar o pygame")
window = pygame.display.set_mode((WIDTH,HEIGHT))
if not GAMEMODE == 0: window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game")



if DEBUG:
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Some Text', False, (200, 2, 100))


map = Map(
'''#########
#.......#
#...P...#
#.#.....#
#....#..#
#.......#
#.......#
#.......#
#########''',
64)


p = Player(map.getPX(),map.getPY(),5,0,0,2*math.pi,90,4)

rays = []
for i in range(int(p.fov*p.res)):
    rays.append( Ray(p, map, DR*(i/p.res-p.fov/2)))



run = True
while run:
    pygame.time.delay(10)

    # Player Moviment --------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT ] or keys[pygame.K_a]:
        p.a -= 0.05
        if (p.a < 0): p.a += 2 * math.pi
        p.dx = math.cos(p.a)*p.vel
        p.dy = math.sin(p.a)*p.vel

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        p.a += 0.05
        if (p.a > 2 * math.pi): p.a -= 2 * math.pi
        p.dx = math.cos(p.a)*p.vel
        p.dy = math.sin(p.a)*p.vel

    if keys[pygame.K_UP   ] or keys[pygame.K_w]: p.x += p.dx; p.y += p.dy
    if keys[pygame.K_DOWN ] or keys[pygame.K_s]: p.x -= p.dx; p.y -= p.dy
    #-------------------------------------------------



    window.fill((0,0,0))
    if not GAMEMODE == 1:
        pygame.draw.rect(window, (50,50,100),(0,0,400,400))
        map.draw(window)

    #print(rays[int(len(rays)/2)+2].o/DR*-1*10)


    for ray in rays:
        ray.update()
        if not GAMEMODE == 1: ray.draw(window)
        if not GAMEMODE == 0: ray.draw_wall(window, HEIGHT, 2)

    if not GAMEMODE == 1: p.draw(window)
    pygame.display.update()


pygame.quit()
