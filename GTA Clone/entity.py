from globals import pygame
from spritesheet import SpriteSheet

class Entity(pygame.sprite.Sprite):
    def __init__(self, position, size, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = position
        # TODO: add a SpriteSheet to an entity
        self.sprite_sheet = SpriteSheet(image_path,size)

        self.spd      = 1        # speed
        self.dir      = (0,0)    # direction list
        self.position = position # position array
        self.accel    = self.dir * self.spd # acceleration array


    def move(self):
        self.accel = self.dir * self.spd
        self.position  = [x + y for x, y in zip(self.position, self.accel)]

    def collide(self):
        pass
    def update(self):
        pass
    def render(self):
        pass

class Person(Entity):
    def __init__(self, position, size, image_path):
       super().__init__(position, size, image_path)
       self.isAlive = True
       self.health_points = 100
