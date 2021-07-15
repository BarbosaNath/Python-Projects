from globals import pygame
from spritesheet import SpriteSheet

class Entity(pygame.sprite.Sprite):
    def __init__(self, position, size, image_path, scale = (1, 1)):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect  = self.image.get_rect()
        self.rect.center = position
        self.collide_box = self.rect.copy()

        self.sprite_sheet = SpriteSheet(image_path,size)
        self.frame_index  = 0
        self.time_elapsed = 0
        self.animation_speed = 300 # how many ms 'til change frame
        self.frame_changed = False
        self.scale = scale

        self.state = {}

        self.spd      = 1        # speed
        self.dir      = (0,0)    # direction list
        self.position = position # position array
        self.accel    = self.dir * self.spd # acceleration array

        self.camera = None

    def move(self):
        accel_x = self.dir[0] * self.spd
        accel_y = self.dir[1] * self.spd
        self.accel = (accel_x, accel_y)
        self.position  = [x + y for x, y in zip(self.position, self.accel)]

    def scale_sprite(self, scale):
            self.image = pygame.transform.scale(
                self.image,
                (
                    self.image.get_size()[0]*scale[0],
                    self.image.get_size()[1]*scale[1]
                )
            )

    def collide(self):
        # TODO: fazer sistema de colisão
        pass

    def animate(self):
        if self.time_elapsed  >= self.animation_speed - 60 and not self.frame_changed:
            self.frame_changed = True
            self.frame_index  += 1

        if self.time_elapsed  <= 60:
            self.frame_changed = False

        self.frame_index = self.frame_index % len(self.animations[self.current_animation])
        self.image       = self.animations[self.current_animation][self.frame_index]
        self.scale_sprite(self.scale)

    def update(self):
        self.rect.center  = self.position
        self.time_elapsed = pygame.time.get_ticks() % self.animation_speed

    def draw(self, canvas):
        canvas.blit(self.image, (self.position[0] - self.camera.offset.x - self.rect.w/2, self.position[1] - self.camera.offset.y - self.rect.h/2))
