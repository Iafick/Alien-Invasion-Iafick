import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class represents one alien that moves upward towards the player."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""

        super().__init__()

        self.screen = ai_game.screen
        self.rect = self.image.get_rect()
        self.settings = ai_game.settings

        # Load the alien image.
        self.image = pygame.image.load(
            "Assets/images/enemy_4.png"
        ).convert_alpha()

        self.rect = self.image.get_rect()

       #set aliens final position
        self.rect.x = self.rect.width
        self.rect.bottom = self.rect.bottom

        # Store vertical position as decimal.
        self.y = float(self.rect.y)

    def check_edge(self):
        """Return True if alien reaches top edge."""

        screen_rect = self.screen.get_rect()

        if self.rect.top <= screen_rect.top
            return True

        return False

    def update(self):
        """Move alien upward towards the players ship."""

        self.y -= self.settings.alien_speed    
        self.rect.y = int(self.y)

