class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60,60)
        self..bullets_allowed = 5

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.scole_scale = 1.5
        self.ship_limit = 3
       
        self.initalize_dynamic_settings() 


    def initalize_dynamic_settings(self):
        self.ship_speed = 3.0
        self.alien_speed = 3.0
        self.bullet_speed = 5.0
        self.alien_points = 50

        self.fleet_direction = 1


    def increase_speed(self):
        """Increase game difficulty by adjusting speed."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
       
