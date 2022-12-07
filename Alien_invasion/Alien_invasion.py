import sys
import pygame
from settings import settings
from ship import ship

class AlienInvasion:
    """overall class to manage game assets and behavior"""

    def __init__(self):
        pygame.init()
        self.settings = settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alian Invasion")
        self.ship = ship(self)

        self.bg_color = (230,230,230)

    def run_game(self):
        """Start the main loop for the game."""

        while True:
            # watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            # Redraw the screen during each pass through the loop .
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()


            # make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':
    # make a code instance and run the game
    ai = AlienInvasion()
    ai.run_game()