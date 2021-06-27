from pygame.locals import (
    K_w,
    K_a,
    K_s,
    K_d,

    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)


def MENU_UP(event, is_key_up = False):
    if event == K_w or event == K_UP:
        if not is_key_up: return True
        else: return False
    else: pass

def MENU_DOWN(event, is_key_up = False):
    if event == K_s or event == K_DOWN:
        if not is_key_up: return True
        else: return False
    else: pass

def MENU_LEFT(event, is_key_up = False):
    if event == K_a or event == K_LEFT:
        if not is_key_up: return True
        else: return False
    else: pass

def MENU_RIGHT(event, is_key_up = False):
    if event == K_d or event == K_RIGHT:
        if not is_key_up: return True
        else: return False
    else: pass
