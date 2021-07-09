import pygame

class Spritesheet:
    def __init__(self, filename):
        # Load the sprite sheet
        self.sheet = pygame.image.load(filename).convert()


    # Load a specific image from a rectangle
    def image_at(self, rectangle, colorkey = None)
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.sizea)convert()
        image.blit(self.sheet, (0,0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at()
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image


    # Load a lot of images and return them as a list
    def images_at(self, rects, images_count, colorkey = None):
        return [self.image_at(rect, colorkey) for rect in rects]


    # Load a strip of images and returns them as a list
    def load_strip(self, rect, images_count, colorkey = None):
        tups = [(rect[0] + rect[2]*x, rect[1], rect[2], rect[4])
                    for x in range(image_count)]
        return self.images_at(tups, colorkey)
