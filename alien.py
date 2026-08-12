"""
Program Name: Alien Invasion
Author: Imran Afick

Purpose:
Represents alien ships that spawn at the bottom of the screen
and move upward toward the player's ship.

Starter Code:
Based on Eric Matthes' Alien Invasion project:
https://github.com/ehmatthes/pcc_3e

Date:
August,2, 2026
"""

from pathlib import Path
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Represent one alien moving upward toward the player's ship."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and rotate it to face upward.
        image_path = Path("Assets") / "images" / "enemy_4.png"
        image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.rotate(image, 180)
        self.rect = self.image.get_rect()

        # Start each new alien near the bottom left of the screen.
        self.rect.x = self.rect.width
        self.rect.bottom = self.screen.get_rect().bottom

        # Store the alien's exact horizontal and vertical position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if alien is at edge of screen (left or right)."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def check_top(self):
        """Return True if alien reaches the player's side (top of screen)."""
        screen_rect = self.screen.get_rect()
        return self.rect.top <= screen_rect.top

    def update(self):
        """Move alien right or left, per fleet_direction."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
