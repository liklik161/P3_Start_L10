import pygame
import sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE, COLORS, GRID_BREEDTE, GRID_HOOGTE
from config import MUUR, VLOER, DOEL
from game import SokobanGame


class SokobanApp:
    """Applicatie klasse die Pygame runt."""
    
    def __init__(self):
        """Initialiseer de applicatie."""
        pygame.init()
        self.scherm = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Sokoban - Overerving Demo")
        self.klok = pygame.time.Clock()
        self.game = SokobanGame()
        self.actief = True
    

    def verwerk_input(self):
        """Verwerk keyboard input."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.actief = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.game.bericht = self.game.beweeg_speler(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.game.bericht = self.game.beweeg_speler(1, 0)
                elif event.key == pygame.K_UP:
                    self.game.bericht = self.game.beweeg_speler(0, -1)
                elif event.key == pygame.K_DOWN:
                    self.game.bericht = self.game.beweeg_speler(0, 1)
                elif event.key == pygame.K_r:
                    self.game.laad_level(self.game.huidig_level)
                elif event.key == pygame.K_n:
                    if self.game.gewonnen:
                        self.game.volgend_level()


    
    def teken(self):
        """Teken alles op het scherm."""
        self.scherm.fill(COLORS["zwart"])
        self._teken_grid()
        self._teken_dozen()
        self.game.speler.teken(self.scherm)
        self._teken_hud()
        pygame.display.flip()
    

    def _teken_grid(self):
        """Teken het grid met vloer types."""
        for y in range(GRID_HOOGTE):
            for x in range(GRID_BREEDTE):
                x_px = x * TILE_SIZE
                y_px = y * TILE_SIZE
                vloer_type = self.game.grid[y][x]
                
                if vloer_type == MUUR:
                    kleur = COLORS["muur"]
                elif vloer_type == DOEL:
                    kleur = COLORS["doel"]
                else:
                    kleur = COLORS["vloer"]
                
                rect = pygame.Rect(x_px, y_px, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(self.scherm, kleur, rect)
                pygame.draw.rect(self.scherm, COLORS["zwart"], rect, 1)
    

    def _teken_dozen(self):
        """ Teken alle dozen. """
        for doos in self.game.dozen:
            doos.teken(self.scherm)
    

    def _teken_hud(self):
        """Teken HUD met info."""
        font = pygame.font.Font(None, 28)
        klein_font = pygame.font.Font(None, 20)
        
        # Bericht bovenaan
        bericht_surf = font.render(self.game.bericht, True, COLORS["zwart"])
        bericht_rect = bericht_surf.get_rect(center=(SCREEN_WIDTH // 2, 15))
        achtergrond = pygame.Rect(bericht_rect.x - 10, bericht_rect.y - 5,
                                  bericht_rect.width + 20, bericht_rect.height + 10)
        pygame.draw.rect(self.scherm, (255, 255, 255), achtergrond)
        pygame.draw.rect(self.scherm, COLORS["zwart"], achtergrond, 2)
        self.scherm.blit(bericht_surf, bericht_rect)
        
        # Stats onderaan
        stats_y = SCREEN_HEIGHT - 30
        level_tekst = klein_font.render(f"Level: {self.game.huidig_level}/{self.game.totaal_levels}",
                                        True, (255, 255, 255))
        self.scherm.blit(level_tekst, (10, stats_y))
        
        
        if self.game.gewonnen and self.game.huidig_level < self.game.totaal_levels:
            instructie = klein_font.render("N: volgend level | R: reset", True, (200, 200, 200))
        else:
            instructie = klein_font.render("Pijltjes: bewegen | R: reset", True, (200, 200, 200))
        self.scherm.blit(instructie, (SCREEN_WIDTH - 380, stats_y))
        
        # Win bericht
        if self.game.gewonnen:
            win_font = pygame.font.Font(None, 48)
            if self.game.huidig_level < self.game.totaal_levels:
                win_tekst = win_font.render("LEVEL VOLTOOID!", True, (255, 215, 0))
            else:
                win_tekst = win_font.render("ALLE LEVELS VOLTOOID!", True, (255, 215, 0))
            win_rect = win_tekst.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            
            bg_rect = pygame.Rect(win_rect.x - 20, win_rect.y - 20, win_rect.width + 40, win_rect.height + 40)
            pygame.draw.rect(self.scherm, (0, 128, 0), bg_rect)
            pygame.draw.rect(self.scherm, (255, 215, 0), bg_rect, 4)
            self.scherm.blit(win_tekst, win_rect)
    

    def run(self):
        """Main game loop."""
        while self.actief:
            self.verwerk_input()
            self.teken()
            self.klok.tick(60)
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    print("Sokoban game")
    app = SokobanApp()
    app.run()
