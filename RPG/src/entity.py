from spritesheet import SpriteSheet


# Creating an Entity class
class Entity:
    def __init__(self, filename):
        self.sprite = SpriteSheet(filename)

