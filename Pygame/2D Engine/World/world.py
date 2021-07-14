from globals import pygame
from globals import GAME_SCALE
import csv, os
vec = pygame.math.Vector2
class World:
    def __init__(self, map_path, tile_size, scale = (1,1), tiles = None):
        self.image = pygame.image.load(map_path)
        self.rect  = self.image.get_rect()
        self.tiles = tiles
        self.scale = scale
        self.tile_size = tile_size
        self.camera = None
        self.tile_map = self.get_map(map_path)

    def draw(self,canvas, pos = (0,0)):
        canvas.blit(self.tile_map, pos)


    def read_csv(self, filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))
        return map

    def load_tiles(self, filename):
        tiles = []
        map = self.read_csv(filename)
        x, y = 0, 0
        for row in map:
            x = 0
            for id in row:
                for tile in self.tiles:
                    if id == tile.id:
                        tiles.append(tile.image, x*self.tile_size*GAME_SCALE[0],)



    #
    # def get_map(self, map_path):
    #     for x in range(self.rect[2]):
    #         for y in range(self.rect[3]):
    #             xpos = (x * self.tile_size[0] * self.scale[0]) - self.camera.offset.x
    #             ypos = (y * self.tile_size[1] * self.scale[1]) - self.camera.offset.y
    #             for tile in self.tiles:
    #                 if tile.color == self.image.get_at((x,y)):
    #                     canvas.blit(self.scaled_tile(tile.image,self.scale), (xpos, ypos))

    def scaled_tile(self, image, scale):
        scaled_image = pygame.transform.scale(
            image,
            (
                image.get_size()[0]*scale[0],
                image.get_size()[1]*scale[1],
            )
        )
        return scaled_image

class Tile:
    def __init__(self):
        pass
