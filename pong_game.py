import sys

import pygame

from paddle import Paddle
from ball import Ball
from settings import Settings
from timer import Timer


class Pong:

    def __init__(self):
        pygame.init()
        self.running = True
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_width()
        self.settings.screen_height = self.screen.get_height()
        pygame.display.set_caption('a game of Pong')

        self.paddle = Paddle(self)
        self.ball = Ball(self)
        self.timer = Timer(self)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.paddle.draw_paddle()
        self.ball.draw_ball()
        self.timer.draw_timer()
        self.paddle.update()
        self.ball.update()
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.USEREVENT:
                self.timer.update()
            # handling key pressed events
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # handling key released events
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.paddle.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.paddle.moving_left = True
        # press ESC to exit
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.paddle.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.paddle.moving_left = False

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            if self.ball.miss_ball():
                print('you just lost my friend.')
                break


if __name__ == '__main__':
    pong = Pong()
    pong.run_game()
