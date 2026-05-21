from pathlib import Path
import pygame as pg
from constants import *
from board import Board
from superCharacter import SuperCharacter
from pacman import PacMan

class SuperGhost(SuperCharacter):
    def __init__(self, row: int, col: int, spriteloc: tuple[int, int, int] = (0, 64, 4)):
        super().__init__(row, col, spriteloc)

    def pathfind(self, current_row: int, current_col: int, target_row: int, target_col: int):
        x = target_col - current_col
        y = target_row - current_row

        if abs(x) > abs(y):
            return "right" if x > 0 else "left"
        return "down" if y > 0 else "up"

    def update(self, board: Board, pacman: PacMan):
        x = pacman.x - self.x
        y = pacman.y - self.y

        if abs(x) > abs(y):
            self.nextAxis = "x"
            self.leftRight = 1 if x > 0 else -1
        else:
            self.nextAxis = "y"
            self.upDown = 1 if y > 0 else -1

        super().move(board, GHOSTSPEED)
