import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
"""Represent one alien that moves upward toward the player's ship."""

def __init__(self, ai_game):
    """Initialize the alien and set its starting position."""

    super().__init__()

    self.screen = ai_game.screen
    self.settings = ai_game.settings

    # Load the alien image.
    self.image = pygame.image.load(
        "Assets/images/enemy_4.png"
    ).convert_alpha()

    # Create a rectangle for the alien.
    self.rect = self.image.get_rect()

    # Start the alien near the bottom of the screen.
    self.rect.x = self.rect.width
    self.rect.bottom = self.screen.get_rect().bottom

    # Store the vertical position as a decimal.
    self.y = float(self.rect.y)

def check_edge(self):
    """Return True if the alien reaches the top edge."""

    screen_rect = self.screen.get_rect()

    if self.rect.top <= screen_rect.top:
        return True

    return False

def update(self):
    """Move the alien upward toward the player's ship."""

    self.y -= self.settings.alien_speed
    self.rect.y = int(self.y)


