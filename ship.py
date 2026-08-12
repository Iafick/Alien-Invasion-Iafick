from pathlib import Path
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Manage the player's ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        # Load ship image using pathlib.
        image_path = Path("Assets") / "images" / "ship.png"
        image = pygame.image.load(
            image_path
        ).convert_alpha()

        # Rotate ship to face downward.
        self.image = pygame.transform.rotate(
            image,
            180
        )

        self.rect = self.image.get_rect()

        # Store decimal position.
        self.x = float(self.rect.x)

        # Movement controls.
        self.moving_right = False
        self.moving_left = False

        # Place ship at the top.
        self.center_ship()


    def center_ship(self):
        """Place the ship at the top center of the screen."""
        self.rect.midtop = self.screen_rect.midtop
        self.rect.y = 20
        self.x = float(self.rect.x)

    def update(self):
        """Move the ship left or right."""
        if (
            self.moving_right
            and self.rect.right < self.screen_rect.right
        ):
            self.x += self.settings.ship_speed

        if (
            self.moving_left
            and self.rect.left > 0
        ):

            self.x -= self.settings.ship_speed

        self.rect.x = int(self.x)



    def blitme(self):
        """Draw the ship on the screen."""

        self.screen.blit(
            self.image,
            self.rect,
        )

