from models.doos import Doos
from models.speler import Speler
from config import GRID_BREEDTE, GRID_HOOGTE, MUUR, VLOER, DOEL, LEVELS


class SokobanGame:
    """Main game-klasse die alles beheert."""
    
    def __init__(self):
        """Initialiseer een nieuw spel."""
        self.huidig_level = 1
        self.totaal_levels = len(LEVELS)
        self.dozen: list[Doos] = []
        self.speler = Speler(1, 1)
        self.zetten = 0
        self.gewonnen = False
        self.bericht = "Welkom bij Sokoban! Duw alle dozen naar de doelen."
        
        self.laad_level(1)
    

    def laad_level(self, level_nummer: int):
        """Laad een specifiek level uit de config."""
        if level_nummer not in LEVELS:
            return
        
        self.huidig_level = level_nummer
        self.zetten = 0
        self.gewonnen = False
        
        level_data = LEVELS[level_nummer]
        
        self.grid = level_data["grid"]
        
        # Reset speler naar startpositie
        self.speler.x = 1
        self.speler.y = 1
        
        self.dozen = []
        for doos_x, doos_y in level_data["dozen"]:
            self.dozen.append(Doos(doos_x, doos_y))
        
        self.bericht = f'Level {level_nummer}'


    def volgend_level(self):
        """Ga naar het volgende level."""
        if self.huidig_level < self.totaal_levels:
            self.laad_level(self.huidig_level + 1)
        else:
            self.bericht = "Je hebt alle levels uitgespeeld!"
    

    def beweeg_speler(self, dx: int, dy: int) -> str:
        """Probeer de speler te bewegen."""
        if self.gewonnen:
            return "Je hebt al gewonnen!"
        
        nieuwe_x = self.speler.x + dx
        nieuwe_y = self.speler.y + dy
        
        # Check of nieuwe positie binnen grid is
        if not self._is_binnen_grid(nieuwe_x, nieuwe_y):
            return "Je kunt niet buiten het veld!"
        
        # Check of nieuwe positie een muur is
        if self.grid[nieuwe_y][nieuwe_x] == MUUR:
            return "Je kunt niet door muren heen lopen!"
        
        # Check of er een doos op nieuwe positie staat
        doos = self._vind_doos_op(nieuwe_x, nieuwe_y)
        if doos:
            # Probeer doos te duwen
            if self._probeer_doos_duwen(doos, dx, dy):
                # Doos geduwd, speler beweegt mee
                self.speler.beweeg(dx, dy)
                self.zetten += 1
                
                # Check win conditie
                if self._check_gewonnen():
                    self.gewonnen = True
                    if self.huidig_level < self.totaal_levels:
                        return f"GEWONNEN in {self.zetten} zetten! Druk N voor volgend level."
                    else:
                        return f"ALLE LEVELS VOLTOOID in {self.zetten} zetten! GEFELICITEERD!"
                
                return f"Doos geduwd!"
            else:
                return "Doos kan niet die kant op bewegen!"
        
        # Geen doos, gewoon bewegen
        self.speler.beweeg(dx, dy)
        self.zetten += 1
        return f"Beweegt... (Zet {self.zetten})"
    

    def _is_binnen_grid(self, x: int, y: int) -> bool:
        """Check of positie binnen grid is."""
        return 0 <= x < GRID_BREEDTE and 0 <= y < GRID_HOOGTE
    

    def _vind_doos_op(self, x: int, y: int) -> Doos | None:
        """Vind een doos op een bepaalde positie, en geef dat doos object terug."""
        # TODO OEFENING 4
        for doos in self.dozen:
            if doos.x == x and doos.y == y:
                return doos
    

    def _probeer_doos_duwen(self, doos: Doos, dx: int, dy: int) -> bool:
        """ Probeer een doos te duwen; True als het gelukt is."""
        # TODO OEFENING 5
        nieuwe_doos_x = dx + doos.x
        nieuwe_doos_y = dy + doos.y

        if not self._is_binnen_grid(nieuwe_doos_x, nieuwe_doos_y):
            return False

        if self.grid[nieuwe_doos_y][nieuwe_doos_x] == MUUR:
            return False

        if self._vind_doos_op(nieuwe_doos_x, nieuwe_doos_y):
            return False

        doos.beweeg(dx,dy)
        return True

    

    def _check_gewonnen(self) -> bool:
        """Check of alle dozen op doel vakjes staan; True als waar, False als niet."""
        # TODO OEFENING 6
        for doos in self.dozen:
            if self.grid[doos.y][doos.x] != DOEL:
                return False

        return True

