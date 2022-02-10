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

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.paddle.draw_paddle()
        self.paddle.update()
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # handling key pressed events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.paddle.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.paddle.moving_left = True
            # handling key released events
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.paddle.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.paddle.moving_left = False

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()


if __name__ == '__main__':
    pong = Pong()
    pong.run_game()
