import os
import csv
import pygame
from globals import GAME_SCALE


class World:
    def __init__(self, file_path, tile_size, tiles_id, collidables):
        self.file = file_path
        self.tile_size = tile_size
        self.collidables = list(collidables)
        self.tile_rects = []
        self.tiles_id = tiles_id
        self.tiles = self.load_csv_tiles(
            file_path) if ".csv" in file_path else self.load_bitmap_tiles
        self.world_surface = pygame.Surface((self.width, self.height))
        self.world_surface.set_colorkey((0, 0, 0))
        self.load_map()
        self.camera = None
        self.camera_offset_x = 0
        self.camera_offset_y = 0

    def draw(self, canvas, pos=(0, 0)):
        x, y = pos
        canvas.blit(self.world_surface,
                    (x - self.camera_offset_x, y - self.camera_offset_y))

    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.world_surface)

    def read_csv(self, file_path):
        map = []
        with open(os.path.join(file_path)) as data:
            m = csv.reader(data, delimiter=",")
            for row in m:
                map.append(list(row))
            data.close()
        return map

    def load_csv_tiles(self, file_path):
        tiles = []
        map = self.read_csv(file_path)
        x, y = 0, 0
        for row in map:
            x = 0
            for tile in row:
                if tile != '-1':
                    tiles.append(Tile(self.tiles_id[int(tile)],
                                      (
                        x * self.tile_size[0] * GAME_SCALE[0],
                        y * self.tile_size[1] * GAME_SCALE[1]
                    )))
                    if int(tile) in self.collidables:
                        self.tile_rects.append(
                            pygame.Rect(
                                x * self.tile_size[0] * GAME_SCALE[0],
                                y * self.tile_size[1] * GAME_SCALE[1],
                                self.tile_size[0] * GAME_SCALE[0],
                                self.tile_size[1] * GAME_SCALE[1]
                            ))
                x += 1
            y += 1

        self.width = x * self.tile_size[0] * GAME_SCALE[0]
        self.height = y * self.tile_size[1] * GAME_SCALE[1]

        return tiles

    def load_bitmap_tiles(self, file_path):
        pass


class Tile:
    def __init__(self, image, pos):
        self.id = id
        self.image = image
        self.rect = image.get_rect()
        self.scaled = pygame.transform.scale(
            image, (int(self.rect.w*GAME_SCALE[0]),
                    int(self.rect.h*GAME_SCALE[1])))
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def draw(self, surface):
        surface.blit(self.scaled, (self.rect.x, self.rect.y))
