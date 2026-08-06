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

        image_path = Path("Assets") / "images" / "enemy_4.png"

        image = pygame.image.load(image_path).convert_alpha()

        # Rotate alien to face upward.
        self.image = pygame.transform.rotate(image, 180)

        self.rect = self.image.get_rect()

        # Start at bottom of screen.
        self.rect.midbottom = self.screen.get_rect().midbottom
        self.y = float(self.rect.y)


    def check_edge(self):
        """Return True if alien reaches the player's side."""

        screen_rect = self.screen.get_rect()

        if self.rect.top <= screen_rect.top:
            return True
        return False

    def update(self):
        """Move alien upward."""

        self.y -= self.settings.alien_speed

        self.rect.y = int(self.y)


