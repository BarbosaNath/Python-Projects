from person import Person
import key_input as K

class Player(Person):
    def __init__(self, position, size, image_path):
        super().__init__(position, size, image_path)
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


    def key_input(self, event, is_key_up = False):
        event = event
        left  = K.MENU_LEFT (event, is_key_up)
        right = K.MENU_RIGHT(event, is_key_up)
        up    = K.MENU_UP   (event, is_key_up)
        down  = K.MENU_DOWN (event, is_key_up)
        if left  == None: left  = False
        if right == None: right = False
        if up    == None: up    = False
        if down  == None: down  = False
        self.dir = (right - left, down - up)

    def update(self):
        super().update()

        if self.dir != (0,0):
            self.state["walking"] = True
        else: self.state["walking"] = False



        if self.state["walking"]:
            self.current_animation = "walking"
        else: self.current_animation = "idle"

        self.animate()

        if abs(self.dir[0]) == 1 and abs(self.dir[1]) == 1:
            new_dir  = list(self.dir)
            new_dir[0] *= 0.707
            new_dir[1] *= 0.707
            self.dir = tuple(new_dir)

        self.move()
