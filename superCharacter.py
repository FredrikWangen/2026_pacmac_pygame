from pathlib import Path
import pygame as pg
from constants import *
from board import Board

class SuperCharacter:
    IMAGE_FILE = Path(__file__).parent / "sprites" / "pacman2.png"

    def getImageSpriteList(self, x_start, y_start, num_frames) -> list[pg.Surface]:
        full_image = pg.image.load(self.IMAGE_FILE)
        frame_width = 16
        
        # Dele opp bildet i frames, som lagres i en liste:
        frames = []
        for i in range(num_frames):
            # Bildene er kvadratiske - bruker frame widht både som høye og bredde:
            frame = full_image.subsurface(pg.Rect(x_start + i * frame_width, y_start, frame_width, frame_width))
            frames.append(frame)
        return frames

    def __init__(self, row: int, col: int, spriteloc: tuple[int,int,int]):
        self.row = row
        self.col = col

        mid = TILE_SIZE // 2
        self.x = col * TILE_SIZE + mid
        self.y = row * TILE_SIZE + mid

        self.moveAxis = "x"
        self.nextAxis = "x"
        self.leftRight = -1
        self.upDown = -1

        self.frames_idle = self.getImageSpriteList(*spriteloc)
        # Bildet vi skal vise til å starte med er idle:
        self.frames = self.frames_idle
        # Om vi vil ha animasjon som går gjennom frames:
        self.current_frame = 0

        # Om vi vil speile bildet:
        self.venstre = False

    def move(self, board: Board, speed: int):
        mid = TILE_SIZE // 2
        current_row = (self.y - mid) // TILE_SIZE
        current_col = (self.x - mid) // TILE_SIZE

        at_center_x = abs((self.x - mid) % TILE_SIZE) <= speed
        at_center_y = abs((self.y - mid) % TILE_SIZE) <= speed

        if self.nextAxis == "y" and self.moveAxis == "x":
            target_row = current_row + self.upDown
            if at_center_x and board.is_road(current_col, target_row):
                self.x = round((self.x - mid) / TILE_SIZE) * TILE_SIZE + mid
                self.moveAxis = "y"
                self.y -= speed * self.upDown
        elif self.nextAxis == "x" and self.moveAxis == "y":
            target_col = current_col + self.leftRight
            if at_center_y and board.is_road(target_col, current_row):
                self.y = round((self.y - mid) / TILE_SIZE) * TILE_SIZE + mid
                self.moveAxis = "x"
                self.x -= speed * self.leftRight

        if self.moveAxis == "x":
            target_col = round((self.x - mid) / TILE_SIZE) + self.leftRight
            if board.is_road(target_col, current_row):
                self.x += speed * self.leftRight
            else:
                center_x = round((self.x - mid) / TILE_SIZE) * TILE_SIZE + mid
                distance_x = center_x - self.x
                if abs(distance_x) <= speed:
                    self.x = center_x
                else:
                    self.x += speed * (1 if distance_x > 0 else -1)
        elif self.moveAxis == "y":
            target_row = round((self.y - mid) / TILE_SIZE) + self.upDown
            if board.is_road(current_col, target_row):
                self.y += speed * self.upDown
            else:
                center_y = round((self.y - mid) / TILE_SIZE) * TILE_SIZE + mid
                distance_y = center_y - self.y
                if abs(distance_y) <= speed:
                    self.y = center_y
                else:
                    self.y += speed * (1 if distance_y > 0 else -1)

    def draw(self, surface: pg.Surface):

            # Få bildet fra en liste av bilder (om du vil bruke animasjon/sprites):
            current_frame_image = self.frames[self.current_frame]
            
            # Speiler bildet hvis det trengs:
            if self.venstre:
                current_frame_image = pg.transform.flip(current_frame_image, True, False)

            rect = current_frame_image.get_rect()
            rect.center = (self.x, self.y)
            # Blit images på skjermen (der self.rect befinner seg):
            surface.blit(current_frame_image, rect)