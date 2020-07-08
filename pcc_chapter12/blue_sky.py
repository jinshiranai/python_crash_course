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
            self.toriel.update()
            self._update_screen()    

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                    

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.toriel.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.toriel.moving_left = True
        elif event.key == pygame.K_UP:
            self.toriel.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.toriel.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.toriel.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.toriel.moving_left = False
        elif event.key == pygame.K_UP:
            self.toriel.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.toriel.moving_down = False

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

        self.toriel_speed = 3

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Load Toriel and get her rect.
        self.image = pygame.image.load('toriel.bmp')
        self.rect = self.image.get_rect()
        
        # Start Toriel at the center of the screen.
        self.rect.center = self.screen_rect.center

    def update(self):
        """Update Toriel's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.toriel_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.toriel_speed
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.toriel_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.toriel_speed

    def blitme(self):
        """Draw Toriel at her current location."""
        self.screen.blit(self.image, self.rect)


if __name__ == '__main__':
    # Make a game instance and run the game.
    bs = BlueSky()
    bs.run_game()
