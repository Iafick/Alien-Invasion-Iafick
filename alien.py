import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""

        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image.
        self.image = pygame.image.load(
            "Assets/images/enemy_4.png"
        ).convert_alpha()

        self.rect = self.image.get_rect()

        # Start each alien near the bottom-left.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien reaches an edge."""

        screen_rect = self.screen.get_rect()

        if (
            self.rect.right >= screen_rect.right
            or self.rect.left <= 0
        ):
            return True

        return False

    def update(self):
        """Move alien horizontally."""

        self.x += (
            self.settings.alien_speed
            * self.settings.fleet_direction
        )

        self.rect.x = int(self.x)

