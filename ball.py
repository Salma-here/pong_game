import pygame


class Ball:

    def __init__(self, pong_game):
        self.screen = pong_game.screen
        self.screen_rect = pong_game.screen.get_rect()
        self.settings = pong_game.settings

        self.color = self.settings.ball_color
        # show ball at the mid-top of screen
        self.position = self.screen_rect.midtop
        self.radius = self.settings.ball_radius

    def draw_ball(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.radius)
