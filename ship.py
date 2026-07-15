import pygame


class Ship:
    """A class to manage the player's ship."""

    def __init__(self, game):
        """Initialize the ship and set its starting position."""

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Load the ship image
        self.image = pygame.image.load(
            "Assets/images/ship.png"
        )

        self.rect = self.image.get_rect()

        # Start the ship at the bottom center
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""

        self.screen.blit(self.image, self.rect)