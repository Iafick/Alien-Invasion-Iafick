import pygame


class Ship:
    """A class to manage the player's ship."""

    def __init__(self, game):
        """Initialize the ship and set its starting position."""

        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        # Load the ship image
        self.image = pygame.image.load(
            "Assets/images/ship.png"
        )

        self.rect = self.image.get_rect()

        # Start the ship at the bottom center
        self.rect.midbottom = self.screen_rect.midbottom

        # Store decimal position for smoother movement
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship position based on movement."""

        if self.moving_right:
            self.x += self.settings.ship_speed

        if self.moving_left:
            self.x -= self.settings.ship_speed

        # Update the rectangle position
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""

        self.screen.blit(self.image, self.rect)