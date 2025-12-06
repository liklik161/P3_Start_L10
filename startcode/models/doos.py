import pygame
from models.gameobject import GameObject
from config import TILE_SIZE, COLORS


class Doos(GameObject):
    """Doos klasse die geduwd kan worden door de speler, erft van GameObject"""

    def __init__(self, x: int, y: int):
        super().__init__(x, y, COLORS["doos"])
    

    def teken(self, scherm: pygame.Surface):
        """Teken de doos als vierkant. Overschrijft GameObject.teken()"""
        x_px = self.x * TILE_SIZE
        y_px = self.y * TILE_SIZE
        marge = 8
        
        rect = pygame.Rect(x_px + marge, y_px + marge,
                          TILE_SIZE - marge * 2, TILE_SIZE - marge * 2)
        pygame.draw.rect(scherm, self.kleur, rect)
        pygame.draw.rect(scherm, COLORS["zwart"], rect, 2)
