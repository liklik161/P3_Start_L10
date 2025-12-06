import pygame
from models.gameobject import GameObject
from config import TILE_SIZE, COLORS


class Speler(GameObject):
    """Speler klasse, erft van GameObject"""
    
    # TODO OEFENING 1: Roep parent constructor aan met super()
    def __init__(self, x: int, y: int):
        super().__init__(x,y, COLORS["speler"])
    

    def teken(self, scherm: pygame.Surface):
        """ Teken de speler op het scherm. Overschrijft GameObject.teken() en tekent een cirkel"""
        x_px = self.x * TILE_SIZE + TILE_SIZE // 2
        y_px = self.y * TILE_SIZE + TILE_SIZE // 2
        straal = TILE_SIZE // 3
        
        pygame.draw.circle(scherm, self.kleur, (x_px, y_px), straal)
        pygame.draw.circle(scherm, COLORS["zwart"], (x_px, y_px), straal, 2)
