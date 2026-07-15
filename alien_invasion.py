import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""

        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,
             self.settings.screen_height)
        )

        pygame.display.set_caption("Alien Invasion")

        # Create the player ship
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""

        while True:
            self._check_events()

            # Update ship position
            self.ship.update()

            # Draw the ship
            self.ship.blitme()

            pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events."""

        for event in pygame.event.get():

            # Close the game window
            if event.type == pygame.QUIT:
                sys.exit()

            # Key pressed
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True

                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            # Key released
            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False


if __name__ == '__main__':
    # Create the game and run it
    ai = AlienInvasion()
    ai.run_game()