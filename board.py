import pygame as pg
from constants import *

class Board:
    def __init__(self):
        self.grid = [
            "#################",
            "#...##.....##...#",
            "#.#.###.###.#.#.#",
            "#.#...........#.#",
            "#.#.###.#.###.#.#",
            "#.....#...#.....#",
            "###.#.#####.#.###",
            "#...............#",
            "###.#.#####.#.###",
            "#.....#...#.....#",
            "#.#.###.#.###.#.#",
            "#.#...........#.#",
            "#.#.###.###.#.#.#",
            "#...##.....##...#",
            "#################",
        ]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

    def window_size(self):
        return self.cols*TILE_SIZE, self.rows*TILE_SIZE

    def draw(self, surface):
        """Tegn brettet på den gitte pygame-flaten."""
        for y, row in enumerate(self.grid):
            for x, tile in enumerate(row):
                rect = pg.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                if tile == '#':
                    pg.draw.rect(surface, DARK_BLUE, rect, border_radius=5)

    def tile_from_pos(self,x,y):
        mid = TILE_SIZE // 2
        row = (y - mid) // TILE_SIZE
        col = (x - mid) // TILE_SIZE
        return (row, col)
    
    def neighbors(self, row,col):
        neighborList = []
        if row != 0:
            if self.is_road(col, row - 1):
                neighborList.append((col,row - 1))
        if row != self.rows-1:
            if self.is_road(col, row + 1):
                neighborList.append((col,row + 1))
        if col != 0:
            if self.is_road(col - 1, row):
                neighborList.append((col - 1,row))
        if col != self.cols - 1:
            if self.is_road(col + 1, row):
                neighborList.append((col + 1,row))
        return neighborList

    def is_road(self, x: int, y: int) -> bool:
        """Returnerer True hvis posisjonen er fri for vegg."""
        if x < 0 or x >= self.cols or y < 0 or y >= self.rows:
            return False
        return self.grid[y][x] != '#'
