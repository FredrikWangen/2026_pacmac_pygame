from pathlib import Path
import pygame as pg
from constants import *
from board import Board
from superCharacter import SuperCharacter

class PacMan(SuperCharacter):
    def __init__(self, row: int, col: int):
        super().__init__(row, col, (0,0,4))
    def update(self, board: Board):
        self.rect = self.frames[self.current_frame].get_rect()
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.nextAxis = "x"
            self.leftRight = -1
        if keys[pg.K_RIGHT]:
            self.nextAxis = "x"
            self.leftRight = 1
        if keys[pg.K_DOWN]:
            self.nextAxis = "y"
            self.upDown = 1
        if keys[pg.K_UP]:
            self.nextAxis = "y"
            self.upDown = -1

        super().move(board, PACMANSPEED)

        


