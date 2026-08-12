import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Manage bullets fired by the player's ship."""

    def __init__(self, ai_game):
        """Create a bullet and place it below the ship."""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Create bullet rectangle.
        self.rect = pygame.Rect( 0, 0,self.settings.bullet_width,self.settings.bullet_height,
        )
        # Start bullet below the ship.
        self.rect.midtop = ai_game.ship.rect.midbottom
        # Store decimal position.
        self.y = float(self.rect.y)


    def update(self):
        """Move the bullet downward across the screen."""
        self.y += self.settings.bullet_speed
        self.rect.y = int(self.y)


    def draw_bullet(self):
        """Draw the bullet on the game screen."""
        pygame.draw.rect(
            self.screen,
            self.settings.bullet_color,
            self.rect,
        )

