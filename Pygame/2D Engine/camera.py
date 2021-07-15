from globals import pygame
from globals import SCREEN_SIZE
from globals import HALF_SCREEN
from globals import GAME_SCALE
from abc import ABC, abstractmethod
vec = pygame.math.Vector2


class Camera:
    def __init__(self, target):
        self.target = target
        self.offset = vec(0,0)
        self.offset_float = vec(0,0)
        self.CONST  = vec(-HALF_SCREEN[0],-HALF_SCREEN[1])

    def set_method(self, method):
        self.method = method

    def scroll(self):
        self.method.scroll()



################### Abstract Scroll Class ###################
class CamScroll(ABC):
    def __init__(self, camera, target):
        self.camera = camera
        self.target = target

    @abstractmethod
    def scroll(self):
        pass




class Follow(CamScroll):
    def __init__(self,camera,target):
        CamScroll.__init__(self,camera,target)

    def scroll(self):
        self.camera.offset_float.x += ((self.target.rect.center[0]) - self.camera.offset_float.x + self.camera.CONST.x)
        self.camera.offset_float.y += ((self.target.rect.center[1]) - self.camera.offset_float.y + self.camera.CONST.y)

        self.camera.offset.x = int(self.camera.offset_float.x)
        self.camera.offset.y = int(self.camera.offset_float.y)

class Border(CamScroll):
    def __init__(self,camera,target,border):
        CamScroll.__init__(self,camera,target)
        self.border = border
        # border = (Left, Top, Right, Bottom)

    def scroll(self):
        self.camera.offset_float.x += (self.target.rect.center[0] - self.camera.offset_float.x + self.camera.CONST.x)
        self.camera.offset_float.y += (self.target.rect.center[1] - self.camera.offset_float.y + self.camera.CONST.y)

        self.camera.offset.x = int(self.camera.offset_float.x)
        self.camera.offset.y = int(self.camera.offset_float.y)

        self.camera.offset.x = max(self.border[0]      , self.camera.offset.x           )
        self.camera.offset.x = min(self.camera.offset.x, self.border[2] - SCREEN_SIZE[0])

        self.camera.offset.y = max(self.border[1]      , self.camera.offset.y           )
        self.camera.offset.y = min(self.camera.offset.y, self.border[3] - SCREEN_SIZE[1])

class Auto(CamScroll):
    def __init__(self, camera, target, scroll_values = (1,0)):
        CamScroll.__init__(self, camera, target)
        self.scroll_values = scroll_values
        # scroll_values = (x amount to move per frame, y amount to moce per frame)

    def scroll(self):
        self.camera.offset_float.x += self.scroll_values[0]
        self.camera.offset_float.y += self.scroll_values[1]

        self.camera.offset.x = int(self.camera.offset_float.x)
        self.camera.offset.y = int(self.camera.offset_float.y)
