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


def MENU_UP(key, is_key_up=False):
    if key[K_w] or key[K_UP]:
        return True
    else:
        return False


def MENU_DOWN(key, is_key_up=False):
    if key[K_s] or key[K_DOWN]:
        return True
    else:
        return False


def MENU_LEFT(key, is_key_up=False):
    if key[K_a] or key[K_LEFT]:
        return True
    else:
        return False


def MENU_RIGHT(key, is_key_up=False):
    if key[K_d] or key[K_RIGHT]:
        return True
    else:
        return False
