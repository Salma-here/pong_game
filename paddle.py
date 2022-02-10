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

        # save paddle x position in float value
        self.x = float(self.rect.x)

        # attributes to help with movement status
        self.moving_right = False
        self.moving_left = False

    def draw_paddle(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.paddle_speed
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.paddle_speed
        # update paddle rect
        self.rect.x = self.x

