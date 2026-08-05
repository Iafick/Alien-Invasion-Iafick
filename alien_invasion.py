"""
Program Name: Alien Invasion - Track 1
Author: Imran Afick
Purpose:
A side-scrolling alien shooter game created with Pygame.

Starter code:
Based on Alien Invasion project from:
https://github.com/RedBeard41/alien_Invasion_starter.git

Date:
07/25/2026
"""
import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button


class AlienInvasion:
    """Manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""

        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (
                self.settings.screen_width,
                self.settings.screen_height,
            )
        )

        pygame.display.set_caption("Alien Invasion")

        self.clock = pygame.time.Clock()

        # Create game objects.
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # Create game statistics.
        self.stats = GameStats(self)

        # Create play button.
        self.play_button = Button(self, "Play")

        self.game_active = False
        self.running = True

        # Create first alien fleet.
        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""

        while self.running:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

            self.clock.tick(60)

    def _check_events(self):
        """Respond to keyboard and mouse events."""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_play_button()

    def _check_keydown_events(self, event):
        """Respond to key presses."""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

        elif event.key == pygame.K_q:
            self.running = False

    def _check_keyup_events(self, event):
        """Respond to key releases."""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_play_button(self):
        """Start a new game when Play is clicked."""

        mouse_position = pygame.mouse.get_pos()

        if self.play_button.rect.collidepoint(mouse_position):

            if not self.game_active:
                self._start_game()

    def _start_game(self):
        """Start or restart the game."""

        self.stats.reset_stats()

        self.game_active = True

        self.bullets.empty()
        self.aliens.empty()

        self._create_fleet()
        self.ship.center_ship()

        pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        """Create a new bullet."""

        if len(self.bullets) < self.settings.bullets_allowed:

            bullet = Bullet(self)

            self.bullets.add(bullet)

    def _update_bullets(self):
        """Update bullets and remove old ones."""

        self.bullets.update()

        for bullet in self.bullets.copy():

            if bullet.rect.top >= self.settings.screen_height:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Check for bullet and alien collisions."""

        collisions = pygame.sprite.groupcollide(
            self.bullets,
            self.aliens,
            True,
            True,
        )

        if collisions:
            self.stats.score += (
                self.settings.alien_points
                * len(collisions)
            )

        if not self.aliens:

            self.bullets.empty()

            self._create_fleet()

    def _update_aliens(self):
        """Update alien positions."""

        self.aliens.update()

        if pygame.sprite.spritecollideany(
            self.ship,
            self.aliens,
        ):
            self._ship_hit()

        self._check_fleet_edges()

    def _check_fleet_edges(self):
        """Respond when aliens reach edge."""

        for alien in self.aliens.sprites():

            if alien.check_edge():

                self._ship_hit()
                break

    def _change_fleet_direction(self):
        """Drop fleet and reverse direction."""

        for alien in self.aliens.sprites():

            alien.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Respond when alien hits ship."""

        if self.stats.ships_left > 0:

            self.stats.ships_left -= 1

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()

            self.ship.center_ship()

            sleep(0.5)

        else:

            self.game_active = False

            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check if aliens reached bottom."""

        screen_rect = self.screen.get_rect()

        for alien in self.aliens.sprites():

            if alien.rect.bottom >= screen_rect.bottom:

                self._ship_hit()

                break

    def _create_fleet(self):
        """Create a fleet of aliens."""

        alien = Alien(self)

        alien_width = alien.rect.width
        alien_height = alien.rect.height

        available_space_x = (
            self.settings.screen_width
            - (2 * alien_width)
        )

        number_aliens_x = available_space_x // (
            2 * alien_width
        )

        available_space_y = (
            self.settings.screen_height
            - (3 * alien_height)
            - self.ship.rect.height
        )

        number_rows = available_space_y // (
            2 * alien_height
        )

        for row_number in range(number_rows):

            for alien_number in range(number_aliens_x):

                self._create_alien(
                    alien_number,
                    row_number,
                )

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the fleet."""

        alien = Alien(self)

        alien_width = alien.rect.width
        alien_height = alien.rect.height

        alien.x = (
            alien_width
            + (2 * alien_width * alien_number)
        )

        alien.rect.x = alien.x

       alien.rect.y = (
             self.settings.screen_height
              - alien_height
              - (2 * alien_height * row_number)
)
        )

        self.aliens.add(alien)

    def _update_screen(self):
        """Draw everything on the screen."""

        self.screen.fill(
            self.settings.bg_color
        )

        self.ship.blitme()

        for bullet in self.bullets.sprites():

            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        if not self.game_active:

            self.play_button.draw_button()

            pygame.mouse.set_visible(True)

        pygame.display.flip()


if __name__ == "__main__":

    ai = AlienInvasion()

    ai.run_game()

