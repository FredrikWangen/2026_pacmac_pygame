from pathlib import Path
import pygame as pg
from constants import *

class PacMan:
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
    

    def __init__(self, x, y):
        self.frames_idle = self.getImageSpriteList(0, 0, 4)
        # Om vi vil ha animasjon som går gjennom frames:
        self.current_frame = 0
    
        # Bildet vi skal vise til å starte med er idle:
        self.frames = self.frames_idle
        self.venstre = False

        # Typisk i PyGame: Bruker en "rect" for å plassere bildet på rett sted på skjermen (se draw metoden)
        self.rect = self.frames[0].get_rect()
        # Kjekt å vite hvilken "tile" vi står på:
        self.row = x // TILE_SIZE
        self.col = y // TILE_SIZE

    
    
    def draw(self, surface):

        # Sørg for at vi tegner midt i "Tile":
        mid = TILE_SIZE // 2
        self.rect.center = (self.row * TILE_SIZE + mid , self.col * TILE_SIZE + mid)

        # Få bildet fra en liste av bilder:
        current_frame_image = self.frames[self.current_frame]
        
        # Speiler bildet hvis det trengs:
        if self.venstre:
            current_frame_image = pg.transform.flip(current_frame_image, True, False)

        # Blit images på skjermen (der self.rect befinner seg):
        surface.blit(current_frame_image, self.rect)

