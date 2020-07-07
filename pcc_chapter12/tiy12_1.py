# Try It Yourself 12-1. Blue Sky.
# Try It Yourself 12-2. Game Character.

import sys
import pygame

class BlueSky:
    """Creates a blue game window."""

    def __init__(self):
        """Initialize properties of the game window."""
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (180, 180, 255)
        pygame.display.set_caption("Blue Sky")

        self.toriel = Toriel(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()    

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.bg_color)
        self.toriel.blitme()
        pygame.display.flip()


class Toriel:
    """A class to manage Toriel."""

    def __init__(self, bs_game):
        """Initialize Toriel and set her starting position."""
        self.screen = bs_game.screen
        self.screen_rect = bs_game.screen.get_rect()

        # Load Toriel and get her rect.
        self.image = pygame.image.load('toriel.bmp')
        self.rect = self.image.get_rect()

        # Start Toriel at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw Toriel at her current location."""
        self.screen.blit(self.image, self.rect) 


if __name__ == '__main__':
    # Make a game instance and run the game.
    bs = BlueSky()
    bs.run_game()
