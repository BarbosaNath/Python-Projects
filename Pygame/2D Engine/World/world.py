import os
import csv
import pygame
import json
from World.tile_set import TileSet
from globals import GAME_SCALE


class World:
    def __init__(self, file_path, tile_size=(16, 16),
                 tile_images=[], collidables=[]):
        if ".json" in file_path:
            with open(file_path, 'r') as file:
                self.json = json.load(file)
            self.file = self.json["file_path"]
            self.tile_size = tuple(self.json["tile_size"])
            self.collidables = self.json["collidables"]
            self.load_images_from_sprite_sheet()
        else:
            self.file = file_path
            self.tile_size = tile_size
            self.collidables = list(collidables)
            self.tile_images = tile_images

        self.tile_rects = []
        self.tiles = self.load_csv_tiles(
            self.file) if ".csv" in self.file else self.load_bitmap_tiles
        self.world_surface = pygame.Surface((self.width, self.height))
        self.world_surface.set_colorkey((0, 0, 0))
        self.load_map()
        self.camera_offset_x = 0
        self.camera_offset_y = 0

    def reset(self):
        self.tile_rects = []
        self.tiles = self.load_csv_tiles(
            self.file) if ".csv" in self.file else self.load_bitmap_tiles
        self.world_surface = pygame.Surface((self.width, self.height))
        self.world_surface.set_colorkey((0, 0, 0))
        self.load_map()

    def draw(self, canvas, pos=(0, 0)):
        x, y = pos
        canvas.blit(self.world_surface,
                    (x - self.camera_offset_x, y - self.camera_offset_y))

    def load_images_from_sprite_sheet(self):
        ts = TileSet(self.json["tile_set"]["file_path"], self.tile_size)
        self.tile_images = []
        for i in self.json["tile_images"]:
            self.tile_images.append(ts.tiles[i])

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
                    tiles.append(Tile(self.tile_images[int(tile)],
                                      (
                        int(x * self.tile_size[0] * GAME_SCALE[0]),
                        int(y * self.tile_size[1] * GAME_SCALE[1])
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
        if (GAME_SCALE[0].is_integer() and GAME_SCALE[1].is_integer()) or \
                (GAME_SCALE[0]-int(GAME_SCALE[0]) == .5 and
                 GAME_SCALE[1]-int(GAME_SCALE[1]) == .5):
            self.scaled = pygame.transform.scale(
                image, (int(self.rect.w*GAME_SCALE[0]),
                        int(self.rect.h*GAME_SCALE[1])))
        else:
            self.scaled = pygame.transform.scale(
                image, (int(self.rect.w*GAME_SCALE[0]+1),
                        int(self.rect.h*GAME_SCALE[1]+1)))
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def draw(self, surface):
        surface.blit(self.scaled, (self.rect.x, self.rect.y))
