import pygame.font
pygame.sprite import Group
from ship import ship

class Scoreboard:
    def_init_
    self.bg_color =(230,230,230)

    self.bullet_width +=

















    def prep_high_score(self):
        high_score =round(self_stats.high_score, -1)
        high_score_str =f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        self.high_score_rect.context = self.screen_rect.centerx


        self.high_score_rect.top = self.score_rect.top

        def show_score(self):
            self.screen.blit(self.score_image,self.score_rect)
            self.screen.blit(self.high_score_image, self.high_score_rect)
            self.screen.blit(self.level_image, self.level_rect)

            def check_high_score(self):
                if self.stats.score > self.stats.high_score:
                    self.stats.high_score = self.stats.score
                    self.prep_high_score()

                    def prep_level(self):
                        level_str =str(self.stats.level)
                        self.level_image = self.font.render(level_str,True, self.text_color, self.settings.bg_color)

                        self.level_rect =self.level_image.get_rect()
                        self.level_rect.right = self.score_rect.right
                        self.level_rect.top = self.score_rect.bottom + 10


                        def prep_ships(self):
                            self.ships = Group


