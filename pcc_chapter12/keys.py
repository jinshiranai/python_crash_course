# PCC Try It Yourself 12-5. Keys.

import sys
import pygame

class Keys:
    """Overall class to manage the Keys... thing."""

    def __init__(self):
        """Initializes the... thing."""
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Keys")
        self.bg_color = (0, 0, 0)

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
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""        
        if event.key == pygame.K_q:
            sys.exit()
        else:
            print(event.key)

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.bg_color)

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game.
    keys = Keys()
    keys.run_game()