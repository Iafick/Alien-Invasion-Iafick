import pygame
from  pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the player's ship."""

    def __init__(self, ai_game):
        super()._init_()
        """Initialize the ship and set its starting position."""

        self.screen = ai_game.screen
         self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        

        # Load the ship image and get its rect.
        self.image =pygame.image.load("images/ship.png").convert_alpha
        self.rect = self.image.get_rect()
        self.center_ship()
        
        # Movement flags
        self.moving_right = False
        self.moving_left = False

        
    
    def update(self):
        """Update the ship's position based on movement flags."""

        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
