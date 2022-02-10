import sys

import pygame

from paddle import Paddle
from settings import Settings


class Pong:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('a game of Pong')
        self.paddle = Paddle(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            self.paddle.draw_paddle()
            pygame.display.flip()


if __name__ == '__main__':
    pong = Pong()
    pong.run_game()
