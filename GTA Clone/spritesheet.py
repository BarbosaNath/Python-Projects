from globals import pygame
class SpriteSheet:
    def __init__(self, image_path, sprite_size):
        self.image       = pygame.image.load(image_path)
        self.sprite_size = sprite_size
        self.columns     = (int)(self.image.get_rect()[2]/sprite_size[0])
        self.rows        = (int)(self.image.get_rect()[3]/sprite_size[1])

    def get_frames(self, start = (0,0), end = None):
        frames = []


        for row in range(self.rows - start[1]):
            for column in range(self.columns - start[0]):
                location = (
                    (start[0] * self.sprite_size[0]) + (self.sprite_size[0] * column),
                    (start[1] * self.sprite_size[1]) + (self.sprite_size[1] *    row)
                )
                frames.append(self.image.subsurface(pygame.Rect(location, self.sprite_size)))

        return frames

    def get_frames_from_strip(self, start = (0,0), direction = "horizontal"):
        frames = []

        if direction == "horizontal":
            for x in range(self.columns - start[0]):
                location = (
                    (start[0] * self.sprite_size[0]) + (self.sprite_size[0] * x),
                    (start[1] * self.sprite_size[1])
                )
                frames.append(self.image.subsurface(pygame.Rect(location, self.sprite_size)))

        elif direction == "vertical":
            for y in range(self.rows - start[1]):
                location = (
                    (start[0] * self.sprite_size[0]),
                    (start[1] * self.sprite_size[1]) + (self.sprite_size[1] * y)
                )
                frames.append(self.image.subsurface(pygame.Rect(location, self.sprite_size)))
        else:
            print("direction should be \"horizontal\" or \"vertical\", you wrote {}".format(direction))

        for i in range(len(frames), 0, -1):
            # TODO: check for empty frames 
            pass

        return frames
