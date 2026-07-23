import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""

        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            self.settings.resolution)
        self.clock = pygame.time.clock()
        pygame.display.set_caption("Alien Invasion")

        self.bg_color = self.settings.bg_color

        # Create the player ship
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game."""

        while True:
            self._check_events()

            # Update ship position
            self.ship.update()

            # Draw the background and ship
            self.screen.fill(self.settings.bg_color)
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











    def _create_fleet(self):
        """Create a fleet of aliens."""

    # Create an alien to get its size
    alien = Alien(self)
    alien_width = alien.rect.width













 current_x = alien_width




while current_x < self.settings.screen_width - alien_width:
         self._create_alien(current_x)
         current_x += 2 * alien_width

def _create_alien(self, x_position):
    new_alien = Alien(self)
new_alien.react.x = x_position
self.aliens.add(new_alien)

if __name__ == '__main__':
    # Create the game and run it
    ai = AlienInvasion()
    ai.run_game()