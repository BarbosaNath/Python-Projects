from globals import pygame
from spritesheet import SpriteSheet
class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, size, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        # TODO: add a SpriteSheet to an entity 
        self.sprite_sheet = SpriteSheet(image_path,size)

        self.spd   = 1# speed
        self.dir   = 1# direction array
        self.pos   = pos  # position array
        self.accel = self.dir * self.spd # acceleration array


    def move(self, dir):
        self.dir   = dir
        self.accel = self.dir * self.spd
        self.pos  += self.accel

    def collide(self):
        pass
    def update(self):
        pass
    def render(self):
        pass

class Person(Entity):
   def __init__(self):
       super().__init__()
       self.isAlive
