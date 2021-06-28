from person import Person
from globals import pygame
import key_input as K

class Player(Person):
    def __init__(self, position, size, image_path, scale = (1, 1)):
        super().__init__(position, size, image_path, scale)
        self.animations = {
            "walking" : self.sprite_sheet.get_frames(),
            "idle"    : [self.sprite_sheet.get_frame()]
        }
        self.state = {
            "walking" : False,
            "running" : False,
            "dodging" : False,
            "idle"    : False
        }
        self.current_animation = "idle"
        self.spd = 2


    def key_input(self, event, is_key_up = False):

        left  = K.MENU_LEFT (event, is_key_up)
        right = K.MENU_RIGHT(event, is_key_up)
        up    = K.MENU_UP   (event, is_key_up)
        down  = K.MENU_DOWN (event, is_key_up)
        if left  == None: left  = False
        if right == None: right = False
        if up    == None: up    = False
        if down  == None: down  = False
        self.dir = (right - left, down - up)

    def fix_diagonal(self):
        if abs(self.dir[0]) == 1 and abs(self.dir[1]) == 1:
            new_dir  = list(self.dir)
            new_dir[0] *= 0.707
            new_dir[1] *= 0.707
            self.dir = tuple(new_dir)

    def rotate_direction(self):
        # TODO: fix clunky rotation
        self.image = pygame.transform.rotate(self.image, 90 * self.dir[0]) if self.dir[1] != -0.707 else self.image
        self.image = pygame.transform.flip(self.image,False,True) if self.dir[1] == -1 else self.image
        if self.dir[1] == -0.707 and self.dir[0] == 0.707:
            self.image = pygame.transform.rotate(self.image,-45 + 180)
        if self.dir[1] == -0.707 and self.dir[0] == -0.707:
            self.image = pygame.transform.rotate(self.image, 45 + 180)

    def update(self):
        super().update()

        if self.dir != (0,0):
            self.state["walking"] = True
        else: self.state["walking"] = False

        if self.state["walking"]:
            self.current_animation = "walking"
        else: self.current_animation = "idle"

        self.fix_diagonal()
        self.move()
        self.animate()
        self.rotate_direction()
