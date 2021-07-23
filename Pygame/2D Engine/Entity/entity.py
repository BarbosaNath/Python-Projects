from globals import pygame
from spritesheet import SpriteSheet
from globals import GAME_SCALE


class Entity(pygame.sprite.Sprite):
    def __init__(self, position, size, image_path, scale=(1, 1)):
        super().__init__()
        self.image = pygame.image.load(image_path).convert()
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.collide_box = self.rect.copy()

        self.sprite_sheet = SpriteSheet(image_path, size)
        self.frame_index = 0
        self.time_elapsed = 0
        self.animation_speed = 300  # how many ms 'til change frame
        self.frame_changed = False
        self.scale = scale

        self.state = {}

        self.speed = 1        # speed
        self.dir = (0, 0)    # direction list
        self.position = list(position)  # position array
        self.accel = self.dir * self.speed  # acceleration array

        self.is_colliding = False

        self.last_position = self.position

    def move(self):
        accel_x = self.dir[0] * self.speed
        accel_y = self.dir[1] * self.speed
        self.accel = (accel_x, accel_y)
        self.position = [x + y for x, y in zip(self.position, self.accel)]

    def scale_sprite(self, scale):
        self.image = pygame.transform.scale(
            self.image,
            (
                int(self.image.get_size()[0]*scale[0]),
                int(self.image.get_size()[1]*scale[1])
            )
        )

    def collide(self, tiles):
        for tile in tiles:
            if self.collide_box.colliderect(tile):
                delta_right = self.collide_box.right - tile.right
                delta_left = self.collide_box.left - tile.left
                delta_top = self.collide_box.top - tile.top
                delta_bottom = self.collide_box.bottom - tile.bottom

                if delta_right < 0:
                    self.position[0] -= GAME_SCALE[0] - GAME_SCALE[0]/6
                if delta_left > 0:
                    self.position[0] += GAME_SCALE[0] - GAME_SCALE[0]/6

                if delta_top < 0:
                    self.position[1] -= GAME_SCALE[1] - GAME_SCALE[1]/6
                if delta_bottom > 0:
                    self.position[1] += GAME_SCALE[1] - GAME_SCALE[1]/6

    def animate(self):
        if (self.time_elapsed >= self.animation_speed - 60 and
                not self.frame_changed):
            self.frame_changed = True
            self.frame_index += 1

        if self.time_elapsed <= 60:
            self.frame_changed = False

        self.frame_index = (self.frame_index %
                            len(self.animations[self.current_animation]))
        self.image = self.animations[self.current_animation][self.frame_index]
        self.scale_sprite(self.scale)

    def update(self):
        self.rect.center = self.position
        self.time_elapsed = pygame.time.get_ticks() % self.animation_speed
        self.accel = (0, 0)

    def draw(self, canvas):
        canvas.blit(self.image, (self.position[0] - self.camera_offset_x -
                    self.rect.w/2, self.position[1] -
                    self.camera_offset_y - self.rect.h/2))
