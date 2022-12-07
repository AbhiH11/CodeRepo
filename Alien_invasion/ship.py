import pygame
class ship:
    """A class to manage ship"""

    def __init__(self,ai_game) -> None:
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect

        self.image = pygame.image.load('Alien_invasion/Images/ship.bmp')
        # C:\Users\abhih\PycharmProjects\CodeRepo\Alien_invasion\Images
        # C:\Users\abhih\PycharmProjects\CodeRepo\Alien_invasion\Images\ship.bmp
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image,self.rect)

        
        