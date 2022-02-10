import pygame


class Paddle:

    def __init__(self, pong_game):
        self.screen = pong_game.screen
        self.screen_rect = pong_game.screen.get_rect()

        self.color = (255, 255, 255)
        self.width = 70
        self.height = 10
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midbottom = self.screen_rect.midbottom

    def draw_paddle(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
