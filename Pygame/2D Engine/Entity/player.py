from Entity.person import Person
from globals import pygame
from globals import GAME_SCALE
from numpy import arctan2, pi
import key_input as K


class Player(Person):
    def __init__(self, position, size, image_path, scale=(1, 1)):
        super().__init__(position, size, image_path, scale)
        self.last_dir = (0, 0)
        self.animations = {
            "walking":  self.sprite_sheet.get_frames(),
            "idle": [self.sprite_sheet.get_frame()]
        }
        self.state = {
            "walking": False,
            "running": False,
            "dodging": False,
            "idle": False
        }
        self.current_animation = "idle"

    def key_input(self, event, is_key_up=False):

        left = (False if K.MENU_LEFT(event, is_key_up) is None
                else K.MENU_LEFT(event, is_key_up))

        right = (False if K.MENU_RIGHT(event, is_key_up) is None
                 else K.MENU_RIGHT(event, is_key_up))

        up = (False if K.MENU_UP(event, is_key_up) is None
              else K.MENU_UP(event, is_key_up))

        down = (False if K.MENU_DOWN(event, is_key_up) is None
                else K.MENU_DOWN(event, is_key_up))

        self.dir = (right - left, down - up)

    def fix_diagonal(self):
        if abs(self.dir[0]) == 1 and abs(self.dir[1]) == 1:
            new_dir = list(self.dir)
            new_dir[0] *= 0.707
            new_dir[1] *= 0.707
            self.dir = tuple(new_dir)

    def rotate_direction(self):
        angle = arctan2(self.last_dir[0], self.last_dir[1]) * 180 / pi
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def set_state(self,
                  state="idle",
                  on_off=True,
                  change_state=True,
                  change_anim=True
                  ):
        if change_state:
            self.state[state] = on_off
        if change_anim:
            self.current_animation = state if on_off else "idle"

    def set_collide_box(self, offset):
        self.collide_box[2] = ((self.sprite_sheet.sprite_size[0] - offset[0])
                               * self.scale[0])
        self.collide_box[3] = ((self.sprite_sheet.sprite_size[1] - offset[1])
                               * self.scale[1])
        self.collide_box.center = self.rect.center

    def reset(self):
        self.speed = (GAME_SCALE[0]/3)*2.5

    def update(self):
        super().update()

        if self.dir != (0, 0):
            self.set_state("walking")
            self.last_dir = self.dir
        else:
            self.set_state("walking", False)

        self.set_collide_box((5, 5))

        self.fix_diagonal()
        self.move()
        self.animate()
        self.rotate_direction()
