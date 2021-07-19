from globals import pygame


class TileSet:
    def __init__(self, image_path, tile_size):
        self.image = pygame.image.load(image_path).convert()
        self.tiles = []
        self.tile_size = tile_size
        self.columns = int(self.image.get_rect()[2]/self.tile_size[0])
        self.rows = int(self.image.get_rect()[3]/self.tile_size[1])

        for row in range(self.rows):
            for column in range(self.columns):
                location = (
                    (self.tile_size[0] * column),
                    (self.tile_size[1] * row)
                )
                self.tiles.append(self.image.subsurface(
                    pygame.Rect(location, self.tile_size)))
