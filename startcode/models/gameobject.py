import pygame
from config import COLORS

class GameObject:
    """ Basisklasse voor alle objecten, superklasse voor Speler en Doos. """
    
    def __init__(self, x: int, y: int, kleur: tuple[int, int, int] = COLORS["zwart"]):
        self.x = x
        self.y = y
        self.kleur = kleur
    

    def beweeg(self, dx: int, dy: int):
        """ Verplaats dit object. dx = verandering in x, dy = verandering in y"""
        # TODO OEFENING 3
        self.x += dx
        self.y += dy
    

    def teken(self, scherm: pygame.Surface):
        """Teken dit object. Moet overschreven worden door subklassen."""
        pass

