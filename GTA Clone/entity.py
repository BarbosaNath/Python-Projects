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
        self.frame_index  = 0
        self.time_elapsed = 0
        self.animation_speed = 300 # how many ms 'til change frame
        self.frame_changed = False

        self.state = {}

        self.spd      = 1        # speed
        self.dir      = (0,0)    # direction list
        self.position = position # position array
        self.accel    = self.dir * self.spd # acceleration array


    def move(self):
        self.accel = self.dir * self.spd
        self.position  = [x + y for x, y in zip(self.position, self.accel)]


    def collide(self):
        pass

    def animate(self):
        if self.time_elapsed >= self.animation_speed - 100 and not self.frame_changed:
            self.frame_changed = True
            self.frame_index += 1

        if self.time_elapsed <= 100:
            self.frame_changed = False

        self.frame_index = self.frame_index % len(self.animations[self.current_animation])
        self.image       = self.animations[self.current_animation][self.frame_index]

    def update(self):
        self.rect.center = self.position
        self.time_elapsed = pygame.time.get_ticks() % self.animation_speed
