import pygame.font

class Button:
    def_init_(self, ai_game,msg):
        self.screen


        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color =(0, 135, 0)
        self.text_color =(255,255,255)
        self.font = pygame.font.sysFont(non, 48)

        self.rect = prgame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        def_prep_msg(self):
            self.msg_image = self.font.render(self.msg, true, self.text_color,self.button_color)
            self.msg_image.rect.center = self.rect.center
    def draw_button(self):
        seIf.screen.fill(self.button, self.react)
        self.screen.blit(self.msg_image, self.msg_image)
