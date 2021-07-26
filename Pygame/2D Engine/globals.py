import pygame
pygame.init()

GAME_SCALE = [3.0, 3.0]
SCREEN_SIZE = (int(199*GAME_SCALE[0]), int(112*GAME_SCALE[1]))
HALF_SCREEN = (int(SCREEN_SIZE[0]/2), int(SCREEN_SIZE[1]/2))


def zoom(zoom_value, decimal=None, reseters=None):
    if isinstance(zoom, tuple):
        GAME_SCALE[0] += zoom_value[0]
        GAME_SCALE[1] += zoom_value[1]
    else:
        GAME_SCALE[0] += zoom_value
        GAME_SCALE[1] += zoom_value

    if decimal is not None:
        GAME_SCALE[0] = round(GAME_SCALE[0], decimal)
        GAME_SCALE[1] = round(GAME_SCALE[1], decimal)

    if reseters is not None:
        for r in reseters:
            r.reset()
