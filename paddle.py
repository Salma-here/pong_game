import pygame


class Paddle:

    def __init__(self, pong_game):
        self.screen = pong_game.screen
        self.screen_rect = pong_game.screen.get_rect()
        self.settings = pong_game.settings

        self.color = self.settings.paddle_color
        self.width = self.settings.paddle_width
        self.height = self.settings.paddle_height
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midbottom = \
            (self.screen_rect.midbottom[0], self.screen_rect.midbottom[1] - self.settings.paddle_margin)

    def draw_paddle(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
