import json

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = self.load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_score(self):
        """Load the saved high score on game start."""
        filename = "high_score.json"
        try:
            with open(filename) as f:
                old_high_score = f.read()
        except FileNotFoundError:
            return 0
        else:
            return int(old_high_score)

    def save_high_score(self):
        """Save the high score on exit."""
        filename = "high_score.json"
        with open(filename, 'w') as f:
            f.write(str(self.high_score))