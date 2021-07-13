from globals import pygame
class World:
    def __init__(self, map_path, tile_size, scale = (1,1), tiles = None):
        self.image = pygame.image.load(map_path)
        self.rect  = self.image.get_rect()
        self.tiles = tiles
        self.scale = scale
        self.tile_size = tile_size


    def draw(self, canvas):
        for x in range(self.rect[2]):
            for y in range(self.rect[3]):
                xpos = x * self.tile_size[0] * self.scale[0]
                ypos = y * self.tile_size[1] * self.scale[1]
                for tile in self.tiles:
                    if tile.color == self.image.get_at((x,y)):
                        canvas.blit(self.scaled_tile(tile.image,self.scale), (xpos, ypos))

    def scaled_tile(self, image, scale):
        scaled_image = pygame.transform.scale(
            image,
            (
                image.get_size()[0]*scale[0],
                image.get_size()[1]*scale[1],
            )
        )
        return scaled_image

#<>
# tiles = {
#     "Name"  : "Grass",
#     "Image" : "Assets/tile_set.png",
#     "Color" : (0,0,0)
# }
#</>
