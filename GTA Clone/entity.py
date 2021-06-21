from globals import pygame
class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.spd   =1# speed
        self.dir   =1# direction array
        self.pos   = pos  # position array
        self.accel = self.dir * self.spd # acceleration array


    def move(self):
        self.pos += self.accel

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
